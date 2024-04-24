var get_point;

function make_quest(){

    //クエスト5
    if(quest==4){
        text_q = "まずは1人,自分で学生を選んで声を掛けてみよう!\n（声掛け例：見回りにきました!or調子どうですか？）"
        get_p = 70;
        return;
    }

    //クエスト6
    if(quest==5){
        text_q = "黄色の座席の学生に声を掛けてみよう!\n（声掛け例：見回りにきました!or調子どうですか？）"
        get_p = 80;
        return;
    }

    //クエスト7
    if(quest==6){
        text_q = "赤色の座席の学生に声を掛けてみよう!\n（声掛け例：お待たせしました!or質問お願いします!）"
        get_p = 90;
        return;
    }

    //クエスト8
    if(quest==7){
        text_q = "最高重要度⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️の学生に声を掛けよう\n（声掛け例：見回りにきました!or調子どうですか？）"
        get_p = 100;
        return;
    }

    //クエスト9
    if(quest==8){
        if(score>=1000){
            var n = parseInt(score) + 50;
            text_q = "得点を"+n+"点以上にしよう\n(高得点のカギは重要度⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️の学生??)"
            get_p = 50;
            return;
        }
        text_q = "得点を1000点以上にしよう\n(高得点のカギは重要度⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️の学生??)"
        get_p = 50;
        return;
    }

    //クエスト10
    if(quest==9){
        if(koekake>=10){
            var n = parseInt(koekake) + 1;
            text_q = "合計"+n+"回学生に声を掛けてみよう\n（声掛け例：見回りにきました!or調子どうですか？）"
            get_p = 100;
            return;
        }
        text_q = "合計10回学生に声を掛けてみよう\n（声掛け例：見回りにきました!or調子どうですか？）"
        get_p = 100;
        return;
    }
    
    //クエスト11以降
    if(quest>=10){
        text_q = "「！」のついてる学生を助けてあげよう\n（声掛け例：さっきの問題は解決した？）"
        get_p = 50;
        return;
    }


}