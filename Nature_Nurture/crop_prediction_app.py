from flask import Flask, render_template, request

app = Flask(__name__)

import pickle
model = pickle.load(open(r"crop_predict_model.pkl",'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Product')
def product():
    return render_template("Product.html")


@app.route('/About')
def About():
    return render_template("About.html")

@app.route('/Contact')
def Contact():
    return render_template("Contact.html")

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/result', methods =['POST'])
def result():
    a =request.form["n"]
    b= request.form["p"]
    c = request.form['k']
    d =  request.form['ph']
    t=[[float(a),float(b),float(c),float(d)]]
    output= model.predict(t)
    print(t)
    print(output)  
    if output == 0:
        y="arecanut"
    if output == 1:
        y = "coffee"
    if output == 2:
        y = "maize"
    if output ==3:
        y = "paddy"
    if output == 4:
        y = "rubber"
    return render_template("result.html",y=y)

@app.route('/predictc')
def predictc():
    return render_template("predictc.html")

if __name__ == '__main__' :
    app.run(debug=False)
    
