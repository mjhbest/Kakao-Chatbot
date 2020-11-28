from konlpy.tag import Hannanum
hannanum = Hannanum()
from datetime import datetime
import time

# now = datetime.now()
# print(now.time())
# if (now.hour == 0 and now.minute == 0 and now.second == 0) :
#     print("hi \n")
# else:
#     print("no")

# room_members_file 은 별도 file로 써줘야 합니다!
##########
def write_room_members (room, sender):
    f = open('room_members_file', 'w', encoding='utf-8-sig', newline ='')
    reader = csv.reader(f) 
    makewrite = csv.writer(f)
    for txt in reader:
        if (txt[0] == room and txt[1] == sender):
            break       
    makewrite.writerow(room, senders)

## 수정필요
def check_new_member (members, sender): 
    if (sender in members):
        return members.index(sender)
    else:
        members.append(sender)
        return members.length-1


def add_msg(room, msg, sender, members, used_words, expressions):
    check_new_member(members, sender)
    nouns = hannanum.nouns(msg)
    for i in nouns:
        if i in expressions.keys:
            used_words[i] += 1

# def check_degree(used_words, expressions):            # 혐오표현 file (expressions) 에서 혐오표현 정도를 읽어서 file에 같이 써주기
#     # degrees

# def read_used_words (room, sender):
#     f =open("used_words_file", "w", encoding = "UTF-8")
#     reader = csv.reader(f)
#     for row in reader:
#         if (row[0] == room and row[1] == sender):
            

def alarm(room, msg, sender, replier, start_time, used_words): 
    # used_words는 sender가 사용한 혐오표현에 대한 list
    now = datetime.now()
    if (now.hour ==0 and now.minute == 0 and now.second == 0):

        response = ('사용자 ' + sender + ' 는 오늘 하루 동안 다음과 같은 혐오 표현을 사용하였습니다. \n')
        for i in used_words.keys:
            response += (str(i) + ':' + str(used_words[i]) +'회 \n')
        f = open("daily_report.csv", "w", encoding ="UTF-8")
        f.write(response)
        f.close()
        # replier.reply(response)
        initialize(room, used_words, members)
    else:
        print("Error! Not 00:00 AM")

def initialize(room, used_words, members):
    for i in used_words.keys:
        used_words[i].clear()

# def alarm(room, msg, sender, isGroupChat, replier, imageDB, packageName): 
#     used_words = dict()                                             # 이후 response 함수에서 global 변수로 지정
#     senders = []
#     return true;                                                    # 이후 response  톡방의 사람들 전체 추가
  