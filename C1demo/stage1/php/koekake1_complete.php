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
  
  //呼び出された回数更新
  //skip回数を0にリセット
  $completion = 1; //声掛け済み
  
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
  if($level<=3){
    $score += 30;
    $color = 1; //🟩
  }else if($level>=7){
    $score += 50;
    $color = 3; //🟥
  }else{
    $score += 40;
    $color = 2; //🟨
  }
  $koekake += 1;

  //クエスト達成
  if($quest==0 && $koekake>=1){ //クエスト1達成
    $quest += 1;
    $score += 10;
    //点滅してる座席の学生に声を掛けてみよう！
  }else if($quest==2 && $koekake>=3){ //クエスト3達成
    $quest += 1;
    $score += 30;
    //合計3人の学生に声を掛けてみよう
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
  
  //声掛け済みend.csvに入れる
  include('sum/end.php');

  //end.csvにagain=1またはskip=1だったら，そのことを入れたいからこうしている（ログ系ならagain=1でも問題ない）
  //end,logは完全にログのため，que_allはリアルタイムで使うから気をつける
  $again = 0; //完了なので0に
  $skip = 0;

  
  //que_allを更新する
  include('sum/que_all.php');
  

  //結果(now_result/now_c09_1.csv)を更新する
  include('sum/result.php');


  /* このphpファイルがどのhtmlファイルから呼ばれたかを取得する */
  include('sum/before.php');

  
  if($htmlName=="button1_koekake_c"){ //システムに従った声掛け

    //新しい学生を探す
    include('sum/new_student.php');

  }else{ //自由な声掛け

    //声掛けした学生をキューから削除して新しい学生を探す
    include('sum/free_student.php');

  }


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
