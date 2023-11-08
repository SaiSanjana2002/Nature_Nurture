from flask import Flask, render_template, request

app = Flask(__name__)

import pickle
model = pickle.load(open(r"E:/TBB2/project/model.pkl",'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods =['POST'])
def login():
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
    return render_template("result.html",y = y)


if __name__ == '__main__' :
    app.run(debug=False)
    
