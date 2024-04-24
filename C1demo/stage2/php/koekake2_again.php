<?php
  //エラー表示
  ini_set('display_errors', 1);
  ini_set('display_startup_errors', 1);
  error_reporting(E_ALL);
  //キャッシュクリア
  header( 'Cache-Control: no-store, no-cache, must-revalidate' );
  header( 'Cache-Control: post-check=0, pre-check=0', FALSE );
  header('Pragma:no-cache');

  //URLクエリパラメータを受け取る
  $parameters = $_SERVER['QUERY_STRING']; //$_SERVERはオブジェクト，QUERY_STRINGは要素（属性）みたいな感じ
  $parameters_make = explode("&",$parameters);
  $student_id_make = explode("=",$parameters_make[0]);
  $ta_id_make = explode("=",$parameters_make[1]);
  $priority_make = explode("=",$parameters_make[2]);
  $completion_make = explode("=",$parameters_make[3]);
  $again_make = explode("=",$parameters_make[4]);
  $skip_make = explode("=",$parameters_make[5]);
  
  $student_id = $student_id_make[1];
  $ta_id = $ta_id_make[1];
  $priority = $priority_make[1];
  $completion = $completion_make[1];
  $again = $again_make[1];
  $skip = $skip_make[1];
  
  //再対応なのでagainを1に
  //skip回数を0にリセット
  $again = 1;
  $skip = 0;

  //初めでなければ，クエリパラメータから得点と声掛け人数を取得して
  $kyosyu_make = explode("=",$parameters_make[6]);
  $score_make = explode("=",$parameters_make[7]);
  $koekake_make = explode("=",$parameters_make[8]);
  $quest_make = explode("=",$parameters_make[9]);
  $stage_make = explode("=",$parameters_make[10]);
  $kyosyu = $kyosyu_make[1];
  $score = $score_make[1];
  $koekake = $koekake_make[1];
  $quest = $quest_make[1];
  $stage = $stage_make[1];
  //得点と声掛け人数追加
  if($priority>=4){
    $score += $priority * 10;
  }else{
    $score += 30;
  }
  $koekake += 1;


  //クエスト達成
  if($quest==4){ //クエスト5達成
    $quest += 1;
    $score += 70;
    //まずは1人,自分で学生を選んで声を掛けてみよう!
  }else if($quest==5 && 4<=$priority && $priority<=6){ //クエスト6達成
    $quest += 1;
    $score += 80;
    //黄色の座席の学生に声を掛けてみよう!
  }else if($quest==6 && 7<=$priority && $priority<=9){ //クエスト7達成
    $quest += 1;
    $score += 90;
    //赤色の座席の学生に声を掛けてみよう!
  }else if($quest==7 && $priority==9){ //クエスト8達成
    $quest += 1;
    $score += 100;
    //声掛け最高レベル（⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️)の学生に声を掛けよう!
  }else if($quest==8 && $score>=1000){ //クエスト9達成
    $quest += 1;
    $score += 50;
    //得点を1000点以上にしよう
  }else if($quest==9 && $koekake>=10){ //クエスト10達成
    $quest += 1;
    $score += 100;
    //合計10人の学生の対応をしよう
  }else{}



  //session開始
  session_start();

  // endとして現在のタイムスタンプを取得し、startからの差分（秒）を計算
  if (isset($_SESSION['start'])) {
      $start = $_SESSION['start'];
      $end = time();
      $taio_seconds = $end - $start; // 経過時間を秒で計算

      // 処理（例: 経過時間を何かのスコアに加算するなど）
      $score += $taio_seconds;
  }

  // 特定のセッション変数を削除
  unset($_SESSION['start']);
  // セッションを完全に終了
  session_destroy();
  



  //パス
  include('sum/path.php');


  //対応ログを書き出す
  $file_name = basename(__FILE__, ".php");
  include('sum/log.php');


  //que_allはpriorityではなくlevelで更新しなければならない
  //que_allの2番目はlevelと最初に決めている(priority_que.pyの時)
  //levelで更新しなきゃいけないのでpriorityからlevelに戻している
  if($priority==1){
    $level = 7;
  }else if($priority==2){
    $level = 4;
  }else if($priority==3){
    $level = 1;
  }else if($priority==4){
    $level = 2;
  }else if($priority==5){
    $level = 5;
  }else if($priority==6){
    $level = 8;
  }else if($priority==7){
    $level = 3;
  }else if($priority==8){
    $level = 6;
  }else{
    $level = 9;
  }

  //que_allを更新する(que_allはlevelで)
  include('sum/que_all.php');


  //結果(now_result/now_c09_1.csv)を更新する
  include('sum/result.php');

?>
<!DOCTYPE html>


<!--新しい学生探す-->

<!--student.php呼び込み-->
<html>
  <head>

  </head>
  <body>
  <script>
      let params1 = '<?php echo $student_id ?>'; 
      let params2 = '<?php echo $ta_id ?>'; 
      let params3 = '<?php echo $level ?>'; 
      let params4 = '<?php echo $completion ?>';
      let params5 = '<?php echo $again ?>'; 
      let params6 = '<?php echo $skip ?>'; 
      let params7 = '<?php echo $kyosyu ?>'; 
      let params8 = '<?php echo $score ?>';
      let params9 = '<?php echo $koekake ?>';
      let params10 = '<?php echo $quest ?>';
      let params11 = '<?php echo $stage ?>';

      let taio_seconds = '<?php echo $taio_seconds ?>';
      sessionStorage.setItem('taio_seconds', taio_seconds); //対応時間をセッションストレージに保存
      
      window.open(`../student2_select.html?student_id=$select&ta_id=${params2}&level=${params3}&completion=${params4}&again=${params5}&skip=${params6}&kyosyu=${params7}&score=${params8}&koekake=${params9}&quest=${params10}&stage=${params11}`,"_top");
    </script>


  </body>
</html>
