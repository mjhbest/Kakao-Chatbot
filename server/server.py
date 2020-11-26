from flask import Flask, request, jsonify

import sys,os
sys.path.insert(0,os.getcwd()+"/app")

import app_time



app = Flask(__name__)
 
@app.route('/',methods = ['GET'])
def hello():
	return 'Hello, Chatbot!'

#example - time return
@app.route('/gettime', methods = ['GET'])
def time_app():
	return jsonify(app_time.time()) #time application 의 함수

# Examples
@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()
    return jsonify(user)
 
@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language":language})
 
if __name__ == "__main__":
    app.run()



