//学生ip&名前データ読み込み
function getCSVFile_ip() {
    var xhr_ip = new XMLHttpRequest();
    xhr_ip.open("get", "../../../student/ip.csv", false);
    xhr_ip.onload = function () {
    createArray_ip(xhr_ip.responseText);
    };
    xhr_ip.send(null);
}

function createArray_ip(ipData) {
    var ipArray = ipData.split("\n");
    ip = new Array();
    for (var i = 0; i < ipArray.length; i++) {
    ip[i] = ipArray[i].split(",");
    count_ip++;
    }
}

getCSVFile_ip();

var student_name;
for (var p = 0; p < count_ip; p++) {
    if (student_id == ip[p][1]) {
    student_name = ip[p][2];
    }
}
//console.log(student_name);


//学生出席データ読み込み
function getCSVFile_att() {
    var xhr_att = new XMLHttpRequest();
    xhr_att.open("get", "../../../student/" + student_id + "/" + student_id + "_att.csv", false);
    xhr_att.onload = function () {
    createArray_att(xhr_att.responseText);
    };
    xhr_att.send(null);
}

function createArray_att(attData) {
    var attArray = attData.split("\n");
    att = new Array();
    for (var i = 0; i < attArray.length; i++) {
    att[i] = attArray[i].split(",");
    count_att++;
    }
}

getCSVFile_att();


//学生確認テストデータ読み込み
function getCSVFile_test() {
    var xhr_test = new XMLHttpRequest();
    xhr_test.onload = function () {
    createArray_test(xhr_test.responseText);
    };

    xhr_test.open("get", "../../../student/" + student_id + "/" + student_id + "_test.csv", false);
    xhr_test.send(null);
}

function createArray_test(testData) {
    var testArray = testData.split("\n");
    test = new Array();
    for (var i = 0; i < testArray.length; i++) {
    test[i] = testArray[i].split(",");
    count_test++;
    }
}

getCSVFile_test();

//学生課題データ読み込み
function getCSVFile_kadai() {
    var xhr_kadai = new XMLHttpRequest();
    xhr_kadai.onload = function () {
    createArray_kadai(xhr_kadai.responseText);
    };

    xhr_kadai.open("get", "../../../student/" + student_id + "/" + student_id + "_kadai.csv", false);
    xhr_kadai.send(null);
}

function createArray_kadai(kadaiData) {
    var kadaiArray = kadaiData.split("\n");
    kadai = new Array();
    for (var i = 0; i < kadaiArray.length; i++) {
    kadai[i] = kadaiArray[i].split(",");
    count_kadai++;
    }
}

getCSVFile_kadai();


//学生意欲データ読み込み
function getCSVFile_iyoku() {
    var xhr_iyoku = new XMLHttpRequest();
    xhr_iyoku.onload = function () {
    createArray_iyoku(xhr_iyoku.responseText);
    };

    xhr_iyoku.open("get", "../../../student/" + student_id + "/" + student_id + "_iyoku.csv", false);
    xhr_iyoku.send(null);
}

function createArray_iyoku(iyokuData) {
    var iyokuArray = iyokuData.split("\n");
    iyoku = new Array();
    for (var i = 0; i < iyokuArray.length; i++) {
    iyoku[i] = iyokuArray[i].split(",");
    count_iyoku++;
    }
}

getCSVFile_iyoku();


//学生希望データ読み込み
function getCSVFile_ta() {
    var xhr_ta = new XMLHttpRequest();
    xhr_ta.onload = function () {
    createArray_ta(xhr_ta.responseText);
    };

    xhr_ta.open("get", "../../../student/" + student_id + "/" + student_id + "_ta.csv", false);
    xhr_ta.send(null);
}

function createArray_ta(taData) {
    var taArray = taData.split("\n");
    ta = new Array();
    for (var i = 0; i < taArray.length; i++) {
    ta[i] = taArray[i].split(",");
    count_ta++;
    }
}

getCSVFile_ta();


student_att = new Array();
student_test = new Array();
student_test2 = new Array();
student_kadai = new Array();
student_iyoku = new Array();
student_ta = new Array();

for (var s = 0; s < count_att; s++) {
    student_att[s] = Number(att[s][1]);
}
for (var st = 0; st < count_test; st++) {
    student_test[st] = Number(test[st][1]);
}
for (var st2 = 0; st2 < count_test; st2++) {
    student_test2[st2] = Number(test[st2][2]);
}
for (var sk = 0; sk < count_kadai; sk++) {
    student_kadai[sk] = Number(kadai[sk][1]);
}
for (var si = 0; si < count_iyoku; si++) {
    student_iyoku[si] = Number(iyoku[si][1]);
}
for (var sta = 0; sta < count_ta; sta++) {
    student_ta[sta] = Number(ta[sta][1]);
}
