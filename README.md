# Bus Reminder Scheduler

Send iMessage to alert the bus schedule every morning before going working.

## How it works

Every moring, before going out of the house, I have to send a message to TTC or check Google Maps to see when the bus will come.

I'm bored with this mundane task, so I wrote a bus scheduler to send me an iMessage to notify when the bus will come, I can have time to prepare.

If you are not using TTC, check the your bus provider from [NextBus](http://webservices.nextbus.com/service/publicXMLFeed?command=agencyList)

## How to get started

The script is based on [bustracker](https://github.com/dalenguyen/bustracker) python package. Make sure that you have it install on your machine.

```bash
pip install bustracker
```

Then replace the routeTag and stopTag with your own.

```python
# bus_reminder.py
stops = [
    {'routeTag': 506, 'stopTag': 3292}
]
```

And don't forget the phone number

```python
# bus_reminder.py
args = ['your-phone-number', message]

```

What you need is a running Mac in order to send iMessage from. I schedule the script to send me a mesage from Monday to Friday at 7:30AM

```bash
crontab -e
```

Remember to edit the path of your python and script

```shell
30 7 * * 1-5 /usr/local/bin/python3 /Users/dnguyen/Documents/projects/bus-reminder/bus_reminder.py # bus reminder
```

## Reference

Thanks [aktau](https://gist.github.com/aktau/8958054) for the iMessage script.
