<?php

    //対応ログを書き出す
    $fp = fopen($path_log,'a');
    if ($fp === false) {
    die('Failed to open log file');
    }
    if(flock($fp,LOCK_EX)){ //書き込み専用ロック
    $datelog = date("Y/m/d H:i:s");
    $data = array($datelog,$student_id,$ta_id,$file_name,$priority,$completion,$again,$skip,$kyosyu,$score,$koekake,$quest,$stage);
    $line = implode(',' , $data);
    if (fwrite($fp, $line . "\n") === false) {
        die('Failed to write to log file');
    }
    flock($fp,LOCK_UN); //書き込み専用ロックをアンロック
    }else{
    die('Failed to acquire exclusive lock on log file');
    }
    fclose($fp);

?>