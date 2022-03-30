from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
def home():
    
        data1 = int(request.form['Department'])
        data2 = int(request.form['Education'])
        data3 = int(request.form['Gender'])
        data4 = int(request.form['Tranings'])
        data5 = int(request.form['Age'])
        data6 = int(request.form['Rating'])
        data7 = int(request.form['Length'])
        data8 =int(request.form['Awards'])
        data9 = int(request.form['Traning Score'])

        arr   = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9]])
        pred  = model.predict(arr)
        return render_template('output.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
