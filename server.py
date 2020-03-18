import json
import os
import socket
import struct

share_dir = r'C:\Users\LIU\Desktop\YSDBarCodeWeb'  # 需要传输的文件所在的文件夹

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#建立一个socket对象
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 回收重用端口10000
phone.bind(('192.168.3.6', 10000))  # 0-65535  0-1024给操作系统，
phone.listen(5)
print('stearting')
while True:  # 建链接循环
    conn, client_addr = phone.accept()
    print(client_addr)
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
                'md5': 'xxdxx',
                'file_size': os.path.getsize(r'%s/%s' % (share_dir, filename))
                # E:\study\第3模块，面向对象\网络编程\文件传输\SERVER\share\jiaoyue.mp4
            }
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')

            # 2 发送报头长度
            conn.send(struct.pack('i', len(header_bytes)))  # 固定长度4

            # 3 发报头
            conn.send(header_bytes)
            # 4发真实数据
            with open('%s/%s' % (share_dir, filename), 'rb') as f:
                # conn.send(f.read())
                for a in f:
                    conn.send(a)
        except ConnectionResetError:
            break
    conn.close()
phone.close()
