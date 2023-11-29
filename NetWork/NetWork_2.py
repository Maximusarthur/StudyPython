import socket
import datetime

# 创建UDP Socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定地址和端口号
server_socket.bind(('10.100.60.103', 3033))
# 接收客户端请求
while True:
    data, addr = server_socket.recvfrom(1024)

    # 获取当前时间
    now = datetime.datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"服务器时间为：{time_str}\n接收到来自客户端 {addr} 的消息：{data.decode()}")
    # 发送响应消息
    response_words = f"来自服务器（10.100.59.169）：你已连接成功。\n来自服务器：再见！".encode()
    server_socket.sendto(response_words, addr)
