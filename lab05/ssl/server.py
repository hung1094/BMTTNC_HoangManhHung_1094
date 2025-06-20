import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

# Danh sách các client đã kết nối
clients = []

def handle_client(client_socket):
    # Thêm client vào danh sách
    clients.append(client_socket)

    print("Đã kết nối với:", client_socket.getpeername())

    try:
        # Nhận và gửi dữ liệu
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))

            # Gửi dữ liệu đến tất cả các client khác
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        client.remove(client)
    except:
        clients.remove(client_socket)
    finally:
        print("Đã ngắt kết nối:", client_socket.getpeername())
                            