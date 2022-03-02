from pip._vendor import requests
import time
url = 'http://www.google.com'
timeout = 5
while True:
    try:
        request = requests.get(url, timeout=timeout)
        print ('Connected to the Internet')
    except (requests.ConnectionError, requests.Timeout) as exception:
        print ('No internet connection.')
    time.sleep(4)