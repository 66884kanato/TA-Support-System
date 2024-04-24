<?php 

    //今日の結果を自分の過去の結果に入れる
    $my_result = $path_result . "result_c". $classroom . "_" . $ta_id . ".csv";
    $fp_result = fopen($my_result,'a');
    if ($fp_result === false) {
    die('Failed to open result file');
    }
    if(flock($fp_result,LOCK_EX)){ //書き込み専用ロック
    $data_result = array($score_today,$taio_today,$quest_today);
    $line_result = implode(',' , $data_result);
    if (fwrite($fp_result, $line_result . "\n") === false) {
        die('Failed to write to result file');
    }
    flock($fp_result,LOCK_UN); //書き込み専用ロックをアンロック
    }else{
    die('Failed to acquire exclusive lock on result file');
    }
    fclose($fp_result);

?>