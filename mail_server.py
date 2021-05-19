import smtplib


class MailServer:
    def __init__(self, sender, recipient, password, server):
        self.sender = sender
        self.recipient = recipient
        self.password = password
        self.server = server

    def send_mail(self, name, url, price):
        with smtplib.SMTP(self.server) as connection:
            connection.starttls()
            connection.login(self.sender, self.password)
            connection.sendmail(
                from_addr=self.sender,
                to_addrs=self.recipient,
                msg=f"Subject: Low price alert!:{name} is available below your target price! get it here \n\n{url}"
            )