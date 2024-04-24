<?php

    //$csvarray = array(); // $csvarray を空の配列として定義する
    $fp_que = fopen($path_previous,'a+');
    if ($fp_que === false) {
      $error = error_get_last();
      die('Failed to open que file: ' . $error['message']);
    }
    fseek($fp_que, 0);
    flock($fp_que,LOCK_EX); //書き込み専用ロック（同時に書き込みされないようにする)
    $a = 0;
    while($lineque = fgetcsv($fp_que)){
      $csvarray[$a] = $lineque;
      $a = $a + 1;
    }
    flock($fp_que,LOCK_UN);
    fclose($fp_que); 

    for($i=0; $i<count($csvarray); $i++){
      if($student_id==$csvarray[$i][0]){ //挙手学生と一致すれば
        break;
      }
    }
    
    //queの更新(そのqueから学生を削除)
    for($j=0; $j<count($csvarray)-1; $j++){
      if($j<$i){
        $csvarray_new[$j] = $csvarray[$j];
      }else{
        $csvarray_new[$j] = $csvarray[$j+1];
      }
      
    }
    $fp_que_write = fopen($path_previous,'w');
    if ($fp_que_write === false) {
      die('Failed to open que file');
    }
    flock($fp_que_write,LOCK_EX);
    foreach($csvarray_new as $csvdata_new){ //csvarrayの各要素をcsvdata_newにコピーしてそれを使う（編集して）
      $linecsv_new = implode(',' , $csvdata_new);
      fwrite($fp_que_write, $linecsv_new . "\n"); //これによってque.csvは書き換わった
    }
    flock($fp_que_write,LOCK_UN);
    fclose($fp_que_write);

?>