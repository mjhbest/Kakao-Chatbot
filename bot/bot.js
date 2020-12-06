const scriptName = "chatbot";
/**
* (string) room
* (string) sender
* (boolean) isGroupChat
* (void) replier.reply(message)
* (boolean) replier.reply(room, message, hideErrorToast = false) // 전송 성공시 true, 실패시 false 반환
* (string) imageDB.getProfileBase64()
* (string) packageName
*/
const api_server = 'http://9aeb798622a4.ngrok.io';
function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
	var args = msg.split(' ');

	if(msg=='hi'){
		replier.reply("Hello! I'm chatbot!");
	}
	if(msg == '/시간'){
		output = org.jsoup.Jsoup.connect(api_server + '/gettime').ignoreContentType(true).get().text();	
		replier.reply(output);
	}		

	
	//방 목록 단어 관리

	if(msg == '/시작'){
		org.jsoup.Jsoup.connect(api_server + '/newroom/' +room).ignoreContentType(true).get().text();
		replier.reply("측정을 시작합니다");
	}

	if(msg == '/종료'){
		org.jsoup.Jsoup.connect(api_server + '/delroom/' +room).ignoreContentType(true).get().text();
		replier.reply("측정을 종료합니다");
	}

	// 차단 단어 단어 관리
	if(args[0]=='/추가'){	
		org.jsoup.Jsoup.connect(api_server + '/newword/' +args[1]+" "+args[2] + " "+room).ignoreContentType(true).get().text();
		replier.reply(args[1]+" 단어가 추가 되었습니다");
	}
	
	if(args[0]=='/삭제'){
		org.jsoup.Jsoup.connect(api_server + '/delword/' +args[1]+ " "+room).ignoreContentType(true).get().text();
		replier.reply(args[1]+" 단어가 삭제 되었습니다");
	}
	
	if(args[0]=='/초기화'){
		org.jsoup.Jsoup.connect(api_server + '/resetword/' +room).ignoreContentType(true).get().text();
		replier.reply("단어 목록이 초기화 되었습니다.");
	}

	//게임
	if(msg == '/game-start'){
		output = org.jsoup.Jsoup.connect(api_server + '/startgame/'+room).ignoreContentType(true).get().text();
		replier.replier(output);
	}

	if(msg == '/game-end'){
		output = org.jsoup.Jsoup.connect(api_server + '/startgame/'+room).ignoreContentType(true).get().text();
		replier.replier(output);
	}

	output = org.jsoup.Jsoup.connect(api_server + '/detect/'+room+'_'+msg).ignoreContentType(true).get().text();
	if(output != undefined){
		replier.replier(output);	
	}




}

//아래 4개의 메소드는 액티비티 화면을 수정할때 사용됩니다.
function onCreate(savedInstanceState, activity) {
	var textView = new android.widget.TextView(activity);
	textView.setText("Hello, World!");
	textView.setTextColor(android.graphics.Color.DKGRAY);
	activity.setContentView(textView);
}

function onStart(activity) {}

function onResume(activity) {}

function onPause(activity) {}

function onStop(activity) {}
