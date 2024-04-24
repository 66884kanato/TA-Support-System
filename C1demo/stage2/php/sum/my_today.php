<?php

    $scriptDirectory = __DIR__;
    // "/C" の次の2文字を取得
    $index = strpos($scriptDirectory, '/C');
    if ($index !== false && $index + 2 < strlen($scriptDirectory)) {
        $classroom = substr($scriptDirectory, $index + 2, 2);
    } else {
        echo "Not found or not enough characters after '/C'";
    }
    //今日の結果を取り出す
    $my_today = $path_now_result . "now_c" . $classroom . "_" . $ta_id . ".csv";
    $fp_now_result = fopen($my_today,'a+'); //読み書き可能
    flock($fp_now_result,LOCK_EX); //書き込み専用ロック（同時に書き込みされないようにする)
    $csvarray_nr = fgetcsv($fp_now_result);
    flock($fp_now_result,LOCK_UN);
    fclose($fp_now_result); 

    $score_today = $csvarray_nr[0];
    $taio_today = $csvarray_nr[1];
    $quest_today = $csvarray_nr[2];
    $koekake_today = $csvarray_nr[3];
    $kyosyu_today = $csvarray_nr[4];

?>