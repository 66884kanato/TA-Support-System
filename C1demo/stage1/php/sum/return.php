<?php

    //元の待ち行列ファイルに戻す
    $fp_que = fopen($path_previous,'a');
    if ($fp_que === false) {
        die('Failed to open que file');
    }
    if(flock($fp_que,LOCK_EX)){ //書き込み専用ロック
        $data_que = array($student_id,$ta_id,$level,$completion,$again,$skip);
        $line_que = implode(',' , $data_que);
        if (fwrite($fp_que, $line_que . "\n") === false) { //末尾に戻した
            die('Failed to write to que file');
        }
        flock($fp_que,LOCK_UN); //書き込み専用ロックをアンロック
    }else{
        die('Failed to acquire exclusive lock on log file');
    }
    fclose($fp_que);

?>