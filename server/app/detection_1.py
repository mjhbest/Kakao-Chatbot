from konlpy.tag import Hannanum
hannanum = Hannanum()
from datetime import datetime
import os
import sys
import pickle
import gzip

surveyFile = os.getcwd() + '/../data/surveyData.pickle'
roomFile = os.getcwd() + "/../data/roomData.pickle"

class ChatRoom():
    def __init__(self,room):
            self.roomName = room
            self.wordList = []
            self.used_words = []
            self.default_words()

    def default_words(self):
            with gzip.open(surveyFile,'rb') as f:
                    data = pickle.load(f)
            self.wordList = data

    def add_word(self,word,score = 0):
            self.wordList[word] = score

    def add_used_words(self, word):
            if word in self.used_words.keys:
                self.used_words[word] += 1 

            else:
                self.used_words[word] = 1
    def clear_used_words(self):
            self.used_words = []



def detect(room, msg):
    with gzip.open(roomFile,'rb') as f:
		    data = pickle.load(f)

    if room in data.keys():
		    room_words = data[room].wordList

    nouns = hannanum.nouns(msg)
    for i in nouns:
        if i in room_words.keys: 
            data[room].add_used_words(i)

    
def alarm(room): 
    with gzip.open(roomFile,'rb') as f:
		    data = pickle.load(f)

    if room in data.keys():
            used_words = data[room].used_words
            room_words = data[room].wordList
    now = datetime.now()
    if (now.hour ==0 and now.minute == 0 and now.second == 0):

        response = ('오늘 하루 동안 다음과 같은 혐오 표현을 사용하였습니다. \n')
        for i in used_words.keys:
            response += ('표현 ' + str(i) + ': \n 혐오도: ' + str(room_words[i]) + '\n 사용한 횟수: '  + str(used_words[i]) + '\n')
        # f = open("daily_report.csv", "w", encoding ="UTF-8")
        # f.write(response)
        # f.close()
        # replier.reply(response)
        data[room].clear_used_words()
        return response
    else:
        return ("Error! Not 00:00 AM")

