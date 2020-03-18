import json
import socket
import struct
import time
import hashlib

download_dir = r'C:\Users\LIU\Desktop\download'  # 文件存放地址

pc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pc.connect(('192.168.3.6', 10000))

while True:
    # 1.发命令
    cmd = input('>>>:').strip()  # get a.text
    if not cmd:
        continue
    pc.send(cmd.encode('utf-8'))

    # 2.接受文件内容，以写的方式打开一个新文件，写入客户端新文件中

    # 1收报头长度
    obj = pc.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 2接收报头
    header_bytes = pc.recv(header_size)

    # 3解析报头,对于数据的描述
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    print('获取的文件信息：', header_dic)
    total_size = header_dic['file_size']
    file_name = header_dic['filename']

    # 4 接受真实的数据
    m = hashlib.md5()  # MD5验证
    with open('%s/%s' % (download_dir, file_name), 'wb') as f:
        recv_size = 0
        StartTime = time.perf_counter()
        while recv_size < total_size:
            res = pc.recv(1024)
            f.write(res)
            m.update(res)
            recv_size += len(res)
    pc.send('True'.encode('utf-8'))
    EndTime = time.perf_counter()
    Time = EndTime - StartTime
    recv_md5 = m.hexdigest()
    recv_server_md5 = pc.recv(1024).decode("utf-8")
    print(recv_md5, '\n', recv_server_md5)
    if recv_md5 == recv_server_md5:
        print('总大小：%s  已经下载大小：%s' '总用时：%s' % (total_size, recv_size, Time))
    else:
        print('MD5验证错误')
pc.close()
