from flask import Flask, redirect, url_for, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
import json
import sqlite3
from sqlite3 import Error


#Configure Flask app
app = Flask(__name__)
CORS(app)

#Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" 

#set db variable as a SQLAlchemy obj tied to flask app "app"
db = SQLAlchemy(app) 

database = r"instance/pokeData.db"

def openConnection(_dbFile):
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    return conn

def closeConnection(_conn, _dbFile):
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)


    # create a database connection


#Default Route "Landing page"
@app.route('/')
def renderIndex():
        #We use the render_template command to render an html page
        return render_template('homePage.html')

@app.route('/viewAllRegions')
def viewAllRegions():
        
        sql = """SELECT * 
                 FROM region """
        
        conn = openConnection(database)
        cur = conn.cursor()
        cur.execute(sql)
        _regions = cur.fetchall()

        # print(type(_regions))

        #We can pass the obj lists as arguments to an html page using render_template.
            #We can parse through the list in the html page with Jinja2 
        return render_template('viewAllRegions.html', regions = _regions)

@app.route('/viewIndPokemon/<pokemonName>')
def viewIndPokemon(pokemonName):

    #Any query we want to diplay on the page, we fetch it as a list before passing all lists to the html page render

    sql = """SELECT * 
                 FROM pokemon
                  WHERE p_name = ? """
        
    conn = openConnection(database)
    cur = conn.cursor()
    cur.execute(sql, (pokemonName, ))
    _pokeInfo = cur.fetchall()
     
    return render_template('viewIndPokemon.html', pokeInfo = _pokeInfo)

@app.route('/viewAllPokemon')
def viewAllPokemon():

    #Any query we want to diplay on the page, we fetch it as a list before passing all lists to the html page render

    sql = """SELECT * 
                 FROM pokemon"""
        
    conn = openConnection(database)
    cur = conn.cursor()
    cur.execute(sql)
    _allPokemon = cur.fetchall()
     
    return render_template('viewAllPokemon.html', allPokemon = _allPokemon)

     

if __name__ == '__main__':

    app.run()