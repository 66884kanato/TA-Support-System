var arg = new Object;
var pair = location.search.substring(1).split('&');
for (var i = 0; pair[i]; i++) {
    var kv = pair[i].split('=');
    arg[kv[0]] = kv[1];
}

var again = arg.again; //再対応
var quest = parseInt(arg.quest) + 1; //クエスト

if(again==1){
    var againText = '再対応の学生に対応しよう'
}else{
    var againText = '挙手した学生に対応しよう'
}
var questText = 'クエスト' + quest;

//何クラか取得
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



/* 前のURLから情報を得る */
const ref = document.referrer;
var before = new Object;
var pair = ref.split('&');
for (var i = 0; pair[i]; i++) {
    var kv = pair[i].split('=');
    before[kv[0]] = kv[1];
}

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
var taio = ""; //taioはkoekakeかkyosyuか
var button; //buttonはnextかagainかskipかstartか
if(php_b.includes("_")){
    //"_"で分割
    var parts = php_b.split("_");
    taio = parts[0].slice(0, -1);
    button = parts[1];
}else{
    button = php_b.slice(0, -1);
}

//ボタン情報を更新しておく
//console.log(taio);
//console.log(button);
sessionStorage.setItem('taio', taio);
sessionStorage.setItem('button', button);
/*
let data = sessionStorage.getItem('button');
console.log(data); // 'value'
*/
