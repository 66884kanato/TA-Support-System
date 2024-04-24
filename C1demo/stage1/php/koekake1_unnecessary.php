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

  //色
  if($level<=3){
    $color = 1; //🟩
  }else if($level>=7){
    $color = 3; //🟥
  }else{
    $color = 2; //🟨
  }
  
  $score += 10; //見に行って問題無しなら，声掛けしてなくても10点を与える

  //パス
  include('sum/path.php');

  //対応ログを書き出す
  $file_name = basename(__FILE__, ".php");
  include('sum/log.php');

  //skip回数を0にリセット
  //スキップは0にしておく（再対応はしないでおく）
  $skip = 0;

  //que_allを更新する
  include('sum/que_all.php');

  //結果(now_result/now_c09_1.csv)を更新する
  include('sum/result.php');

  //自由はあり得ない
  include('sum/new_student.php');

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
