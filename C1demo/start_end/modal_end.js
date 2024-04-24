/* フィードバック内容設定 */
var feedback; //フィードバック
var content; //フィードバック内容
var reward; //報酬説明

feedback = "結果発表"
content = "お疲れ様でした!!"
reward = "次も頑張りましょう!!"


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

