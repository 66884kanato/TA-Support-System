//座席表描画
window.addEventListener('DOMContentLoaded',
    function () {
        // Canvas APIが利用できるかを判定（1）
        if (HTMLCanvasElement) {

            // コンテキストオブジェクトを取得（2）
            var cv = document.querySelector('#cv');
            var c = cv.getContext('2d');

            //座席情報
            var keep_seat_x = 40; //一番右上の座席のx座標
            var space = 45; //座席の感覚
            //教卓
            var kyoutaku_x = 500; //教卓のx座標
            var kyoutaku_y = 5; //教卓のy座標
            var kyoutaku_width = space + 36; //教卓の横幅
            var kyoutaku_height = keep_seat_x - 10; //教卓の縦幅
            //スクリーン
            var screen_x = 243; //スクリーンのx座標
            var screen_y = kyoutaku_y; //スクリーンのx座標
            var screen_width = space*3 + 36; //スクリーンの横幅
            var screen_height = kyoutaku_height; //スクリーンの縦幅
            //希望ルール
            var rule_x = 70; //希望ルールのx座標
            var rule_y = 19; //希望ルールのy座標
            //座席番号
            var sn_lx = 0;
            var sn_rx = 624;
            var sn_y = 73;
            var seat_space = 45;

            var char_size = 25; //文字サイズ

            //教卓描画
            c.fillStyle = 'white'; //fillRectの背景の色
            c.strokeStyle = 'black'; //fillRectの枠線の色
            c.fillRect(kyoutaku_x, kyoutaku_y, kyoutaku_width, kyoutaku_height); //四角形
            c.strokeRect(kyoutaku_x, kyoutaku_y, kyoutaku_width, kyoutaku_height); //四角形の枠線
            c.font = char_size + "px 'MSPゴシック'";
            c.fillStyle = "black";
            var center_k_x = kyoutaku_x + kyoutaku_width/2 - char_size; 
            var center_k_y = kyoutaku_y + kyoutaku_height/2 + char_size/3;
            c.fillText("教卓", center_k_x, center_k_y);

            //スクリーン描画
            c.fillStyle = 'white'; //fillRectの背景の色
            c.strokeStyle = 'black'; //fillRectの枠線の色
            c.fillRect(screen_x, screen_y, screen_width, screen_height); //四角形
            c.strokeRect(screen_x, screen_y, screen_width, screen_height); //四角形の枠線
            c.font = char_size + "px 'MSPゴシック'";
            c.fillStyle = "black";
            var center_s_x = screen_x + screen_width/2 - char_size*2.4; 
            var center_s_y = screen_y + screen_height/2 + char_size/3;
            c.fillText("スクリーン", center_s_x, center_s_y);

            char_size = 14; //文字サイズ

            //希望
            c.font = char_size + "px 'MSPゴシック'";
            c.fillStyle = "black";
            c.fillText("好成績↔︎低成績", rule_x, rule_y);
            char_size = 19; //四角サイズ
            rule_y += 2;
            c.fillStyle = 'hsl(109, 94%, 50%)'; //fillRectの背景の色
            c.fillRect(rule_x+char_size, rule_y, char_size, char_size); //四角形
            c.fillStyle = "#ffe327"; //fillRectの背景の色
            c.fillRect(rule_x+2*char_size, rule_y, char_size, char_size); //四角形
            c.fillStyle = "#FF0000"; //fillRectの背景の色
            c.fillRect(rule_x+3*char_size, rule_y, char_size, char_size); //四角形

            
            //座席ボタン描画
            make_seat_button();


            //座席番号
            char_size = 13; //文字サイズ
            c.font = char_size + "px 'MSPゴシック'";
            c.fillStyle = "black";
            c.fillText("101", sn_rx, sn_y);
            c.fillText("112", sn_lx, sn_y);
            sn_y += seat_space;
            c.fillText("113", sn_rx, sn_y);
            c.fillText("122", sn_lx+86, sn_y);
            sn_y += seat_space;
            c.fillText("123", sn_rx, sn_y);
            c.fillText("134", sn_lx, sn_y);
            sn_y += seat_space;
            c.fillText("135", sn_rx, sn_y);
            c.fillText("146", sn_lx, sn_y);
            sn_y += seat_space;
            c.fillText("147", sn_rx, sn_y);
            c.fillText("158", sn_lx, sn_y);
            sn_y += seat_space;
            c.fillText("159", sn_rx, sn_y);
            c.fillText("170", sn_lx, sn_y);
            sn_y += seat_space;
            c.fillText("171", sn_rx, sn_y);
            c.fillText("182", sn_lx, sn_y);
            
        }
    }
);