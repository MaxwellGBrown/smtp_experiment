"""Send messages to SMTP server."""
import email.message
import smtplib
import sys


def main(port):
    """Run an SMTP client to server."""
    with smtplib.SMTP(host="localhost", port=port) as smtp:
        smtp.set_debuglevel(1)

        message = email.message.EmailMessage()
        message.set_content("Hello World")
        message["Subject"] = "Hello World"
        message["From"] = "foo@test.com"
        message["To"] = "bar@test.com"

        smtp.send_message(message)
        smtp.quit()


if __name__ == "__main__":
    main(sys.argv[1])
