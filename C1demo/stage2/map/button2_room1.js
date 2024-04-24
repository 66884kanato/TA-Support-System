//座席
var keep_seat_x = 595; //一番左上の座席のx座標
var keep_seat_y = 55; //一番左上の座席のy座標
var move_seat_x = keep_seat_x; //描画用
var move_seat_y = keep_seat_y; //描画用
var space = 45; //座席の感覚
var hallway = 75; //通路の幅


//座席ボタン作成
function make_seat_button(){

  //class=seat-containerに入れるよ
  const seatContainer = document.querySelector('.seat-container');

  //ip座席設定
  var start_ip = 101; //第1演習室の初めのip
  var now_ip = start_ip;
  var end_ip = new Array; //座席の右端のip
  end_ip[0] = start_ip + 11;
  for(var i=1; i<7; i++){
    if(i==1){ //前から2列目は
      end_ip[i] = end_ip[i-1] + 10;
    }else{
      end_ip[i] = end_ip[i-1] + 12;
    }
  }
      
  //ボタン描画
  var i = 0; //i列目
  while(now_ip<=end_ip[6]){
    while(now_ip<=end_ip[i]){

      //ボタン作成
      const seatButton = document.createElement('button');
      seatButton.classList.add('seat-button');

      //色とクリック先
      var seat_inf_index = now_ip - start_ip;
      if(seat_inf[seat_inf_index][1]!=0){ //その座席に座っているなら
        
        //色
        if(seat_inf[seat_inf_index][3]<=3){
          seatButton.style.backgroundColor = 'hsl(109, 94%, 50%)'; //🟩
        }else if(seat_inf[seat_inf_index][3]>=7){
          seatButton.style.backgroundColor = "#FF0000"; //🟥
        }else{
          seatButton.style.backgroundColor = "#ffe327"; //🟨
        }

        if(seat_inf[seat_inf_index][6]==2){ //skip=2なら（欠席）
          seatButton.style.backgroundColor = '#eeebeb';
        } 

        if(seat_inf[seat_inf_index][1]!=student_id){ //声掛け学生と一致しないなら
          
          //クリック先
          seatButton.dataset.student_id = seat_inf[seat_inf_index][1];
          seatButton.dataset.ta_id = ta_id;
          seatButton.dataset.level = seat_inf[seat_inf_index][3];; //この時seat_infのlevelを代入してはいけない(レベルではなく重要度に書き換わっているから)
          seatButton.dataset.completion = seat_inf[seat_inf_index][4];
          seatButton.dataset.again = seat_inf[seat_inf_index][5];
          seatButton.dataset.skip = seat_inf[seat_inf_index][6];
          seatButton.dataset.kyosyu = kyosyu;
          seatButton.dataset.score = score;
          seatButton.dataset.koekake = koekake;
          seatButton.dataset.quest = quest;
          seatButton.dataset.stage = stage;
        
          seatButton.addEventListener('click', function(event){

            params1 = event.currentTarget.dataset.student_id;
            params2 = event.currentTarget.dataset.ta_id;
            params3 = event.currentTarget.dataset.level;
            params4 = event.currentTarget.dataset.completion;
            params5 = event.currentTarget.dataset.again;
            params6 = event.currentTarget.dataset.skip;
            params7 = event.currentTarget.dataset.kyosyu;
            params8 = event.currentTarget.dataset.score;
            params9 = event.currentTarget.dataset.koekake;
            params10 = event.currentTarget.dataset.quest;
            params11 = event.currentTarget.dataset.stage;
          
            window.location.href = `../php/taio2.php?student_id=${params1}&ta_id=${params2}&level=${params3}&completion=${params4}&again=${params5}&skip=${params6}&kyosyu=${params7}&score=${params8}&koekake=${params9}&quest=${params10}&stage=${params11}`
          });
        
        }
        
      }else{ //座っていないなら
        seatButton.style.backgroundColor = '#eeebeb';
      }

      //声掛け学生の点滅
      if(seat_inf[seat_inf_index][1]==student_id){ //声掛け学生と一致なら
        seatButton.classList.add('blinking'); // blinkingクラスを追加して点滅させる
      }


      //声掛け枠線の追加
      if(seat_inf[seat_inf_index][4]==1){ //すでに声をかけた学生なら
        seatButton.style.border = "2.5px solid black";
      }

      //要再対応なら
      if(seat_inf[seat_inf_index][5]==1){ //すでに声をかけた学生なら
        seatButton.style.fontSize = '30px';
        seatButton.textContent = '!';
      }else{
        seatButton.textContent = '';
      }

      // 新しい座標をボタンに設定
      seatButton.style.left = `${move_seat_x}px`;
      seatButton.style.top = `${move_seat_y}px`;

      //css指定してボタン描画
      seatContainer.appendChild(seatButton);

      //console.log("(x,y)=("+seatButton.style.left+","+seatButton.style.top+")");

      //通路考慮
      if(i<=1){ //前から1,2列目
        if((now_ip%4) != 0){ //4の倍数じゃなければ通路じゃない
          move_seat_x -= space;
        }else{ //4の倍数は通路
          move_seat_x -= hallway;
        }
      }else{ //前から3列目以降
        if((now_ip%4) != 2){ //now_ip(mod 4)=2じゃなければ通路じゃない
          move_seat_x -= space;
        }else{ //4の倍数は通路
          move_seat_x -= hallway;
        }
      }

      //console.log("(start,end)=("+now_ip+","+end_ip[i]+")");
      now_ip++;

    }

    move_seat_x = keep_seat_x; //x座標は元に戻す
    move_seat_y += space; //y座標は進める
    i++; //i列目更新

  }

}