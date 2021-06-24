"""Send messages to SMTP server."""
import smtplib
import sys


def main(port):
    """Run an SMTP client to server."""
    with smtplib.SMTP(host="localhost", port=port) as smtp:
        print("Sending no-op")
        smtp.noop()
        print("Sent no-op!")


if __name__ == "__main__":
    main(sys.argv[1])
