<?php

    //待ち行列ファイル3に戻す（いないとみなす）
    $fp_que = fopen($path_que3,'a');
    if ($fp_que === false) {
      die('Failed to open que3 file');
    }
    if(flock($fp_que,LOCK_EX)){ //書き込み専用ロック
      $level = 3; //声掛けレベルを上げるて赤色表示できるようにする
      $data_que = array($student_id,$ta_id,$level,$completion,$again,$skip);
      $line_que = implode(',' , $data_que);
      if (fwrite($fp_que, $line_que . "\n") === false) {
        die('Failed to write to que3 file');
      }
      flock($fp_que,LOCK_UN); //書き込み専用ロックをアンロック
    }else{
      die('Failed to acquire exclusive lock on que file');
    }
    fclose($fp_que0);

?>