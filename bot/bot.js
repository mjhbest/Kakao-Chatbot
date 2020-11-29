const scriptName = "chatbot";
let start = 0;
var scores = [];
var bads = [];
/**
* (string) room
* (string) sender
* (boolean) isGroupChat
* (void) replier.reply(message)
* (boolean) replier.reply(room, message, hideErrorToast = false) // 전송 성공시 true, 실패시 false 반환
* (string) imageDB.getProfileBase64()
* (string) packageName
*/
const api_server = 'http://662578a443c3.ngrok.io';
function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
	if(msg=='hi'){
		replier.reply("Hello! I'm chatbot!");
	}
	if(msg == '/시간'){
		output = org.jsoup.Jsoup.connect(api_server + '/gettime').ignoreContentType(true).get().text();	
		replier.reply(output);
	}

	if(msg == '/시작'){
		org.jsoup.Jsoup.connect(api_server + '/' +room).ignoreContentType(true).get().text();
		replier.reply("측정을 시작합니다");
	}

	if(msg.startsWith('/단어추가')){
		org.jsoup.Jsoup.connect(api_server + '/' +room).ignoreContentType(true).get().text();
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
