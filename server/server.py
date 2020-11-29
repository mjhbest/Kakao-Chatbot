from flask import Flask, request, jsonify

import sys,os
sys.path.insert(0,os.getcwd()+"/app")

import app_time
from word_collector import *



app = Flask(__name__)
 
@app.route('/',methods = ['GET'])
def hello():
	return 'Hello, Chatbot!'

@app.route('/init',methods = ['GET'])
def init():
	return 

#example - time return
#time application 의 함수
@app.route('/gettime', methods = ['GET'])
def time_app():
	return jsonify(app_time.time()) 

#방 생성
@app.route('/newroom/<room>')
def newroom(room):
	new_room(room)
	return room

#####단어 추가 모듈
@app.route('/newword/<word_data>', methods = ['GET'])
def newword(word_data):
	args = word_data.split();
	if len(args) == 2 :
		args.append(0)
	new_word(args[0],args[1],args[2])
	return word_data

@app.route('/delword/<word_data>', methods = ['GET'])
def delword(word_data):
	args = word_data.split();
	delete_word(args[0],args[1])
	return word_data

@app.route('/resetword/<word_data>', methods = ['GET'])
def resetword(word_data):
	reset_word(word_data)
	return word_data

# 예시 모
@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()
    return jsonify(user)
 
@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language":language})
 
if __name__ == "__main__":
    app.run()



