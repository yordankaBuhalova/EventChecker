from requests import get
from bs4 import BeautifulSoup
import time
import smtplib, ssl

def getResult(events):
    results=''
    for event in events:
        # search for "Naturarena Hohe Warte" in all events
        if ("Naturarena Hohe Warte") in event.text:
            # if event contains "Naturarena Hohe Warte" save it in results
            results=results + event.text +"\n"
    return results

#URL
r = get("https://www.firstviennafc.at/termine.html")
time.sleep(1)
soup = BeautifulSoup(r.text, features="html.parser")
# take all events from this Webpage
events = soup.find_all("div", {"class": "spieltermin-entry"})
# search for Hohe Warte Events
results= getResult(events)

smtp_server = 'smtp.gmail.com'
port = 587 # For starttls
sender_email = 'etest932@gmail.com'
password = input('Type your password and press enter:')

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password) # log in

    receiver_email = 'test@gmail.at' # SET RECEIVER EMAIL

    SUBJECT ='Stadion Hohe Warte: Events'
    TEXT = results
    if TEXT=='':
        TEXT='No Events' # if no Events send this message
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

