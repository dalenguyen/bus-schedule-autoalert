from bustracker import BusTracker

agency = 'ttc'
bus = BusTracker(agency)

# get prediction for bus stops
stops = [
    {'routeTag': 506, 'stopTag': 3292}
]

result = bus.get_predictions(stops)

incomings = result['predictions']['direction']['prediction']

bus_name = result['predictions']['routeTag']

next_buses = ''

for bus in incomings:
    next_buses += str(bus['minutes']) + ','


message = bus_name + ' will come in ' + next_buses + ' minutes'

"""
Start sending bus reminder
"""

import subprocess
args = ['your-phone-number', message]

scpt = '/Users/dnguyen/Documents/projects/python/bus-reminder/sendiMessage.scpt'

print(message)

p = subprocess.Popen(
        ['/usr/bin/osascript', scpt] + [str(arg) for arg in args], 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = p.communicate()

if p.returncode:
    print ('ERROR:', err)
else:
    print (out) # 4