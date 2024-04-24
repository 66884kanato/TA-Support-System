//学生ip&名前データ読み込み
function getCSVFile_ip() {
    var xhr_ip = new XMLHttpRequest();
    xhr_ip.open("get", "../../student/ip.csv", false);
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

//que_all.csv読み込み
function getCSVFile_que_all() {
    var xhr_que = new XMLHttpRequest();
    xhr_que.open("get", "../../que/que_all.csv", false);
    xhr_que.onload = function () {
        createArray_que_all(xhr_que.responseText);
    };
    xhr_que.send(null);
}

function createArray_que_all(queData) {
    var queArray = queData.replace(/\r/g, '').split("\n");
    que_all = new Array();
    for (var i = 0; i < queArray.length; i++) {
        que_all[i] = queArray[i].split(",");
    }
}

getCSVFile_que_all();
console.log(que_all);

//マップ作成に必要なseat_inf(IPアドレス下3桁, student_id, ta_id, level, completion, again, skip)を作成
var seat_inf = new Array();
for(var i=0; i<count_ip; i++){
    seat_inf[i] = []; // 各seat_inf[i]を空の配列として初期化(これによって2次元配列化)

    var ip_inf = ip[i][0].split(".");
    var seat_ip = parseInt(ip_inf[3]);
    seat_inf[i][0] = (seat_ip + ip_to_seat).toString(); //IPアドレスの３番目だけをseat_infの0列目に格納
    //ここからはクエリパラメータと同じ（score,koekake以外）
    seat_inf[i][1] = ip[i][1]; //seat_infの1列目にstudent_idを格納(いない場合は0が格納)
    seat_inf[i][2] = ta_id; //seat_infの2列目にta_idを格納

    for(var j=0; j<que_all.length; j++){
      if(que_all[j][0]==seat_inf[i][1]){ //que_all.csv側の学籍番号とip.csv側の学籍番号が一致したら
        seat_inf[i][3] = que_all[j][2]; //seat_infの3列目にlevelを格納
        seat_inf[i][4] = que_all[j][3]; //seat_infの4列目にcompletionを格納
        seat_inf[i][5] = que_all[j][4]; //seat_infの5列目にagainを格納
        seat_inf[i][6] = que_all[j][5]; //seat_infの6列目にskipを格納
      }
    }
  
}
 console.log(seat_inf);