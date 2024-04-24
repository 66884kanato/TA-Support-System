<?php

  //声掛け済みend.csvに入れる
  $fp_end = fopen($path_end,'a');
  if ($fp_end === false) {
    die('Failed to open end file');
  }
  if(flock($fp_end,LOCK_EX)){ //書き込み専用ロック
    $data_end = array($student_id,$ta_id,$priority,$completion,$again,$skip,$kyosyu,$score,$koekake,$quest,$stage);
    $line_end = implode(',' , $data_end);
    if (fwrite($fp_end, $line_end . "\n") === false) {
      die('Failed to write to end file');
    }
    flock($fp_end,LOCK_UN); //書き込み専用ロックをアンロック
  }else{
    die('Failed to acquire exclusive lock on end file');
  }
  fclose($fp_end);

?>