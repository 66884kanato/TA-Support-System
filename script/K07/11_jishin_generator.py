
# TASS Script Phase 11
# 各々のクラス(C01,C02,...)の各授業回(#01,#02,...)のactivity-report(Cover)解答
# 2022FP-C00-activity-report_FP22#??(Cover)-解答.csv
# から，
# out/???????_jishin.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ jishin?,1 など．
# ?は順に授業回，自信無の回答．低1-6高．-は未回答．

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'jishin'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
JISHIN_FILES_NAME = DATA_DIR + '*解答.csv'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

jishin_byID = {}
jishin_unit_ByID = {}

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	jishin_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[0]

###

jishin_files = glob.glob(JISHIN_FILES_NAME)
jishin_files.sort()
#print(jishin_files)

for jishin_file_input_name in jishin_files:
	if(len(re.findall('(Cover)',jishin_file_input_name)) == 0):
		continue
	jishin_file_name = open(jishin_file_input_name, 'r', encoding='utf-8')
	jishin_file_number = jishin_file_input_name.split('#')
	jishin_file_number = jishin_file_number[1][0:2]

	for jishin_file_line in jishin_file_name:
		if(len(re.findall('1023456',jishin_file_line)) != 0):
			continue
		if(len(re.findall('所属組織',jishin_file_line)) != 0):
			continue

		jishin_file_line = jishin_file_line.replace('-', '0')
		jishin_file_line = jishin_file_line.replace('1.全く当てはまらない', '1')
		jishin_file_line = jishin_file_line.replace('2.当てはまらない', '2')
		jishin_file_line = jishin_file_line.replace('3.どちらかというと当てはまらない', '3')
		jishin_file_line = jishin_file_line.replace('4.どちらかというと当てはまる', '4')
		jishin_file_line = jishin_file_line.replace('5.当てはまる', '5')
		jishin_file_line = jishin_file_line.replace('6.強く当てはまる', '6')

# 無関係の設問のカット

		jishin_file_line = jishin_file_line.replace(',自宅等学外からのオンライン受講での学習を希望する', '')
		jishin_file_line = jishin_file_line.replace(',学内からのオンライン受講での学習を希望する', '')
		jishin_file_line = jishin_file_line.replace(',演習室での対面授業への参加を希望する', '')
		jishin_file_line = jishin_file_line.replace(',オンデマンドの自習教材での学習を希望する', '')

#		print(jishin_file_line)
		jishin_file_data = jishin_file_line[:-1].split(',')
		if(len(jishin_file_data)>14):
			jishin_unit_ByID[jishin_file_data[2]] = jishin_file_data[15]
		else:
			jishin_unit_ByID[jishin_file_data[2]] = '-'

	jishin_file_name.close()

	for jishin_unitFinal in sorted(jishin_byID.keys()):
		if jishin_unitFinal in jishin_unit_ByID:
			jishin_byID[jishin_unitFinal] = jishin_byID[jishin_unitFinal] + ',' + jishin_unit_ByID[jishin_unitFinal]
			jishin_unit_ByID[jishin_unitFinal] = '-'
		else:
			jishin_byID[jishin_unitFinal] = jishin_byID[jishin_unitFinal] + ',-'

for jishinFinal in sorted(jishin_byID.keys()):
	jishin_out_file_name = open(OUT_DIR + jishinFinal + '_' + OUT_FILE_PREFIX + '.csv', 'w', encoding='utf-8')
	jishin_out_data = jishin_byID[jishinFinal].split(',')
	for m in range(1,len(jishin_out_data)):
		jishin_out_file_name.write(OUT_FILE_PREFIX + str(m) + ',' + jishin_out_data[m]+'\n')
	jishin_out_file_name.close()

