from app import app
from flask import render_template, request
from werkzeug import secure_filename
from app import MLmodel

fname = ''

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def index():
	return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      fname = f.filename	
      f.save(secure_filename(fname))
      return 'file uploaded successfully'

@app.route('/predict', methods = ['GET'])
def predict():
   if request.method == 'GET':
      result = MLmodel.predict_all(fname)	
      return render_template('index.html', predict=result)

