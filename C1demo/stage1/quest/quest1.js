var get_point;

function make_quest(){

    //クエスト1
    if(quest==0){
        text_q = "点滅してる座席の学生に声を掛けてみよう！\n（声掛け例：見回りにきました!or調子どうですか？）"
        get_p = 10;
        return;
    }

    //クエスト2
    if(quest==1){
        text_q = "挙手した学生がいれば対応してあげよう\n（声掛け例：お待たせしました!or質問お願いします!）"
        get_p = 10;
        return;
    }

    //クエスト3
    if(quest==2){
        if(koekake>=3){
            var n = parseInt(koekake) + 1;
            text_q = "合計"+n+"回学生に声を掛けてみよう\n（声掛け例：見回りにきました!or調子どうですか？）"
            get_p = 30;
            return;
        }
        text_q = "合計3回学生に声を掛けてみよう\n（声掛け例：見回りにきました!or調子どうですか？）"
        get_p = 30;
        return;
    }

    //クエスト4
    if(quest>=3){
    text_q = "慣れてきたら第2ステージに進もう\n（第2ステージでは，獲得点数=⭐️の数×10点以上!!）"
    get_p = 30;
    return;
    }

}