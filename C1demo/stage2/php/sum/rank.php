<?php

    //now_resultからランキング作成（よりリアルタイムなランキングを作るため)
    foreach (glob($path_now_result . "/*.csv") as $filePath) {
        $resultEach = null;
        if (($handle = fopen($filePath, "r")) !== false) {
            while (($data = fgetcsv($handle, 1000, ",")) !== false) {
                $resultEach = $data;
            }
            fclose($handle);
        }
        $resultSum[] = $resultEach;
    }

    // 点数が高い順に並び替え
    usort($resultSum, function ($a, $b) {
        $scoreComparison = intval($b[0]) - intval($a[0]);
        if ($scoreComparison != 0) {
            return $scoreComparison;
        }

        $voiceComparison = intval($b[1]) - intval($a[1]);
        if ($voiceComparison != 0) {
            return $voiceComparison;
        }

        return intval($b[2]) - intval($a[2]);
    });

    // rank.csv更新
    $rankPath = "../../../result/rank.csv";
    file_put_contents($rankPath, ""); // ファイルを空にする

    foreach ($resultSum as $row) {
        file_put_contents($rankPath, implode(",", $row) . PHP_EOL, FILE_APPEND);
    }

?>