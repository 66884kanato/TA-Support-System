<?php
  //新しい学生を探す
  //que1の先頭を取ってくる
  //ta.csvに入れる（声掛け中）
  //que1の先頭削除
  $fp_que1 = fopen($path_que1,'a+'); //読み書き可能
  flock($fp_que1,LOCK_EX); //書き込み専用ロック（同時に書き込みされないようにする)
  $a = 0;
  while($lineque1 = fgetcsv($fp_que1)){
    $csvarray1[$a] = $lineque1;
    $a = $a + 1;
  }
  flock($fp_que1,LOCK_UN);
  fclose($fp_que1); 
  if(isset($csvarray1[0][0])){ //que1が空じゃない
    //新しい学生
    $new_student_student_id = $csvarray1[0][0];
    $new_student_ta_id = $ta_id;
    $new_student_level = $csvarray1[0][2];
    $new_student_completion = $csvarray1[0][3];
    $new_student_again = $csvarray1[0][4];
    $new_student_skip = $csvarray1[0][5];

    //ta1ならta1.csvに声掛け中学生を入れる
    $fp_que0 = fopen($path_ta,'w'); //wにすればファイルの内容無視して書き込める（空ファイルに書き込むのと同じ）
    if ($fp_que0 === false) {
      die('Failed to open que file');
    }
    if(flock($fp_que0,LOCK_EX)){ //書き込み専用ロック
      $data0_que = array($new_student_student_id,$new_student_ta_id,$new_student_level,$new_student_completion,$new_student_again,$new_student_skip);
      $line0_que = implode(',' , $data0_que);
      if (fwrite($fp_que0, $line0_que . "\n") === false) { //末尾に戻した
        die('Failed to write to que file');
      }
      flock($fp_que0,LOCK_UN); //書き込み専用ロックをアンロック
    }else{
      die('Failed to acquire exclusive lock on log file');
    }
    fclose($fp_que0);

    //que1の先頭から削除
    $fp_que1_write = fopen($path_que1,'w');
    flock($fp_que1_write,LOCK_EX);
    for ($i = 1 ; $i < count($csvarray1); $i++){
      $csvarray1_new[$i-1] = $csvarray1[$i];
    }
    foreach($csvarray1_new as $csvdata1_new){
      $linecsv1_new = implode(',' , $csvdata1_new);
      fwrite($fp_que1_write, $linecsv1_new . "\n");
    }
    flock($fp_que1_write,LOCK_UN);
    fclose($fp_que1_write);

  }else{ //que1が空
    //que2の先頭を取ってくる
    $fp_que2 = fopen($path_que2,'a+'); //読み書き可能
    flock($fp_que2,LOCK_EX); //書き込み専用ロック（同時に書き込みされないようにする)
    $a = 0;
    while($lineque2 = fgetcsv($fp_que2)){
      $csvarray2[$a] = $lineque2;
      $a = $a + 1;
    }
    flock($fp_que2,LOCK_UN);
    fclose($fp_que2); 
    if(isset($csvarray2[0][0])){ //que2が空じゃない
      //新しい学生
      $new_student_student_id = $csvarray2[0][0];
      $new_student_ta_id = $ta_id;
      $new_student_level = $csvarray2[0][2];
      $new_student_completion = $csvarray2[0][3];
      $new_student_again = $csvarray2[0][4];
      $new_student_skip = $csvarray2[0][5];

      //ta1ならta1.csvに声掛け中学生を入れる
      $fp_que0 = fopen($path_ta,'w'); //wにすればファイルの内容無視して書き込める（空ファイルに書き込むのと同じ）
      if ($fp_que0 === false) {
        die('Failed to open que file');
      }
      if(flock($fp_que0,LOCK_EX)){ //書き込み専用ロック
        $data0_que = array($new_student_student_id,$new_student_ta_id,$new_student_level,$new_student_completion,$new_student_again,$new_student_skip);
        $line0_que = implode(',' , $data0_que);
        if (fwrite($fp_que0, $line0_que . "\n") === false) { //末尾に戻した
          die('Failed to write to que file');
        }
        flock($fp_que0,LOCK_UN); //書き込み専用ロックをアンロック
      }else{
        die('Failed to acquire exclusive lock on log file');
      }
      fclose($fp_que0);

      //que2の先頭から削除
      $fp_que2_write = fopen($path_que2,'w');
      flock($fp_que2_write,LOCK_EX);
      for ($i = 1 ; $i < count($csvarray2); $i++){
        $csvarray2_new[$i-1] = $csvarray2[$i];
      }
      foreach($csvarray2_new as $csvdata2_new){
        $linecsv2_new = implode(',' , $csvdata2_new);
        fwrite($fp_que2_write, $linecsv2_new . "\n");
      }
      flock($fp_que2_write,LOCK_UN);
      fclose($fp_que2_write);

    }else{ //que1もque2も空
      //que3の先頭を取ってくる
      $fp_que3 = fopen($path_que3,'a+'); //読み書き可能
      flock($fp_que3,LOCK_EX); //書き込み専用ロック（同時に書き込みされないようにする)
      $a = 0;
      while($lineque3 = fgetcsv($fp_que3)){
        $csvarray3[$a] = $lineque3;
        $a = $a + 1;
      }
      flock($fp_que3,LOCK_UN);
      fclose($fp_que3); 
      if(isset($csvarray3[0][0])){ //que3が空じゃない
        //新しい学生
        $new_student_student_id = $csvarray3[0][0];
        $new_student_ta_id = $ta_id;
        $new_student_level = $csvarray3[0][2];
        $new_student_completion = $csvarray3[0][3];
        $new_student_again = $csvarray3[0][4];
        $new_student_skip = $csvarray3[0][5];

        //ta1ならta1.csvに声掛け中学生を入れる
        $fp_que0 = fopen($path_ta,'w'); //wにすればファイルの内容無視して書き込める（空ファイルに書き込むのと同じ）
        if ($fp_que0 === false) {
          die('Failed to open que file');
        }
        if(flock($fp_que0,LOCK_EX)){ //書き込み専用ロック
          $data0_que = array($new_student_student_id,$new_student_ta_id,$new_student_level,$new_student_completion,$new_student_again,$new_student_skip);
          $line0_que = implode(',' , $data0_que);
          if (fwrite($fp_que0, $line0_que . "\n") === false) { //末尾に戻した
            die('Failed to write to que file');
          }
          flock($fp_que0,LOCK_UN); //書き込み専用ロックをアンロック
        }else{
          die('Failed to acquire exclusive lock on log file');
        }
        fclose($fp_que0);

        //que3の先頭から削除
        $fp_que3_write = fopen($path_que3,'w');
        flock($fp_que3_write,LOCK_EX);
        for ($i = 1 ; $i < count($csvarray3); $i++){
          $csvarray3_new[$i-1] = $csvarray3[$i];
        }
        foreach($csvarray3_new as $csvdata3_new){
          $linecsv3_new = implode(',' , $csvdata3_new);
          fwrite($fp_que3_write, $linecsv3_new . "\n");
        }
        flock($fp_que3_write,LOCK_UN);
        fclose($fp_que3_write);

      }else{
        print('声を掛ける学生がいません');
      }

    }

  }
  
?>