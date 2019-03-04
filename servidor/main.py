#Importamos flask del modulo flask trae la clase flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'Hola mundo con flask.'

if __name__  == '__main__':
    app.run()#host='0.0.0.0' Es opcion para orientar de manera manual el host


