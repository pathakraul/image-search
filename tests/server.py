from flask import Flask, request, render_template
from pathlib import Path
import os
import sys
import time

app = Flask(__name__)

#app route binds the urls with functions. Once the / is executed in the browser it will call this function.
# Here the index() is an view function which handles the request from a client which are routed to this function
@app.route('/')
def index():
    return "<h1> Hello World </h1>"

@app.route('/hello/')
def Hello():
    return render_template('index.html')

# this is dynamic app route which passes the name in the url to the function.
@app.route('/user/<name>')
def pathak(name):
    return "<h1> Hello {} </h1>".format(name)

def main():
    app.run(debug=True)


#export FLASK_APP=sever.py
#export FLASK_DEBUG=1
if __name__ == '__main__':
    main()
