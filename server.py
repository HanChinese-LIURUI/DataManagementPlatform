import os
import json
import socket
import struct
import hashlib

share_dir = r'C:\Users\Administrator\Desktop'  # 需要传输的文件所在的文件夹

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立一个socket对象
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 回收重用端口10000
phone.bind(('192.168.3.6', 10000))  # 0-65535  0-1024给操作系统，
phone.listen(5)
print('服务器已启动，等待连接')
while True:  # 建链接循环
    conn, client_addr = phone.accept()
    print("连接信息:", client_addr)
    while True:  # 通信循环
        try:
            # 1.收命令
            res = conn.recv(1024)  # get jiaoyue.mp4
            # 2.解析命令，提取相应命令参数
            cmds = res.decode('utf-8').split()  # ['get', 'jiaoyue.mp4']
            filename = cmds[1]
            # 3.以读的方式打开

            # 1制作报头
            header_dic = {
                'filename': filename,
                'file_size': os.path.getsize(r'%s/%s' % (share_dir, filename))  # 获得文件的大小单位字节
            }
            header_json = json.dumps(header_dic)
            # json.dumps()用于将字典形式的数据转化为字符串，
            # json.loads()用于将字符串形式的数据转化为字典
            header_bytes = header_json.encode('utf-8')  # 以 encoding 指定的编码格式编码字符串

            # 2 发送报头长度
            conn.send(struct.pack('i', len(header_bytes)))  # 按照给定的格式，把数据封装成字符串

            # 3 发报头
            conn.send(header_bytes)
            # 4发真实数据
            m = hashlib.md5()  # MD5验证
            with open('%s/%s' % (share_dir, filename), 'rb') as f:
                # conn.send(f.read())
                for line in f:
                    m.update(line)
                    conn.send(line)
            recv = conn.recv(1024)  # 阻塞，服务器接收客户端数据接收完成的确认
            print('客户端已接收完数据') if eval(recv.decode("utf-8")) else print('Error')
            conn.send(m.hexdigest().encode('utf-8'))  # 给客户端发送md5验证值
        except ConnectionResetError as e:
            print('Error:', e)
            break
    conn.close()
phone.close()
