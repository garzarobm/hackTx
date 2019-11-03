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
key = '605880dc58036d59e4a24c7f244a7a09'


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

        result(source, destination, date)

        data = str(source) + str(destination) + str(date)
        return render_template('test.html', colours=colours, colours2=colours2, text=data)


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

        for json_response in json_responses[:1]:
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

            hour = np.random.randint(0, 24)
            minute = np.random.randint(0, 60)
            dt = datetime.strptime(date, '%Y-%m-%d') + timedelta(hours=hour) + timedelta(minutes=minute)
            time_segments = duration // 15

            times = [dt + timedelta(minutes=i * 15) for i in range(time_segments + 1)]
            latitude_rate = (destination_latitude - origin_latitude) / time_segments
            longitude_rate = (destination_longitude - origin_longitude) / time_segments
            latitude_points = [origin_latitude + latitude_rate * i for i in range(time_segments + 1)]
            longitude_points = [origin_longitude + longitude_rate * i for i in range(time_segments + 1)]

            ret_times = []
            ret_icons = []

            for i in range(len(longitude_points)):
                latitude = latitude_points[i]
                longitude = longitude_points[i]
                cast = forecast(key, latitude, longitude, time=times[i].isoformat())
                if 'icon' in cast['currently']:
                    icon = cast['currently']['icon']
                    ret_times.append(times[i].strftime("%Y-%m-%d %H:%M:%S"))
                    ret_icons.append(icon)

            flight['times'] = ret_times
            flight['icons'] = ret_icons
            flights.append(flight)
        return flights


if __name__ == '__main__':
    app.run(debug=True)
