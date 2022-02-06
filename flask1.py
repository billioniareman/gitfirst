from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    name="Ayush Patidar"
    return render_template("C:Users\arvind\goThrough.html",name2=name)


@app.route("/about")
def about():
    name1="Aditya Agrawal"
    name2="Raj Patidar"
    name3="Ayush Patidar"
    name4="Rishabh Yadav"
    name5="Priyanshi Gupta"
    name6="Shreem Pauranik"
    return render_template("about.html",name1=name1,name2=name2,name3=name3,name4=name4,name5=name5,name6=name6)
app.run(debug=True)

@app.route("/ab")
def about():
    name="ayush"
    con="9893023657"
    email="rampra9981@gmail.com"
    c="name is "+name+" contact number is "+con+" email me on "+email
    return c
app.run(debug=True)