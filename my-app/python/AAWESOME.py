from flask import Flask, render_template, request
from darksky import forecast
from datetime import datetime
from datetime import timedelta
import json
import numpy as np
import urllib.parse
import urllib.request

app = Flask(__name__)

aa_url = 'http://antoniodidnothingwrong-hacktx.herokuapp.com/flights?'
key = 'b83b1a21964642d7c104391dc410beb9'


@app.route('/', methods=['GET', 'POST'])
def mainFun():
    colours = ['DFW', 'ORD', 'LAX', 'JFK']
    colours2 = ['JFK', 'LAX', 'ORD', 'DFW']
    if request.method == 'GET':
        return render_template('test.html', colours=colours, colours2=colours2)

    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']
        date = request.form['date']

        flights = result(source, destination, date)

        return render_template('test.html', colours=colours, colours2=colours2, flights=flights, date=date)


def result(origin, destination, date):
    values = {'date': date}

    if origin is not None:
        values['origin'] = origin

    if destination is not None:
        values['destination'] = destination

    aa_data = urllib.parse.urlencode(values)
    req = urllib.request.Request(aa_url + aa_data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        json_responses = json.loads(the_page)

        flights = []

        for json_response in json_responses[:3]:
            origin_latitude = json_response['origin']['location']['latitude']
            origin_longitude = json_response['origin']['location']['longitude']
            destination_latitude = json_response['destination']['location']['latitude']
            destination_longitude = json_response['destination']['location']['longitude']
            duration = json_response['duration']['hours'] * 60 + json_response['duration']['minutes']

            flight = {}

            flight_number = json_response['flightNumber']

            flight['flightNumber'] = str(flight_number)

            """
            print(f'flight_num: {flight_number}')
            print(f'Origin lat:{origin_latitude}')
            print(f'Origin long:{origin_longitude}')
            print(f'Destination lat:{destination_latitude}')
            print(f'Destination long:{destination_longitude}')
            print(f'Duration: {duration}')
            """

            segment_time = 30
            hour = np.random.randint(0, 24)
            minute = np.random.randint(0, 60)
            dt = datetime.strptime(date, '%Y-%m-%d') + timedelta(hours=hour) + timedelta(minutes=minute)
            time_segments = duration // segment_time

            times = [dt + timedelta(minutes=i * segment_time) for i in range(time_segments + 1)]
            latitude_rate = (destination_latitude - origin_latitude) / time_segments
            longitude_rate = (destination_longitude - origin_longitude) / time_segments
            latitude_points = [origin_latitude + latitude_rate * i for i in range(time_segments + 1)]
            longitude_points = [origin_longitude + longitude_rate * i for i in range(time_segments + 1)]

            ret_times = []
            ret_icons = []
            percent = 0

            for i in range(len(longitude_points)):
                latitude = latitude_points[i]
                longitude = longitude_points[i]
                cast = forecast(key, latitude, longitude, time=times[i].isoformat())
                if 'icon' in cast['currently']:
                    icon = cast['currently']['icon']
                    if 'snow' in icon:
                        percent += 15
                    elif 'rain' in icon:
                        percent += 12
                    elif 'sleet' in icon:
                        percent += 10
                    elif 'wind' in icon:
                        percent += 7
                    elif 'fog' in icon:
                        percent += 4
                    elif 'partly-cloudy' in icon:
                        percent += 1
                    elif 'cloudy' in icon:
                        percent += 3
                    ret_times.append(times[i].strftime("%I:%M %p"))
                    ret_icons.append(icon)

            flight['times'] = ret_times
            flight['icons'] = ret_icons
            flight['percent'] = str(percent)

            flights.append(flight)
        return flights


if __name__ == '__main__':
    app.run(debug=True)
