<?php

    //que_allを更新する
    $fp_que_all = fopen($path_all,'r+');
    if($fp_que_all === false){
    die('Failed to open que_all file');
    }
    if(flock($fp_que_all,LOCK_EX)){
    $data_que_all = array($student_id,$ta_id,$level,$completion,$again,$skip);
    $line_que_all = implode(',' , $data_que_all);
    // ファイルの内容を読み込んで更新
    $updatedFileContent = '';
    while (($line = fgets($fp_que_all)) !== false) {
        // 行をカンマで分割して配列にする
        $rowData = explode(',', $line);
        // $student_idが一致する行を見つけたらデータを更新
        if (trim($rowData[0]) == $student_id) {
        $line = $line_que_all . "\n"; // 新しいデータに置き換える
        }
        $updatedFileContent .= $line;
    }
    // ファイルポインタをファイルの先頭に戻し、ファイルを切り詰める
    ftruncate($fp_que_all, 0);
    rewind($fp_que_all);
    if(fwrite($fp_que_all, $updatedFileContent . "\n") === false){
        die('Failed to write to que_all file');
    }
    flock($fp_que_all,LOCK_UN);
    }else{
    die('Failed to acquire exclusive lock on que_all file');
    }
    fclose($fp_que_all);

?>