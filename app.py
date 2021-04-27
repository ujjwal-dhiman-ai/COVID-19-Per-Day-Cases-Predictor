from flask import Flask, render_template, request
import requests
import pickle

app = Flask(__name__)
filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
# prediction = loaded_model.predict([[2021,4,25]])
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Day = int(request.form['Day'])
        Month = int(request.form['Month'])
        Year = int(request.form['Year'])
        prediction = loaded_model.predict([[Year,Month,Day]])
        return render_template('index.html',prediction_text="Number Of Cases On Above Entered Date: {}".format(int(prediction)))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)   