from flask import Flask
 
app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return 'Hello World. My name is Le Tran Huu Nhan'
 
app.run(host='localhost', port=5000)