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

  //初めになることはない(クエリパラメータがstartになることはない）
  //クエリパラメータから得点と声掛け人数を取得して
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


  //パス
  include('sum/path.php');

  
  //今日の結果を取り出す
  include('sum/my_today.php');
  

  //今日の結果を自分の過去の結果に入れる
  include('sum/to_result.php');


  //ランキング作成
  include('sum/rank.php');
  
?>

<!DOCTYPE html>



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
      
      window.open(`../../end.html?student_id=end&ta_id=${params2}&level=${params3}&completion=${params4}&again=${params5}&skip=${params6}&kyosyu=${params7}&score=${params8}&koekake=${params9}&quest=${params10}&stage=${params11}`,"_top");
    </script>


  </body>
</html>
