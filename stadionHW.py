from requests import get
from bs4 import BeautifulSoup
import smtplib
import time

#URL
r = get("https://www.firstviennafc.at/termine.html?fbclid=IwAR3IDTnnVuvQxUOd64pIZ-3zdDEVGLiSYUfnDoXEWaKTnGF5c1VTlTPeFh8")
time.sleep(1)
soup = BeautifulSoup(r.text, features="html.parser")
# take all events from this Webpage
events = soup.find_all("div", {"class": "spieltermin-entry"})

results=""
for event in events:
    # search for "Naturarena Hohe Warte" in all events
    if ("Naturarena Hohe Warte") in event.text:
        # if event conteins "Naturarena Hohe Warte" save it in allevents
        results=allevents + event.text +"\n"
print(results)





