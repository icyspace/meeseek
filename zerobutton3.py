
#button press will send to api end point, 10 sec hold will shut down
#todo, connect to wifi, double/tripple clicks

from gpiozero import Button
from gpiozero import LED
from gpiozero import PWMLED
from subprocess import check_call
from signal import pause
import time
import requests
import datetime
import json as simplejson


# api-endpoint
url = "https://prod-27.centralus.logic.azure.com:443/workflows/acc0c1324fc74d709157c9b610286812/triggers/ma$
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

#startup
led = PWMLED(17)
now = datetime.datetime.now()
timestamp = now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))

data = {'id': 'meeseeks001', 'datetime': timestamp, 'message': 'Meeseeks Box On'}
requests.post(url, data=simplejson.dumps(data), headers=headers)
led.pulse(n=2, background=False)
led.value = 1

def send_logicapp():
    led.blink(on_time=.1, off_time=.1,n=1,background=False)
    led.value = 1
    # get timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))
    data = {'id': 'meeseeks001', 'datetime': timestamp, 'message': 'Button Push'}
    requests.post(url, data=simplejson.dumps(data), headers=headers)

    print("LogicApp Request Sent! : " + timestamp)

def shutdown():

    # get timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%dT%H:%M:%S') + ('-%02d' % (now.microsecond / 10000))

    data = {'id': 'meeseeks001', 'datetime': timestamp, 'message': 'Button Shutdown'}
    requests.post(url, data=simplejson.dumps(data), headers=headers)
    led.pulse(n=3, background=False)
    check_call(['sudo', 'poweroff'])

def push_button():
