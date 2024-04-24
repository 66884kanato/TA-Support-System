var arg = new Object;
var pair = location.search.substring(1).split('&');
for (var i = 0; pair[i]; i++) {
    var kv = pair[i].split('=');
    arg[kv[0]] = kv[1];
}

var params1 = arg.student_id;
var params2 = arg.ta_id;
var params3 = arg.level;
var params4 = arg.completion;
var params5 = arg.again;
var params6 = arg.skip;
var params7 = arg.kyosyu;
var params8 = arg.score;
var params9 = arg.koekake;
var params10 = arg.quest;
var params11 = arg.stage;

var student_id = params1; //学籍番号
var ta_id = params2; //ta_id
var level = params3; //レベル
var kyosyu = params7; //挙手対応数
var score = params8; //声掛け点数
var koekake = params9; //声掛け人数
var quest = params10; //クエスト
var stage = params11; //ステージ

//主にstudentinfo.html用
var count_ip = 0;
var count_att = 0;
var count_test = 0;
var count_kadai = 0;
var count_iyoku = 0;
var count_ta = 0;

//result.html用
var stage2 = 250;
var to2 = stage2 - score; //第2ステージまでの点数

//map1_room.html用
var ip_to_seat = 90; //ipアドレスと座席の実際の差
//map1_room1.html用
var ip_94_102 = 7; //ipアドレス94-102までの実際の差