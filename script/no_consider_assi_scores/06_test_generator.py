# TASS Script Phase 6
# 各々のクラス(C01,C02,...)の各授業回(#02,#03,...)の
# 学習の確認問題の評定ファイルを.csvファイルでダウンロードしたもの
# 2022FP-C00-学習の確認問題_FP22#??-評定.csv
# から，
# out/???????_test.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ test?,2,1 など．
# ?は順に授業回，ただし2回目から実施．その次は，1問目の点数，2問目の点数．
# 点数は2点が満点，1点が部分点，0点が不正解，-は未受験
# 複数回答している場合は，始めに回答した点数を読み込む

import sys
import re
import io
import os
import glob

# Windows環境の対策用
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'test'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
TEST_FILES_NAME = DATA_DIR + '*評定.csv'

if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

test_byID = {}

# 学生名簿ファイルを読み込み
with open(MEIBO_KANJI_FILE, 'r', encoding='utf-8') as meibo_kanji_file_input:
    for line in meibo_kanji_file_input:
        line = line.strip().split(',')
        # 最初の授業回のデータを初期値として設定
        test_byID[line[0]] = '-/-'
        
#print(test_byID)

# 評定ファイルを処理
test_files = glob.glob(TEST_FILES_NAME)
test_files.sort()

for test_file_input_name in test_files:
    if 'activity-report' in test_file_input_name:
        continue
    
    test_file_number = test_file_input_name.split('#')[1][:2]
    
    with open(test_file_input_name, 'r', encoding='utf-8') as test_file:
        test_unit_byID = {}
        for line in test_file:
            if 'IDナンバー' in line or '全平均' in line or '期限切れ' in line or '電通' in line:
                continue
            line = line.replace('.00','').replace('-','0').strip()
            data = line.split(',')
            studentID = data[2]
            scores = data[9] + '/' + data[10]  # Adjust for actual columns
            
			#複数回答の場合は初めの回答を採用する処理
            if studentID not in test_unit_byID:
                test_unit_byID[studentID] = scores
                    

    for id in test_byID.keys():
        if id in test_unit_byID:
            # 最初の授業回のデータに続けて記録
            test_byID[id] += ',' + test_unit_byID[id]
        else:
            test_byID[id] += ',-/-'
    

# 出力ファイルを生成
for id, data in sorted(test_byID.items()):
    with open(os.path.join(OUT_DIR, id + '_' + OUT_FILE_PREFIX + '.csv'), 'w', encoding='utf-8') as outfile:
        scores = data.split(',')
        for idx, score in enumerate(scores, start=1):
            formatted_score = score.replace('/', ',')
            outfile.write(f"{OUT_FILE_PREFIX}{idx},{formatted_score}\n")
