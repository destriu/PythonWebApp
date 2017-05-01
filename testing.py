import logging
from flask import flask

app = Flask(_name_)

# print "Content-Type: text/plain"
# print ""
# print "Congratulations, it's a web app!"

@app.route('/')
def hello():
    return "Hello"

if __name__ == '__testing__':
    app.run(host='127.0.0.1',port=8080,debug=True)
