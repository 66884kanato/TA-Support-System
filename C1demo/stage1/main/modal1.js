/* フィードバック内容設定 */
var feedback; //フィードバック
var content; //フィードバック内容
var reward; //報酬説明

//声掛けレベル
var star;
if(level_i==1){ //🟩
  star = '⭐️';
}else if(level_i==2){ //🟩
  star = '⭐️⭐️';
}else if(level_i==3){ //🟩
  star = '⭐️⭐️⭐️';
}else if(level_i==4){ //🟨
  star = '⭐️⭐️⭐️⭐️';
}else if(level_i==5){ //🟨
  star = '⭐️⭐️⭐️⭐️⭐️';
}else if(level_i==6){ //🟨
  star = '⭐️⭐️⭐️⭐️⭐️⭐️';
}else if(level_i==7){ //🟥
  star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
}else if(level_i==8){ //🟥
  star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
}else{ //🟥
  star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
}

if(taio=="koekake"){

  if(button=="complete"){

    feedback = "ナイス声掛け!!🎉"
    content = "次の学生にも声を掛けてみよう!"
    if(quest_i>0){
      reward = "声掛け＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
    }else{
      reward = "声掛け報酬(Lv." + star + ")＋対応時間 → " + score_i + "点"
    }
  
  }else if(button=="again"){

    feedback = "ナイス声掛け!!🎉"
    content = "また後で対応してあげよう!"
    if(quest_i>0){
      reward = "声掛け＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
    }else{
      reward = "声掛け報酬(Lv." + star + ")＋対応時間 → " + score_i + "点"
    }

  }else if(button=="necessary"){

    feedback = "声掛け開始!!"
    content = "ナイス発見です👍"
    reward = "分からなかったら先生に聞こう"

  }else if(button=="unnecessary"){

    feedback = "ナイス巡回!!🎉"
    content = "次の学生の座席にも行ってみよう!"
    reward = "巡回報酬 → " + score_i + "点"

  }else{ 
    //koekakeなのでそもそもここは実行されない
  }

}else{

  if(button=="complete"){
    
    feedback = "ナイス対応!!🎉"
    content = "次の学生も助けてあげよう!"
    if(quest_i>0){
      reward = "対応＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
    }else{
      reward = "対応報酬(Lv." + star + ")＋対応時間→ " + score_i + "点"
    }
  
  }else if(button=="necessary"){

    feedback = "挙手対応開始!!"
    content = "困っている学生を助けてあげよう👍"
    reward = "分からなかったら先生に聞こう"

  }else if(button=="again"){

    feedback = "ナイス対応!!🎉"
    content = "また後で対応してあげよう!"
    if(quest_i>0){
      reward = "対応＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
    }else{
      reward = "対応報酬(Lv." + star + ")＋対応時間→ " + score_i + "点"
    }

  }else if(button=="start" && quest_n==1){

    feedback = "ゲーム目標"
    content = "問題を抱え込む学生を助けてあげよう!!" 
    if(score_me_before!=0){
      reward = "前回の得点: " + score_me_before + "点";
    }else{
      reward = "";
    }

  }else if(button=="start" && quest_n!=1){

    feedback = "第1ステージ"
    content = "慣れたらまた第2ステージに行こう!!" 
    reward = "";

  }else{
    //skipの場合はモーダルウィンドウ表示しない
  }

}


/* モーダルウィンドウ設定 */
var contentElement = document.createElement('div');
contentElement.id = 'easyModal';
contentElement.className = 'modal';

contentElement.innerHTML = `
  <div class="modal-content">
    <div class="modal-header"> <!--上側-->
      <h1 align="center">`+ feedback +`</h1>
    </div>
    <div class="modal-body">
      <h1 align="center">` + content + `</h1>
      <h1 align="center">` + reward + `</h1>
    </div>
  </div>
`;

if(button!="skip" && button!="necessary" && button!="back"){ //skipじゃないならモーダルウィンドウ表示

  document.body.appendChild(contentElement);

  //モーダル生成
  const modal = document.getElementById('easyModal');

  // ページが読み込まれた時
  document.addEventListener('DOMContentLoaded', function(){
    modalOpen();
    setTimeout(modalClose, 3500); //3秒後modalClose
  });

  //モーダルopen
  function modalOpen() {
    modal.style.display = 'block';
  }

  //ゆっくりモーダルclose
  function modalClose() {
    modal.classList.add('closing');
    setTimeout(() => {
      modal.style.display = 'none';
      modal.classList.remove('closing');
    }, 1000); // Adjust the timeout to match the animation duration
  }

  // モーダルコンテンツ以外がクリックされた時
  addEventListener('click', outsideClose);
  function outsideClose(e) {
    if (e.target == modal) {
      modal.style.display = 'none';
    }
  }

}

