"""SMTP server implementation.

SMTP RFC
https://datatracker.ietf.org/doc/html/rfc5321

SMTP Status Codes & Responses
https://datatracker.ietf.org/doc/html/rfc3463
"""
import argparse
import socket


def main(host="localhost", port=587):
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

                while True:
                    message = b""
                    while not message.endswith(b"\r\n"):
                        message += connection.recv(1024)

                    command, *rest = message.split(b" ")
                    if command == b"QUIT":
                        break
                    elif command.upper() == b"MAIL":
                        # Requires a HELO or EHLO first, with "220 OK" response

                        # Begin a Mail Transaction
                        # https://datatracker.ietf.org/doc/html/rfc5321#section-3.3

                        # 1. MAIL FROM:<sender>
                        #    250 OK -- If sender is accepted
                        #    550 or 553 if failed (TODO)
                        print(message)
                        connection.send(b"250 OK\r\n")
                        print(b">>> 250 OK\r\n")

                        # 2. RCPT TO:<recievers>
                        #    250 OK
                        reciept = b""
                        while not reciept.endswith(b"\r\n"):
                            reciept += connection.recv(1024)
                        print(reciept)
                        connection.send(b"250 OK\r\n")
                        print(b">>> 250 OK\r\n")

                        # 3. DATA\r\n
                        #    354 Intermediate
                        #
                        #    Fails if there was no MAIL or RCPT command
                        #    Return "503 Command out of sequence" or "5"
                        start_email = b""
                        while not start_email.endswith(b"\r\n"):
                            start_email += connection.recv(1024)
                        print(start_email)
                        connection.send(b"354 Intermediate\r\n")
                        print(b">>> 354 Intermediate\r\n")

                        # 4. All lines up until a line with a single period
                        #    are considered a part of the message data.
                        #    (e.g. "Hello World\r\n.\r\n")
                        email_data = b""
                        while not email_data.endswith(b"\r\n.\r\n"):
                            email_data += connection.recv(1024)
                        print(email_data)
                        connection.send(b"250 OK\r\n")
                        print(b">>> 250 OK\r\n")
                    else:
                        print(message)
                        connection.send(b"220 OK\r\n")

        print("Connection closed!")


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--host", default="localhost")
    argument_parser.add_argument("--port", default=587)

    kwargs = vars(argument_parser.parse_args())
    main(**kwargs)
