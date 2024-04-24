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
  
  //挙手対応は一律10点
  $score += 10;
  //挙手対応更新
  $kyosyu = $kyosyu + 1;
  if($level<=3){
    $color = 1; //🟩
  }else if($level>=7){
    $color = 3; //🟥
  }else{
    $color = 2; //🟨
  }


  //パス
  include('sum/path.php');

  /*
  //再対応に挙手で対応したならそのqueから消しておく
  include('sum/again_ok.php');
  */


  if($quest==1){ //クエスト2達成
    $quest += 1;
    $score += 10;
    //挙手した学生がいれば対応してあげよう
  }



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
  

  //対応ログを書き出す
  $file_name = basename(__FILE__, ".php");
  include('sum/log.php');


  //声掛け済みend.csvに入れる
  include('sum/end.php');

  
  //end.csvにagain=1だったことを入れたいからこうしている（ログ系ならagain=1でも問題ない）
  $again = 0; //完了なので0に
  $skip = 0; //skip回数を0にリセット
    

  //que_allを更新する
  include('sum/que_all.php');


  //結果(now_result/now_c09_1.csv)を更新する
  include('sum/result.php');
  

  //新しい学生を探す
  //挙手対応前に表示されていた学生に声を掛けることになるはず
  //そのためqueを更新する必要はない
  //ta.csvを取ってくる
  $fp_que0 = fopen($path_ta,'a+');
  flock($fp_que0,LOCK_EX);
  $que_ta = fgetcsv($fp_que0);
  flock($fp_que0,LOCK_UN);
  fclose($fp_que0);
  $new_student_student_id = $que_ta[0];
  $new_student_ta_id = $ta_id;
  $new_student_level = $que_ta[2];
  $new_student_completion = $que_ta[3];
  $new_student_again = $que_ta[4];
  $new_student_skip = $que_ta[5];
  
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

      let taio_seconds = '<?php echo $taio_seconds ?>';
      sessionStorage.setItem('taio_seconds', taio_seconds); //対応時間をセッションストレージに保存
      
      window.open(`../student1_koekake.html?student_id=${params1}&ta_id=${params2}&level=${params3}&completion=${params4}&again=${params5}&skip=${params6}&kyosyu=${params7}&score=${params8}&koekake=${params9}&quest=${params10}&stage=${params11}`,"_top");
    </script>

  </body>
</html>
