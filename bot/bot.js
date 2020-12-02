const scriptName = "chatbot";
let start = 0;
var scores = [];
var bads = [];
var words = [['군무새', 1.89, 1.29, '성'], ['김치녀', 2.77, 1.04, '인종'],
	['꽃뱀', 2.44, 1.46, '성'] , ['여직원', 1.18, 1.27, '성'], ['여의사', 1.18, 1.27, '성'], 
	['맘충', 2.10, 1.44, '성'], ['한남충', 2.8, 1.19, '성'], ['김여사', 2.34, 1.47, '성'],
	['개저씨', 2.23, 1.06, '성'], ['꼴페미', 2.81, 1.38, '성'], ['뚱녀', 2.55, 1.24, '성'], 
	['성괴', 1.97, 1.53, '성'], ['여적여', 2.2, 1.39, '성'], ['엠창', 2.23, 1.56, '성'], 
	['걸레', 2.] ]

/**
* (string) room
* (string) sender
* (boolean) isGroupChat
* (void) replier.reply(message)
* (boolean) replier.reply(room, message, hideErrorToast = false) // 전송 성공시 true, 실패시 false 반환
* (string) imageDB.getProfileBase64()
* (string) packageName
*/
const api_server = 'http://e8a59214407f.ngrok.io';
function response(room, msg, sender, isGroupChat, replier, imageDB, packageName) {
	var args = msg.split(' ');

	if(msg=='hi'){
		replier.reply("Hello! I'm chatbot!");
	}
	if(msg == '/시간'){
		output = org.jsoup.Jsoup.connect(api_server + '/gettime').ignoreContentType(true).get().text();	
		replier.reply(output);
	}

	// 단어 detection 

	
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

	//Daily Repory
	// if(packageName == "com.xfl.msgbot"){
	// 	Api.replyRoom("test","msg");
	// }

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