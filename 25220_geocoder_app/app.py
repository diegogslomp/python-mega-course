from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
from geopy.geocoders import Nominatim
import pandas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    return send_file(output_file, attachment_filename="output.csv", as_attachment=True)

@app.route('/success-table', methods=['POST'])
def success():
    global df
    global output_file
    if request.method == 'POST':
        try:
            uploaded_file=request.files['file']
            df = pandas.read_csv(uploaded_file)
            gc = Nominatim(scheme='http')
            df['coordinates'] = df['Address'].apply(gc.geocode)
            df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x!= None else None)
            df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x!= None else None)
            df = df.drop(['coordinates'], 1)
            output_file = 'tmp.csv'
            df.to_csv(output_file)
            return render_template('index.html', btn='download.html', table='table.html', message=df.to_html())
        except Exception as e:
            return render_template('index.html',message="Make sure you have a csv file with an address/Address column")

if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0')
    app.run()
