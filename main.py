from C1337 import Auth
from time import sleep
import getpass
import datetime

url = 'https://candidature.1337.ma/users/sign_in'
email = input("Email : ")
password = getpass.getpass('Password : ')
c = Auth(url, email, password)
c.delay = 2
c.launchBrowser()
c.login()

isCheckinAvailable = not c.check()
i = 1
while(isCheckinAvailable):
    print("{}: Attempt {}, check-in is not available yet .. ".format(
        datetime.datetime.now(), i))
    sleep(30) # Sleep every 30 seconds, don't ddos the server :3
    c.refresh()
    if(c.disconnected()):
        c.login()
    isCheckinAvailable = not c.check()
    i += 1

