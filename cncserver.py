# cncserver.py
import socket

SERVER_HOST = "localhost"  SERVER_PORT = 12345

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[*] Listening for connections on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print("[+] Received data:", data.decode())
                # Process the received data here
        except Exception as e:
            print(f"[-] Error: {e}")

        client_socket.close()

if __name__ == "__main__":
    start_server()
