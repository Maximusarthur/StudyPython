import socket
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
def get_server_ip(url):
    ip = socket.gethostbyname(url)
    return ip
if __name__ == '__main__':
    local_ip = get_local_ip()
    print(f"本机IP地址为： {local_ip}")
    for i in range(3):
        url = input("请输入URL地址：")
        server_ip = get_server_ip(url)
        print(f"{url} 的IP地址为：{server_ip}")
