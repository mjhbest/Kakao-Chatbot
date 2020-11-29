import pandas as pd
import pickle
import gzip
import os
import sys 

surveyFile = os.getcwd() + '/../data/surveyData.pickle'
roomFile = os.getcwd() + "/../data/roomData.pickle"

class ChatRoom():
	def __init__(self,room):
		self.roomName = room
		self.wordList = []
		self.default_words()

	def default_words(self):
		with gzip.open(surveyFile,'rb') as f:
			data = pickle.load(f)
		self.wordList = data

	def add_word(self,word,score = 0):
		self.wordList[word] = score


def new_room(room):
	if not os.path.isfile(roomFile):
		init_roomData()
	
	#create new room
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	new_room = ChatRoom(room)
	data[room] = new_room

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)

def del_room(room):
	if not os.path.isfile(roomFile):
		return ;
	
	#create new room
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	data.pop(room)

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)


def new_word(word , score , room):
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	if room in data.keys():
		data[room].add_word(word,score)

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)

def delete_word(word, room):
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	if room in data.keys():
		if word in data[room].wordList:
			data[room].wordList.pop(word)

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)


def reset_word(room):
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	if room in data.keys():
		data[room].default_words()

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)


def make_survey_pickle():
	#make survey file to pickle dict
	csv = pd.read_csv(os.getcwd()+"/../../data//survey_result.csv")
	data = {}

	for i in range(len(csv)):
		word = csv.loc[i]['Word']
		score = csv.loc[i]['Mean']
		data[word] = score

	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)	 

def init_roomData():
	data = {}
	with gzip.open(roomFile,'wb') as f:
		pickle.dump(data,f)


if __name__ == '__main__':
	with gzip.open(os.getcwd() + "/../../data/roomData.pickle",'rb') as f:
		data = pickle.load(f)

	for key in data.keys():
		print(key)
		print(data[key].wordList)
