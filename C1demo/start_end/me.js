//何クラか取得
var scriptPath = window.location.href;
var index = scriptPath.indexOf('/C');
if (index !== -1 && index + 2 < scriptPath.length) {
  var classroom = scriptPath.substr(index + 2, 2);
} else {
  console.log("Not found or not enough characters after '/C'");
}

//本人の結果読み込み
var path_me = path_now_result + "now_c" + classroom +"_" + ta_id + ".csv";
function getCSVFile_me() {
  var xhr_me = new XMLHttpRequest();
  xhr_me.open("get", path_me, false);
  xhr_me.onload = function () {
    createArray_me(xhr_me.responseText);
  };
  xhr_me.send(null);
}

function createArray_me(meData) {
  var meArray = meData.split("\n");
  me = new Array();
  for (var i = 0; i < meArray.length; i++) {
    me[i] = meArray[i].split(",");
  }
}

getCSVFile_me();

//今日
var score_me_today = me[0][0];
var taio_me_today = me[0][1];
var quest_me_today = me[0][2];
var koekake_me_today = me[0][3]
var kyosyu_me_today = me[0][4];

//前回の結果読み込み
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