from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
        return "hello admin"

@app.route("/admin")
def hello_guest():
        return "hello admin"


if __name__ == '__main__':
	app.run