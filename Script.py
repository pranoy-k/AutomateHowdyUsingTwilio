
#login to howdy
import time
import auth
import requests
from lxml import html

USERNAME = auth.username
PASSWORD = auth.password

LOGIN_URL = "https://cas.tamu.edu/cas/login"

URL = "https://cas.tamu.edu/cas/login"

def login():

    session_requests = requests.session()

    result = session_requests.get(LOGIN_URL)

    payload = {'csrfmiddlewaretoken': 'YiCKZCqAWk1wlrwdzltQN5vWaPh04b37',
              'password': auth.password ,
              'username': auth.username }

    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    print(result.ok)


def main():

    while True:
        login()
        time.sleep(3600)


main()
