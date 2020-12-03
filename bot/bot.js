const scriptName = "chatbot";
let start = 0;
var scores = [];
var bads = [];
var info = [['군무새', 1.89, 1.29, '성'], ['김치녀', 2.77, 1.04, '성'],
	['꽃뱀', 2.44, 1.46, '성'] , ['여직원', 1.18, 1.27, '성'], ['여의사', 1.18, 1.27, '성'], 
	['맘충', 2.10, 1.44, '성'], ['한남충', 2.8, 1.19, '성'], ['김여사', 2.34, 1.47, '성'],
	['개저씨', 2.23, 1.06, '성'], ['꼴페미', 2.81, 1.38, '성'], ['뚱녀', 2.55, 1.24, '성'], 
	['성괴', 1.97, 1.53, '성'], ['여적여', 2.2, 1.39, '성'], ['엠창', 2.23, 1.56, '성'], 
	['걸레', 2.72, 1.18, '성'], ['백마', 2.5, 1.32, '성'], ['외노자', 1.04, 1.10, '인종'],
	['양키', 1.44, 1.12, '인종'], ['튀기', 3.0, 0.82, '인종'], ['혼혈', 0.09, 0.29, '인종'],
	['짱깨', 2.24, 0.291, '인종'], ['조선족', 0.58, 0.92, '인종'], ['왕서방', 0.85, 1.17, '인종'],
	['쪽발이', 2.41, 1.22, '인종'], ['니그로', 2.93, 1.28, '인종'], ['코쟁이', 2.08, 1.00, '인종'],
	['검둥이', 3.09, 1.00, '인종'], ['흑형', 1.72, 1.24, '인종'], ['양놈', 2.30, 1.14, '인종'], ['똥양인', 2.87, 1.02, '인종']]

var words = ['군무새','김치녀','꽃뱀', '여직원', '여의사', '맘충', '한남충', '김여사', '개저씨',
	'꼴페미', '뚱녀', '성괴', '여적여', '엠창', '걸레', '백마', '외노자', '양키', '튀기', '혼혈', '짱깨',
	'조선족', '왕서방', '쪽발이', '니그로', '코쟁이', '검둥이', '흑형', '양놈', '똥양인']
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
	var output;

	if(msg=='hi'){
		replier.reply("Hello! I'm chatbot!");
	}
	if(msg == '/시간'){
		output = org.jsoup.Jsoup.connect(api_server + '/gettime').ignoreContentType(true).get().text();	
		replier.reply(output);
	}

	// 단어 detection 

	for (var i = 0 ; i < words.length ; i++) {
		if (msg.indexOf(words[i]) != -1) { // 표현단어 찾음 
			// 기사 받아옴 
			output = org.jsoup.Jsoup.connect(api_server + '/getarticle/' + words[i]).ignoreContentType(true).get().text();
			replier.reply(words[i] + " (이)라는 단어를 사용하셨습니다.\n\n" + words[i] + " 은(는) " + String(info[i][1]) + " 정도의 혐오도를 갖고 있는 혐오 표현 단어입니다.\n" + "(일반인 42명에게 설문조사, \n0 = (혐오도가) 없다\n1 = 조금 있다\n2 = 어느정도 있다\n3 = 꽤 포함되어 있다\n4 = 많이 포함되어 있다\n표준편차 = " + String(info[i][2]) +")\n\n" + "다음은 " + words[i] + " 과(와) 관련된 기사입니다. \n" + String(output))
		}
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