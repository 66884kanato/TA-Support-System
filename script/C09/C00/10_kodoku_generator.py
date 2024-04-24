
# TASS Script Phase 10
# 各々のクラス(C01,C02,...)の各授業回(#01,#02,...)のactivity-report(Cover)解答
# 2022FP-C00-activity-report_FP22#??(Cover)-解答.csv
# から，
# out/???????_kodoku.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ kodoku?,1 など．
# ?は順に授業回，孤独感の回答．低1-6高．-は未回答．

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'kodoku'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
KODOKU_FILES_NAME = DATA_DIR + '*解答.csv'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

kodoku_byID = {}
kodoku_unit_ByID = {}

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	kodoku_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[0]

###

kodoku_files = glob.glob(KODOKU_FILES_NAME)
kodoku_files.sort()
#print(kodoku_files)

for kodoku_file_input_name in kodoku_files:
	if(len(re.findall('(Cover)',kodoku_file_input_name)) == 0):
		continue
	kodoku_file_name = open(kodoku_file_input_name, 'r', encoding='utf-8')
	kodoku_file_number = kodoku_file_input_name.split('#')
	kodoku_file_number = kodoku_file_number[1][0:2]

	for kodoku_file_line in kodoku_file_name:
		if(len(re.findall('1023456',kodoku_file_line)) != 0):
			continue
		if(len(re.findall('所属組織',kodoku_file_line)) != 0):
			continue

		kodoku_file_line = kodoku_file_line.replace('-', '0')
		kodoku_file_line = kodoku_file_line.replace('1.全く当てはまらない', '1')
		kodoku_file_line = kodoku_file_line.replace('2.当てはまらない', '2')
		kodoku_file_line = kodoku_file_line.replace('3.どちらかというと当てはまらない', '3')
		kodoku_file_line = kodoku_file_line.replace('4.どちらかというと当てはまる', '4')
		kodoku_file_line = kodoku_file_line.replace('5.当てはまる', '5')
		kodoku_file_line = kodoku_file_line.replace('6.強く当てはまる', '6')

# 無関係の設問のカット

		kodoku_file_line = kodoku_file_line.replace(',自宅等学外からのオンライン受講での学習を希望する', '')
		kodoku_file_line = kodoku_file_line.replace(',学内からのオンライン受講での学習を希望する', '')
		kodoku_file_line = kodoku_file_line.replace(',演習室での対面授業への参加を希望する', '')
		kodoku_file_line = kodoku_file_line.replace(',オンデマンドの自習教材での学習を希望する', '')

#		print(kodoku_file_line)
		kodoku_file_data = kodoku_file_line[:-1].split(',')
		if(len(kodoku_file_data)>14):
			kodoku_unit_ByID[kodoku_file_data[2]] = kodoku_file_data[14]
		else:
			kodoku_unit_ByID[kodoku_file_data[2]] = '-'

	kodoku_file_name.close()

	for kodoku_unitFinal in sorted(kodoku_byID.keys()):
		if kodoku_unitFinal in kodoku_unit_ByID:
			kodoku_byID[kodoku_unitFinal] = kodoku_byID[kodoku_unitFinal] + ',' + kodoku_unit_ByID[kodoku_unitFinal]
			kodoku_unit_ByID[kodoku_unitFinal] = '-'
		else:
			kodoku_byID[kodoku_unitFinal] = kodoku_byID[kodoku_unitFinal] + ',-'

for kodokuFinal in sorted(kodoku_byID.keys()):
	kodoku_out_file_name = open(OUT_DIR + kodokuFinal + '_' + OUT_FILE_PREFIX + '.csv', 'w', encoding='utf-8')
	kodoku_out_data = kodoku_byID[kodokuFinal].split(',')
	for m in range(1,len(kodoku_out_data)):
		kodoku_out_file_name.write(OUT_FILE_PREFIX + str(m) + ',' + kodoku_out_data[m]+'\n')
	kodoku_out_file_name.close()

