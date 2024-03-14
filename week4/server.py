import socket

def server_program():
    # Get the hostname
    host = socket.gethostname()
    port = 5000  # Choose a port number above 1024

    # Create a socket instance
    server_socket = socket.socket()

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)  # Maximum number of queued connections

    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Send a welcome message to the client
        client_socket.send("Welcome to the server!".encode())

        # Receive data from the client
        data = client_socket.recv(1024).decode()
        print(f"Received from client: {data}")

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    server_program()
