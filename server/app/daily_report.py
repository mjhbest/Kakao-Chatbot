from word_collector import *
from article_recommendation import *
import pandas as pd
import pickle
import gzip
import os
import sys

def make_text(room):
	perfect = True
	text = "어제 하루 동안 다음과 같은 단어를 사용하였습니다.\n"
	for word in room.wordDict.keys():
		w = room.wordDict[word]
		if w.history != 0:
			text += "<{0}> 혐오도 : {1}, 사용한 횟수 : {2}\n".format(w.word,w.score,w.history)
			text += "사용하신 단어 <"+word+">와 관련된 다음과 같은 기사를 추천드립니다!\n"+get_article(word)+"\n"
			perfect = False

	if perfect:
		text =  "축하합니다! 어제 하루동안 설정된 단어를 하나도 사용하지 않았습니다!"

	return text


def daily_report(): #사용한 단어 초기화
	with gzip.open(roomFile,'rb') as f:
		data = pickle.load(f)

	output = {}
	room_list = data.keys()
	for room in room_list:
		output[room] = make_text(data[room])
	return output


