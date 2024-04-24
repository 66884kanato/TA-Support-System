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
  $level_make = explode("=",$parameters_make[2]);
  $completion_make = explode("=",$parameters_make[3]);
  $again_make = explode("=",$parameters_make[4]);
  $skip_make = explode("=",$parameters_make[5]);
  
  $student_id = $student_id_make[1];
  $ta_id = $ta_id_make[1];
  $level = $level_make[1];
  $completion = $completion_make[1];
  $again = $again_make[1];
  $skip = $skip_make[1];

  $stage_make =explode("=",$parameters_make[10]);
  $stage = $stage_make[1];

  //初期設定
  if($stage=="start"){
    $kyosyu = 0;
    $score = 0;
    $koekake = 0;
    $quest = 0;
    $stage = 1;
  }else{  //第2ステージから戻ってきた場合は
    $kyosyu_make = explode("=",$parameters_make[6]);
    $score_make = explode("=",$parameters_make[7]);
    $koekake_make = explode("=",$parameters_make[8]);
    $quest_make = explode("=",$parameters_make[9]);
    $kyosyu = $kyosyu_make[1];
    $score = $score_make[1];
    $koekake = $koekake_make[1];
    $quest = $quest_make[1];
    $stage = 1;
  }

  //得点と声掛け人数追加
  if($level<=3){
    $color = 1; //🟩
  }else if($level>=7){
    $color = 3; //🟥
  }else{
    $color = 2; //🟨
  }
  
  //パス
  include('sum/path.php');

  //対応ログを書き出す
  $file_name = basename(__FILE__, ".php");
  include('sum/log.php');
  
  $file_ta = file($path_ta, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
  if ($file_ta === false) {
    die('Failed to read file');
  }

  $fp_que0 = fopen($path_ta,'a+');
  flock($fp_que0,LOCK_EX);
  $que_ta = fgetcsv($fp_que0);
  flock($fp_que0,LOCK_UN);
  fclose($fp_que0);
  
  // ファイルが空または一行目が存在する場合
  if(isset($que_ta[0])){
    
    //ta.csvの先頭を取ってくる
    $new_student_student_id = $que_ta[0];
    $new_student_ta_id = $ta_id;
    $new_student_level = $que_ta[2];
    $new_student_completion = $que_ta[3];
    $new_student_again = $que_ta[4];
    $new_student_skip = $que_ta[5];

  }else{ //ta.csvが空なら

    //結果(now_result/now_c09_1.csv)を更新する
    include('sum/result.php');

    //新しい学生を探す
    include('sum/new_student.php');

  } //ta.csvが空なら


?>

<!DOCTYPE html>


<!--新しい学生探す-->

<!--student.php呼び込み-->
<html>
  <head>

  </head>
  <body>
    <script>
      let params1 = '<?php echo $new_student_student_id ?>'; 
      let params2 = '<?php echo $new_student_ta_id ?>'; 
      let params3 = '<?php echo $new_student_level ?>'; 
      let params4 = '<?php echo $new_student_completion ?>';
      let params5 = '<?php echo $new_student_again ?>'; 
      let params6 = '<?php echo $new_student_skip ?>'; 
      let params7 = '<?php echo $kyosyu ?>'; 
      let params8 = '<?php echo $score ?>';
      let params9 = '<?php echo $koekake ?>';
      let params10 = '<?php echo $quest ?>';
      let params11 = '<?php echo $stage ?>';
      
      window.open(`../student1_koekake.html?student_id=${params1}&ta_id=${params2}&level=${params3}&completion=${params4}&again=${params5}&skip=${params6}&kyosyu=${params7}&score=${params8}&koekake=${params9}&quest=${params10}&stage=${params11}`,"_top");
    </script>


  </body>
</html>
