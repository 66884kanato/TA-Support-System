/* フィードバック内容設定 */
var feedback; //フィードバック
var content; //フィードバック内容
var reward; //報酬説明

//声掛け重要度
var star;
if(level_i==1){ //重要度1
  star = '⭐️';

}else if(level_i==2){ //重要度2
  star = '⭐️⭐️';
}else if(level_i==3){ //重要度3
  star = '⭐️⭐️⭐️';
}else if(level_i==4){ //重要度4
  star = '⭐️⭐️⭐️⭐️';
}else if(level_i==5){ //重要度5
  star = '⭐️⭐️⭐️⭐️⭐️';
}else if(level_i==6){ //重要度6
  star = '⭐️⭐️⭐️⭐️⭐️⭐️';
}else if(level_i==7){ //重要度7
  star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
}else if(level_i==8){ //重要度8
  star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
}else{ //重要度9
  star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
}


if(taio=="koekake"){

  if(button=="complete"){

    feedback = "ナイス声掛け!!🎉"
    content = "次の学生にも声を掛けよう!"
    if(quest_i>0){
      reward = "声掛け＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
    }else{
      reward = "声掛け報酬(重要度" + star + ")＋対応時間 → " + score_i + "点"
    }
  
  }else if(button=="again"){

    feedback = "ナイス声掛け!!🎉"
    content = "また後で対応してあげよう!"
    if(quest_i>0){
      reward = "声掛け＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
    }else{
      reward = "声掛け報酬(重要度" + star + ")＋対応時間 → " + score_i + "点"
    }

  }else{ 
    //koekakeなのでそもそもここは実行されない
  }

}else{

  if(button=="complete"){

    if(again_b==1){ //再対応なら
      feedback = "ナイス声掛け!!🎉"
      content = "次の学生も助けてあげよう!"
      if(quest_i>0){
        reward = "声掛け＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
      }else{
        reward = "声掛け報酬(重要度" + star + ")＋対応時間 → " + score_i + "点"
      }
    }else{
      feedback = "ナイス対応!!🎉"
      content = "次の学生も助けてあげよう!"
      if(quest_i>0){
        reward = "対応＋クエスト" + quest_b + "達成報酬 → " + score_i + "点"
      }else{
        reward = "対応報酬(重要度" + star + ")＋対応時間 → " + score_i + "点"
      }
    }
  
  }else if(button=="again"){

    feedback = "ナイス対応!!🎉"
    content = "また後で対応してあげよう!"
    if(quest_i>0){
      reward = "対応＋クエスト" + quest_b + "達成＋対応時間 → " + score_i + "点"
    }else{
      reward = "対応報酬(重要度" + star + ")＋対応時間 → " + score_i + "点"
    }

  }else{ //button=="start"
    
    content = "困っている学生をどんどん助けよう!!"
    if(quest_i==1){
      feedback = "第2ステージにチャレンジ!!🎉"
      reward = "クエスト" + quest_b + "達成報酬 → " + score_i + "点"
    }else if(quest_i>1 && score_i>=30){
      feedback = "第2ステージにチャレンジ!!🎉"
      reward = "クエスト5達成報酬 → " + score_i + "点"

    }else if(quest_i>i){
      feedback = "第2ステージにチャレンジ!!🎉"
      reward = ""
    }else{
      feedback = "再チャレンジ!!"
      reward = ""
    }

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

//モーダルウィンドウ表示
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

