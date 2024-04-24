<?php
  //エラー表示
  ini_set('display_errors', 1);
  ini_set('display_startup_errors', 1);
  error_reporting(E_ALL);
  //キャッシュクリア
  header("Cache-Control:no-cache,no-store,must-revalidate,max-age=0");
  header("Cache-Control:pre-check=0,post-check=0",false);
  header("Pragma:no-cache");

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

  //session開始
  session_start();
  //現在のタイムスタンプをstartとしてセッションに保存
  $_SESSION['start'] = time();

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

  //パス
  include('sum/path.php');

  //対応ログを書き出す
  $file_name = basename(__FILE__, ".php");
  include('sum/log.php');

  //スキップは0にしておく（再対応はしないでおく）
  $skip = 0;

  //que_allを更新する
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
      let params3 = '<?php echo $priority ?>'; 
      let params4 = '<?php echo $completion ?>';
      let params5 = '<?php echo $again ?>'; 
      let params6 = '<?php echo $skip ?>'; 
      let params7 = '<?php echo $kyosyu ?>'; 
      let params8 = '<?php echo $score ?>';
      let params9 = '<?php echo $koekake ?>';
      let params10 = '<?php echo $quest ?>';
      let params11 = '<?php echo $stage ?>';

      sessionStorage.setItem('taio', "kyosyu"); //対応種類をセッションストレージに保存
      //sessionStorage.setItem('button', "necessary"); //ボタン種類をセッションストレージに保存
    
      window.open(`../student2_taio.html?student_id=${params1}&ta_id=${params2}&level=${params3}&completion=${params4}&again=${params5}&skip=${params6}&kyosyu=${params7}&score=${params8}&koekake=${params9}&quest=${params10}&stage=${params11}`,"_top");
    </script>

  </body>
</html>
