from flask import Flask, request, jsonify

import sys,os
sys.path.insert(0,os.getcwd()+"/app")

import app_time
from word_collector import *
from article_recommendation import *
from chat_game import *
from daily_report import *


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

@app.route('/delroom/<room>')
def delroom(room):
	del_room(room)
	return room

#단어 관리 모듈
@app.route('/newword/<word_data>', methods = ['GET'])
def newword(word_data):
	args = word_data.split();
	word = args[0]
	score = args[1]
	room = ""

	for i in range(2,len(args)):
		if(len(room)!=0):
			room+= " "
		room += args[i]
	new_word(room,word,score)
	return word_data

@app.route('/delword/<word_data>', methods = ['GET'])
def delword(word_data):
	args = word_data.split();

	word = args[0]
	room = ""
	for i in range(1,len(args)):
		if(len(room)!=0):
			room+= " "
		room += args[i]

	delete_word(word,room)
	return word_data

@app.route('/resetword/<word_data>', methods = ['GET'])
def resetword(word_data):
	reset_word(word_data)
	return word_data


#게임 모듈
@app.route('/startgame/<room>', methods = ['GET'])
def startgame(room):
	return start_game(room)

@app.route('/endgame/<room>', methods = ['GET'])
def endgame(room):
	return end_game(room)

@app.route('/detect/<word_data>', methods = ['GET'])
def detect(word_data):
	args = word_data.split("_");
	result = check_msg(args[0],args[1])
	if result != None:
		return result
	return ""

@app.route('/report', methods = ['GET'])
def report():
	return jsonify(daily_report())



# 예시용 모듈
@app.route('/userLogin', methods = ['POST'])
def userLogin():
    user = request.get_json()
    return jsonify(user)
 
@app.route('/environments/<language>')
def environments(language):
    return jsonify({"language":language})
 
if __name__ == "__main__":
    app.run()



