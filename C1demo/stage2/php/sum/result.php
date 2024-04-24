<?php

    $scriptDirectory = __DIR__;
    // "/C" の次の2文字を取得
    $index = strpos($scriptDirectory, '/C');
    if ($index !== false && $index + 2 < strlen($scriptDirectory)) {
        $classroom = substr($scriptDirectory, $index + 2, 2);
    } else {
        echo "Not found or not enough characters after '/C'";
    }
    //結果(now_result/now_c09_1.csv)を更新する
    $taio = $koekake + $kyosyu;
    $my_result = $path_now_result . "now_c" . $classroom . "_" . $ta_id . ".csv";
    $fp_result = fopen($my_result, 'w');
    if($fp_result===false){
        die('Failed to open result file');
    }
    if(flock($fp_result, LOCK_EX)){
        $data_result = array($score, $taio, $quest, $koekake, $kyosyu);
        $line_result = implode(',', $data_result);
        if(fwrite($fp_result, $line_result. "\n")===false){
        dine('Failed to write to result file');
        }
        flock($fp_result, LOCK_UN);
    }else{
        die('Failed to acquire exclusive lock on result file');
    }
    fclose($fp_result);

?>