/* 現在のURLからの情報を得る */
var now = new Object;
var pair = location.search.substring(1).split('&');
for (var i = 0; pair[i]; i++) {
    var kv = pair[i].split('=');
    now[kv[0]] = kv[1];
}

var ta_id = now.ta_id; //ta_id
var level_n = now.level; //レベル
var completion_n = now.completion; //声掛け完了
var again_n = now.again; //要再対応
var skip_n = now.skip //スキップ
var kyosyu_n = now.kyosyu; //挙手対応完了
var score_n = now.score; //スコア
var koekake_n = now.koekake; //声掛け回数
var quest_n = parseInt(now.quest) + 1; //クエスト
var stage_n = now.stage //ステージ
if(quest_n>6){
    quest_n = 6;
}
var questText = 'クエスト' + quest_n;

/* 何クラか取得 */
var scriptPath = window.location.href;
var index = scriptPath.indexOf('/C');
if (index !== -1 && index + 2 < scriptPath.length) {
    var classroom = scriptPath.substr(index + 2, 2);
} else {
    console.log("Not found or not enough characters after '/C'");
}
/* 演習室決定 */
if(classroom=="01" || classroom=="02"|| classroom=="04" || classroom=="05" || classroom=="07" || classroom=="09" || classroom=="1d"){
    var room = "1";
}else{ //classroom=="03" || classroom=="06"|| classroom=="08" || classroom=="10" || classroom=="11" || classroom=="12" || classroom=="2d"
    var room = "2";
}
console.log(classroom);




/* 前のURLから情報を得る */
const ref = document.referrer;
var before = new Object;
var pair = ref.split('&');
for (var i = 0; pair[i]; i++) {
    var kv = pair[i].split('=');
    before[kv[0]] = kv[1];
}

var level_b = before.level; //レベル
var completion_b = before.completion; //声掛け完了
var again_b = before.again; //要再対応
var skip_b = before.skip //スキップ
var kyosyu_b = before.kyosyu; //挙手対応完了
var score_b = before.score; //スコア
var koekake_b = before.koekake; //声掛け回数
var quest_b = parseInt(before.quest) + 1; //クエスト
var stage_b = before.stage //ステージ


/* 前にどのphpファイルが読み込まれたかを取得する */
// "/"と".php?"の間の文字列を取得
function get_before_php(ref){
    //URLを"/"で分割
    var parts = ref.split('/'); 
    // 最後の部分を取得
    var lastPart = parts[parts.length - 1];
    // ".php?"より前の部分を取得
    var result = lastPart.split('.php?')[0];
    return result;
}

//前回のphpファイル名取得
var php_b = get_before_php(ref);
//console.log(php_b);
var taio = ""; //taioはkoekakeかkyosyuか
var button; //buttonはnextかagainかskipかstartか
if(php_b.includes("_")){
    //"_"で分割
    var parts = php_b.split("_");
    taio = parts[0].slice(0, -1);
    taio = parts[0].slice(0, -1);
    button = parts[1];
}else{
    button = php_b.slice(0, -1);
}

//ボタン情報を更新しておく
//console.log(taio)
//console.log(button)
sessionStorage.setItem('button', button);
/*
let data = sessionStorage.getItem('button');
console.log(data); // 'value'
*/



//使いたい情報
var level_i = level_b; //一つ前のページのレベルを知りたい
var score_i = score_n - score_b; //増えた点数を知りたい
var quest_i = quest_n - quest_b; //クエストが達成されたか知りたい
var stage_i = stage_n - stage_b; //ステージの行き来情報を知りたい


/* 前回の得点を取得 */
var path_now_result = "../../now_result/"; 
var path_result = "../../result/"; 
var path_before = path_result + "result_c" + classroom + "_" + ta_id + ".csv";

function getCSVFile_before() {
  var xhr_before = new XMLHttpRequest();
  xhr_before.open("get", path_before, false);
  xhr_before.onload = function () {
    createArray_before(xhr_before.responseText);
  };
  xhr_before.send(null);
}

function createArray_before(beforeData) {
  var beforeArray = beforeData.split("\n");
  before = new Array();
  for (var i = 0; i < beforeArray.length; i++) {
    before[i] = beforeArray[i].split(",");
  }
}

getCSVFile_before();

var score_me_before = before[before.length-2][0];
//console.log(score_me_before);