from konlpy.tag import Hannanum
hannanum = Hannanum()
from word_collector import *
import pandas as pd
import pickle
import gzip
import os
import sys 

life = 3
roomFile = os.getcwd() + "/../data/roomData.pickle"

def start_game(room):
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	if data[room].life != -1:
		return "게임이 이미 시작되었습니다."

	data[room].life = life

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)

	return "게임이 시작되었습니다. Life : {}".format(life)

def end_game(room):
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	if data[room].life == -1:
		return "게임이 아직 시작되지 않았습니다."

	data[room].life = -1

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)
	return "게임이 종료되었습니다."


def check_msg(room,msg):
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)
	detect = []

	if room in data.keys():
		room_words = data[room].wordDict

	morphs = hannanum.morphs(msg)
	for morph in morphs:
		for word in room_words.keys():
			if room_words[word].word in morph:
				room_words[word].used()
				detect.append(word)
		
	result = ""
	if data[room].life != -1: 
		if len(detect) != 0:
			data[room].life -= 1
			
			text = ""
			for bad in detect:
				text += bad + ","

			if data[room].life == 0:
				data[room].life = -1
				result += text
				result += " : Game Over".format(detect)
			else:
				result += text
				result += " : Life가 {0}개 남았습니다\n".format(data[room].life)
				
				for bad in detect:
					s = room_words[bad].score
					if s == '0':
						result += "사용하신 단어 '{0}'는 점수가 지정되지 않았네요!".format(bad)
					else:
						result += "사용하신 단어 '{0}'는 {1}의 혐오가 있는 단어입니다!".format(bad,s)
	print(result)
	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)
	
	return result 



if __name__ == '__main__':
	start_game("1")
	print(check_msg("1","군무새 죽어"))

	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)