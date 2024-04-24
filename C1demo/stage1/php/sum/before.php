<?php

    /* 前のURLから情報を得る */
    if (isset($_SERVER['HTTP_REFERER'])) {
        $previousUrl = $_SERVER['HTTP_REFERER'];
    } else {
        echo "リファラ情報は利用できません";
    }

    /* このphpファイルがどのhtmlファイルから呼ばれたかを取得する */
    $parts = explode('/', $previousUrl);
    // 最後の部分を取得(ファイル名.html?クエリパラメータ)
    $lastPart = end($parts);
    // ".html?" より前の部分を取得
    $htmlName = explode('.html?', $lastPart)[0];

?>