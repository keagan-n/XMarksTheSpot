from sys import argv
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
import requests
import os
from entry import Entry
from database import Database
from werkzeug.utils import secure_filename
import uuid


app = Flask(__name__, template_folder='templates')


# only allow .jpg, .png, .gif
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'static/images'


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])

def index():    

    database = Database()

    database.connect()
    entries = database.allEntries()
    database.disconnect()


    html = render_template('index.html', entries=entries)
    response = make_response(html)
    return response


@app.route('/location')
def location():
    html = render_template('location.html')
    resp = make_response(html)
    return resp


# adds user entry into database
@app.route('/addEntry', methods=['POST'])
def addEntry():


    placename = request.form.get('placename')
    description = request.form.get('description')
    location = request.form.get('location')

    # # get and process image file
    uploaded_file = request.files['file']

    filename = secure_filename(uploaded_file.filename)
    print(filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            print('Invalid image extension')
            exit(400)

        # generate random filename in case users submit the same filename
        filename = str(uuid.uuid4().int) + file_ext
        print(filename)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    else:
        print('No image file found')

    
    # imagepath should be static/images/FILE_NAME.file_ext (e.g. png or jpg)
    imagepath = app.config['UPLOAD_PATH'] + '/' + filename
    entry = Entry(placename=placename, description=description, location=location, image=imagepath)

    database = Database()

    database.connect()
    database.insertEntry(entry)
    database.disconnect()

    return redirect(url_for('index'))

@app.route('/about')
def about():
    html = render_template('about.html')
    resp = make_response(html)
    return resp





if __name__ == '__main__':
    # if len(argv) != 2:
    #     print('Usage: ' + argv[0] + ' port')
    #     exit(1)
    app.run(debug=True)

