import socket

# 创建UDP Socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据到服务器端
server_addr = ('10.100.60.103', 3033)
data = input("请输入要发送的消息：").encode()
client_socket.sendto(data, server_addr)

# 接收服务器端的响应消息
response_data, addr = client_socket.recvfrom(1024)
print(f"接收到来自服务器端 {addr} 的响应消息：{response_data.decode()}")

# 关闭Socket连接
client_socket.close()
