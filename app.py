from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle


app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/multinomialNB')
def multinomialNB():
    return render_template('multiNB.html')

@app.route('/predict',methods=['POST'])
def predict():
	comment = request.form['comment']
	data = [comment]
	my_prediction = model.predict(data)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)