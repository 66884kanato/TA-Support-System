
# TASS Script Phase 9
# 各々のクラス(C01,C02,...)の各授業回(#01,#02,...)のactivity-report(Cover)解答
# 2022FP-C00-activity-report_FP22#??(Cover)-解答.csv
# から，
# out/???????_ta.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ ta?,1 など．
# ?は順に授業回，TAへの希望回答．1は必要な時だけ，2は時々，3はTAから．
# -は未回答．

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'ta'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
TA_FILES_NAME = DATA_DIR + '*解答.csv'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

ta_byID = {}
ta_unit_ByID = {}

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	ta_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[0]

###

ta_files = glob.glob(TA_FILES_NAME)
ta_files.sort()
#print(shusseki_files)

for ta_file_input_name in ta_files:
	if(len(re.findall('(Cover)',ta_file_input_name)) == 0):
		continue
	ta_file_name = open(ta_file_input_name, 'r', encoding='utf-8')
	ta_file_number = ta_file_input_name.split('#')
	ta_file_number = ta_file_number[1][0:2]

	for ta_file_line in ta_file_name:
		if(len(re.findall('1023456',ta_file_line)) != 0):
			continue
		if(len(re.findall('所属組織',ta_file_line)) != 0):
			continue

		ta_file_line = ta_file_line.replace('-', '0')
		ta_file_line = ta_file_line.replace('教員やTAには、質問がある時のみ教えて欲しい', '1')
		ta_file_line = ta_file_line.replace('教員やTAには、定期的に学習の進捗を確認して欲しい', '2')
		ta_file_line = ta_file_line.replace('教員やTAには、内容がわかるまで十分に教えて欲しい', '3')

#		print(logfile_line)
		ta_file_data = ta_file_line[:-1].split(',')
		ta_unit_ByID[ta_file_data[2]] = ta_file_data[13]

	ta_file_name.close()

	for ta_unitFinal in sorted(ta_byID.keys()):
		if ta_unitFinal in ta_unit_ByID:
			ta_byID[ta_unitFinal] = ta_byID[ta_unitFinal] + ',' + ta_unit_ByID[ta_unitFinal]
			ta_unit_ByID[ta_unitFinal] = '-'
		else:
			ta_byID[ta_unitFinal] = ta_byID[ta_unitFinal] + ',-'

for taFinal in sorted(ta_byID.keys()):
	ta_out_file_name = open(OUT_DIR + taFinal + '_' + OUT_FILE_PREFIX + '.csv', 'w', encoding='utf-8')
	ta_out_data = ta_byID[taFinal].split(',')
	for m in range(1,len(ta_out_data)):
		ta_out_file_name.write(OUT_FILE_PREFIX + str(m) + ',' + ta_out_data[m]+'\n')
	ta_out_file_name.close()

