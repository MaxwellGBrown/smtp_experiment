"""SMTP server implementation."""
import socket
import sys


def main(host="localhost", port=8888):
    """Run an SMTP server."""
    with socket.socket() as incoming:
        incoming.bind((host, port))

        print(f"Listening at smpt://{host}:{port}")
        incoming.listen(1024)

        while True:
            connection, (client_host, client_port) = incoming.accept()
            print(f"Connection opened from smtp://{client_host}:{client_port}")

            with connection:
                # Greet the connection
                connection.send(b"220 OK\r\n")

                message = b""
                while not message.endswith(b"\r\n"):
                    message += connection.recv(1024)

                print(message)
                connection.send(b"250 OK\r\n")
            print("Connection closed!")


if __name__ == "__main__":
    main(port=int(sys.argv[1]))
