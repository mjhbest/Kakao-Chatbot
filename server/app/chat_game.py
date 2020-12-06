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

	detect = None
	if room in data.keys():
	    room_words = data[room].wordDict

	nouns = hannanum.nouns(msg)
	for noun in nouns:
		if noun in room_words.keys():
			print(noun)
			room_words[noun].used()
			detect = noun

	if data[room].life != -1: #if game playing
		if detect != None:
			data[room].life -= 1
			if data[room].life == 0:
				data[room].life = -1
				result = "{0} : Game Over".format(detect)
			else:
				result = "{0} : Life가 {1}개 남았습니다".format(detect,data[room].life)

	else:
		result = ""

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)
	
	return result 



if __name__ == '__main__':
	start_game("1")
	print(check_msg("1","군무새 죽어"))

	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)