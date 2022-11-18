1   from flask import Flask, render_template, request
2   import numpy as np
3   import pickle
4
5
6   app = Flask(__name__)
7   model = pickle.load(open('Liver2.pkl', 'rb'))
8
9   @app.route('/',methods=['GET'])
10  def Home():
11       return render_template('index.html')
12
13  @app.route("/predict", methods=['POST'])
14  def predict():
15      if request.method == 'POST':
16           Age = int(request.form['Age'])
17           Gender = int(request.form['Gender'])
18           Total_Bilirubin = float(request.form['Total_Bilirubin'])
19           Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
20           Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
21           Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
22           Total_Protiens = float(request.form['Total_Protiens'])
23           Albumin = float(request.form['Albumin'])
24           Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])
25
26
27           values = np.array([[Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
28           prediction = model.predict(values)
29
30           return render_template('result.html', prediction=prediction)
31
32
33   if __name__ == "__main__":
34       app.run(debug=True)
