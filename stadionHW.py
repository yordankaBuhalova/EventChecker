from requests import get
from bs4 import BeautifulSoup
import smtplib
import time


r = get("https://www.firstviennafc.at/termine.html?fbclid=IwAR3IDTnnVuvQxUOd64pIZ-3zdDEVGLiSYUfnDoXEWaKTnGF5c1VTlTPeFh8")
time.sleep(1)


soup = BeautifulSoup(r.text, features="html.parser")

events = soup.find_all("div", {"class": "spieltermin-entry"})
allevents=""
for event in events:

    if ("Naturarena Hohe Warte") in event.text:

        allevents=allevents + event.text +"\n"


print(allevents)



