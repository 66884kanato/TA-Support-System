window.addEventListener('DOMContentLoaded',
  function () {
    // Canvas APIが利用できるかを判定（1）
    if (HTMLCanvasElement) {
      // コンテキストオブジェクトを取得（2）
      var cv = document.querySelector('#cv');
      var c = cv.getContext('2d');

      var i;
      var h;

      var rate_word_size = 19;
      var startpointx = 0;
      var startpointy = 40;
      var space = 27;
      var allstudent_attsum = 0;
      var student_attscore = 0;
      var allstudent_kadaisum = 0;
      var student_kadaiscore = 0;
      var allstudent_testsum = 0;
      var allstudent_test2sum = 0;
      var student_testscore = 0;
      var student_test2score = 0;
      var today_test_score = 0;
      var today_test2_score = 0;
      var today_total_testscore = 0;
      //var previous_total_testscore = 0;


      c.font = rate_word_size + "px 'MSPゴシック'";
      c.fillStyle = "black";


      //学籍番号，氏名
      c.font = rate_word_size + "px 'MSPゴシック'";
      c.fillStyle = "black";
      c.fillText(student_id+': '+student_name, startpointx, startpointy);
      startpointy += space;

      //声掛け重要度(この時のlevelは，map_room2.htmlによりすでに重要度に変換されている)
      var star; //⭐️
      var get_k; //声掛け点数
      var get_t = "30点"; //挙手点数(一律)
      var kibo; //希望度
      if(level==1){ //重要度1
        star = '⭐️';
        get_k = "30点";
        kibo = "挙手時のみの対応で大丈夫";
      }else if(level==2){ //重要度2
        star = '⭐️⭐️';
        get_k = "30点";
        kibo = "定期的に声掛けして欲しい";
      }else if(level==3){ //重要度3
        star = '⭐️⭐️⭐️';
        get_k = "30点";
        kibo = "たくさん声掛けして欲しい";
      }else if(level==4){ //重要度4
        star = '⭐️⭐️⭐️⭐️';
        get_k = "40点";
        kibo = "たくさん声掛けして欲しい";
      }else if(level==5){ //重要度5
        star = '⭐️⭐️⭐️⭐️⭐️';
        get_k = "50点";
        kibo = "定期的に声掛けして欲しい";
      }else if(level==6){ //重要度6
        star = '⭐️⭐️⭐️⭐️⭐️⭐️';
        get_k = "60点";
        kibo = "挙手時のみの対応で大丈夫";
      }else if(level==7){ //重要度7
        star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
        get_k = "70点";
        kibo = "たくさん声掛けして欲しい";
      }else if(level==8){ //重要度8
        star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
        get_k = "80点";
        kibo = "定期的に声掛けして欲しい";
      }else{ //重要度9
        star = '⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️';
        get_k = "90点";
        kibo = "挙手時のみの対応で大丈夫";
      }
      c.fillText('声掛け重要度: '+star, startpointx, startpointy);
      startpointy += space;

      //声掛け希望度
      c.font = rate_word_size + "px 'MSPゴシック'";
      c.fillStyle = "black";
      c.fillText("声掛け希望:" + " " + "　" + kibo, startpointx, startpointy);
      startpointy += space;

      c.fillText('声掛け点数: '+get_k+"　"+"　挙手対応点数: "+get_t, startpointx, startpointy);
      startpointy += space;

      
      //出席率生成
      for (i = 0; i < 15; i++) {
        if ((student_att[i] == 0) || (student_att[i] == 1) || (student_att[i] == 2)) {
          allstudent_attsum = i + 1;
          student_attscore += student_att[i];
          if(student_att[i] == 2){
            student_attscore -= 1; 
          }
        }
      }
      c.font = rate_word_size + "px 'MSPゴシック'";
      c.fillStyle = "black";
      c.fillText("出席率: " + " "+ " " + " " + "　" + "　" + "　" + "　" + Math.floor(student_attscore / allstudent_attsum * 100) + "%", startpointx, startpointy);
      startpointy += space;


      //宿題提出率の生成
      for (i = 0; i < 15; i++) {
        if ((student_kadai[i] == 0) || (student_kadai[i] == 1) || (student_kadai[i] == 2)) {
          student_kadaiscore += student_kadai[i];
        }
      }
      allstudent_kadaisum = student_kadai.length - 1;
      c.font = rate_word_size + "px 'ＭＳ Ｐゴシック'";
      c.fillStyle = "black";
      c.fillText("宿題提出率: " + "　" +"　" +"　" + Math.floor(student_kadaiscore / allstudent_kadaisum * 100) + "%", startpointx, startpointy);
      startpointy += space;



      //確認問題正答率の生成
      for (i = 0; i < 15; i++) {
        if ((student_test[i] == 0) || (student_test[i] == 1) || (student_test[i] == 2)) {
          allstudent_testsum = (i + 1) * 2 -2;
          //第1回の分抜いた-2
          student_testscore += student_test[i];
        }
      }
      for (i = 0; i < 15; i++) {
        if ((student_test2[i] == 0) || (student_test2[i] == 1) || (student_test2[i] == 2)) {
          allstudent_test2sum = (i + 1) * 2 -2;
          //第1回の分抜いた-2
          student_test2score += student_test2[i];
        }
      }
      c.font = rate_word_size + "px 'MSPゴシック'";
      c.fillStyle = "black";
      c.fillText("確認問題正答率:" + "　" + " " + Math.floor((student_testscore + student_test2score) / (allstudent_testsum + allstudent_test2sum) * 100) + "%", startpointx, startpointy);
      startpointy += space;


      //今回の確認問題の点数の生成
      if(isNaN(student_test[student_test.length-2])){
        today_test_score = 0;
      }else{
        today_test_score = student_test[student_test.length-2];
      }

      if(isNaN(student_test2[student_test2.length-2])){
        today_test2_score = 0;
      }else{
        today_test2_score = student_test2[student_test2.length-2];
      }

      today_total_testscore = today_test_score + today_test2_score;
      //console.log(today_total_testscore);

      //今回の確認問題
      c.font = rate_word_size + "px 'MSPゴシック'";
      c.fillStyle = "black";
      c.fillText("今回の確認問題: " + "　" + today_total_testscore + "/" + 4, startpointx, startpointy);
      startpointy += space;

      /*
      //前回の確認問題の点数の生成
      if(isNaN(student_test[student_test.length-3])){
        previous_test_score = 0;
      }else{
        previous_test_score = student_test[student_test.length-3];
      }

      if(isNaN(student_test[student_test.length-3])){
        previous_test2_score = 0;
      }else{
        previous_test2_score = student_test2[student_test2.length-3];
      }

      previous_total_testscore = previous_test_score + previous_test2_score;
      //console.log(previous_total_testscore);


      //前回の確認問題
      c.font = rate_word_size + "px 'MSPゴシック'";
      c.fillStyle = "black";
      c.fillText("前回の確認問題: " + "　" + previous_total_testscore + "/" + 4, startpointx, startpointy);
      startpointy += space;
      */

      
    }
  }
);