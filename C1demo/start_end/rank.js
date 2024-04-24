//ランキング読み込み（リアルタイムなランキングが反映される）
var path_rank = path_result + "rank.csv";
function getCSVFile_rank() {
  var xhr_rank = new XMLHttpRequest();
  xhr_rank.open("get", path_rank, false);
  xhr_rank.onload = function () {
    createArray_rank(xhr_rank.responseText);
  };
  xhr_rank.send(null);
}

function createArray_rank(rankData) {
  var rankArray = rankData.split("\n");
  rank = new Array();
  for (var i = 0; i < rankArray.length; i++) {
    rank[i] = rankArray[i].split(",");
  }
}

getCSVFile_rank();

//ランキング表作成
function make_rank(){

  var n = rank.length;
  var f = 0;
  document.write('<table class="tabl">');
  for(i=1; i<n; i++){
    j = i - 1;
    if(rank[j][0]==score_me_today && rank[j][1]==taio_me_today && rank[j][2]==quest_me_today && f==0){
      document.write('<tr class="me"> <td>'+i+'位：</td> <td>'+rank[j][0]+'点</td> <td>対応回数：'+rank[j][1]+'回</td> <td>クエスト：'+rank[j][2]+'個</td> </tr>');
      f = 1;
    }else{
      document.write('<tr> <td>'+i+'位：</td> <td>'+rank[j][0]+'点</td> <td>対応回数：'+rank[j][1]+'回</td> <td>クエスト：'+rank[j][2]+'個</td> </tr>');
    }
  }
  document.write('</table>');

}