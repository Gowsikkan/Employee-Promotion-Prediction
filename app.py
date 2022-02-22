from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('attr.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def man():
    return render_template('app.html')

@app.route('/predict', methods=['POST'])
def home():
        print('helo')
        data1 = int(request.form['Department'])
        data2 = int(request.form['Region'])
        data3 = int(request.form['Education'])
        data4 = int(request.form['Gender'])
        data5 = int(request.form['Recuritment'])
        data6 = int(request.form['Tranings'])
        data7 = int(request.form['Age'])
        data8 = int(request.form['Rating'])
        data9 = int(request.form['Length'])
        data10 =int(request.form['Awards'])
        data11 = int(request.form['Traning Score'])

        arr   = np.array([[data1, data3,data2, data4, data5, data6, data7, data8, data9, data10,data11]])
        pred  = model.predict(arr)
        return render_template('output.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)
