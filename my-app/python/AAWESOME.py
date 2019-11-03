from flask import Flask, request
import json
import urllib.parse
import urllib.request

app = Flask(__name__)

url = 'http://antoniodidnothingwrong-hacktx.herokuapp.com/flights?'


@app.route('/', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        origin = request.args.get('origin', None)
        destination = request.args.get('destination', None)
        date = request.args.get('date', None)

        if date is None:
            date = '2020-01-01'

        values = {'date': date}

        if origin is not None:
            values['origin'] = origin

        if destination is not None:
            values['destination'] = destination

        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(url + data)
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')
            json_responses = json.loads(the_page)
            for json_response in json_responses:
                origin_latitude = json_response['origin']['location']['latitude']
                origin_longitude = json_response['origin']['location']['longitude']
                destination_latitude = json_response['destination']['location']['latitude']
                destination_longitude = json_response['destination']['location']['longitude']
                duration = json_response['duration']['hours']*60 + json_response['duration']['minutes']

                flight_number = json_response['flightNumber']
                print(f'flight_num: {flight_number}')
                print(f'Origin lat:{origin_latitude}')
                print(f'Origin long:{origin_longitude}')
                print(f'Destination lat:{destination_latitude}')
                print(f'Destination long:{destination_longitude}')
                print(f'Duration: {duration}')
                print()


if __name__ == '__main__':
    app.run(debug=True)
