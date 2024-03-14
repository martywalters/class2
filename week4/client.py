import socket

def client_program():
    # Get the server hostname
    host = socket.gethostname()
    port = 5000

    # Create a socket instance
    client_socket = socket.socket()

    # Connect to the server
    client_socket.connect((host, port))

    # Send a message to the server
    message = input("Enter a message to send: ")
    client_socket.send(message.encode())

    # Receive the server's response
    data = client_socket.recv(1024).decode()
    print(f"Received from server: {data}")

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    client_program()
