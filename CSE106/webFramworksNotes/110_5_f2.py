

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route("/")
def index(name):
        return render_template("f2.html")
@app.route("/success/<name>/<password>")
def success(name, password):
        return "hello %s, your password is %s" % name, password


@app.route("/login", methods = ['POST'])
def login():
        user = request.form['name']
        password = request.form['password']
        return redirect(url_for('success', name = user, password=password))


@app.route("/hello/<name>")
def hello(name):
	return render_template("hello.html", name = name) 
        #return html page with plugged in variables



if __name__ == '__main__':
	app.run()