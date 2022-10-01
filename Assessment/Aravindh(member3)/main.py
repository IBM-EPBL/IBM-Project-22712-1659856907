from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def fun():
    return render_template("index.html")

@app.route('/post')
def first():
    return render_template("login.html")

@app.route('/index')
def go():
    return render_template("index.html")

@app.route('/about')
def abt():
    return render_template("mainindex.html")

if(__name__)=="__main__":
    app.run(debug=True)