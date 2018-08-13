from flask import Flask
from flask import request,redirect,session,g,Response,render_template
import  models
import user_models

app = Flask(__name__)

mydata = ""

@app.route('/')
def hello_world():
    #return render_template('test.html')
    return 'Hello World!'

@app.route("/usergraph/")
def user_graph():
    conn, cursor = user_models.init()
    global mydata
    req = request.args
    user_id = req['user']
    mydata = user_models.execute(conn, cursor, user_id)
    return render_template('test.html')

@app.route("/usergraph/data")
def data():
	return mydata

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
