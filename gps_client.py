import gps
import requests

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


while True:
	try:
		report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		if report['class'] == 'TPV':
			payload = {'lat': report.lat, 'lng': report.lon }
			r = requests.post("http://192.168.1.8:4567/line/2/bus/3/location", data=payload)	
	except KeyError:
		print 'KeyError'
		pass
	except KeyboardInterrupt:
		quit()
	except StopIteration:
		session = None
		print "GPSD has terminated"
