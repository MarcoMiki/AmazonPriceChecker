from scraper import Scraper
from watchlist import watchlist
from mail_server import MailServer
import os

# details of the email you are sending from, its password, its smtp server and the email you are sending to. Either
# add yours as environmental variables or declare them as strings
SENDER = os.environ.get("SENDER")
RECIPIENT = os.environ.get("RECIPIENT")
PASSWORD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")

mail_server = MailServer(sender=SENDER, recipient=RECIPIENT, password=PASSWORD, server=SERVER)

for item in watchlist:
    scraper = Scraper(item["url"])
    if scraper.check_price(item["target_price"]):
        mail_server.send_mail(name=item["name"], url=item["url"], price=scraper.price)
