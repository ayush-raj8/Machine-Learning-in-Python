from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


# Load the CLassifier model
filename = 'model.pkl'
classifier = pickle.load(open(filename,'rb'))

@app.route('/')
def home():
    return render_template('diabetes.html')


@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes1():
    if request.method == 'POST':
        glucose = float(request.form['Glucose'])
        insulin = float(request.form['Insulin'])
        data = np.array([[glucose, insulin]])
        my_prediction = float(classifier.predict(data))
        return render_template('d_result.html',prediction=my_prediction,glucose=glucose,insulin=insulin)


if __name__ == '__main__':
	app.run(debug=True)
