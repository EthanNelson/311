import csv
import urllib2
import json
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():

	url = 'https://data.cityofchicago.org/resource/m4zg-aj7c.json'
	# pretend to be a chrome 47 browser on a windows 10 machine
	response = urllib2.urlopen(url)
	data = response.read()
	data2 = json.loads(data)
    # csv_path = './static/la-riots-deaths.csv'
	# csv_file = open(data, 'r')
	# csv_obj = csv.DictReader(csv_file)
	# csv_list = list(csv_obj)
	# read = csv.DictReader(data)
	# csv_list = list(read)
	#csv_list = list(data)
	return data2

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)