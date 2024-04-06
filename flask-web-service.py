from flask import Flask
app = Flask('MyCoolWebService')

@app.route('/')
def hello_world():
    return 'Hello World! '

@app.route('/fromtatiana')
def hello_tatiana():
    return 'Hello World from Tatiana! '


app.run(host='0.0.0.0', port=5000)()