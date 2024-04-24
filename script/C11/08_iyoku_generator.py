
# TASS Script Phase 8
# 各々のクラス(C01,C02,...)の各授業回(#01,#02,...)のactivity-report(Cover)解答
# 2022FP-C00-activity-report_FP22#??(Cover)-解答.csv
# から，
# out/???????_iyoku.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ iyoku?,1 など．
# ?は順に授業回，意欲回答．1は低い，2は中，3は高い．-は未回答．

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'iyoku'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
IYOKU_FILES_NAME = DATA_DIR + '*解答.csv'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

iyoku_byID = {}
iyoku_unit_ByID = {}

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	iyoku_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[0]

###

iyoku_files = glob.glob(IYOKU_FILES_NAME)
iyoku_files.sort()
#print(shusseki_files)

for iyoku_file_input_name in iyoku_files:
	if(len(re.findall('(Cover)',iyoku_file_input_name)) == 0):
		continue
	iyoku_file_name = open(iyoku_file_input_name, 'r', encoding='utf-8')
	iyoku_file_number = iyoku_file_input_name.split('#')
	iyoku_file_number = iyoku_file_number[1][0:2]

	for iyoku_file_line in iyoku_file_name:
		if(len(re.findall('1023456',iyoku_file_line)) != 0):
			continue
		if(len(re.findall('所属組織',iyoku_file_line)) != 0):
			continue
#		print(logfile_line)
		iyoku_file_data = iyoku_file_line[:-1].split(',')
		iyoku_unit_ByID[iyoku_file_data[2]] = '-'
# 意欲
		if(len(re.findall('この授業の試験範囲の内容に取り組みたい',iyoku_file_line)) != 0):
			iyoku_unit_ByID[iyoku_file_data[2]] = '1'
		if(len(re.findall('余裕があればこの授業の高度な内容に取り組みたい',iyoku_file_line)) != 0):
			iyoku_unit_ByID[iyoku_file_data[2]] = '2'
		if(len(re.findall('この授業に関連する高度な内容に取り組みたい',iyoku_file_line)) != 0):
			iyoku_unit_ByID[iyoku_file_data[2]] = '3'

	iyoku_file_name.close()

	for iyoku_unitFinal in sorted(iyoku_byID.keys()):
		if iyoku_unitFinal in iyoku_unit_ByID:
			iyoku_byID[iyoku_unitFinal] = iyoku_byID[iyoku_unitFinal] + ',' + iyoku_unit_ByID[iyoku_unitFinal]
			iyoku_unit_ByID[iyoku_unitFinal] = '-'
		else:
			iyoku_byID[iyoku_unitFinal] = iyoku_byID[iyoku_unitFinal] + ',-'

for iyokuFinal in sorted(iyoku_byID.keys()):
	iyoku_out_file_name = open(OUT_DIR + iyokuFinal + '_' + OUT_FILE_PREFIX + '.csv', 'w', encoding='utf-8')
	iyoku_out_data = iyoku_byID[iyokuFinal].split(',')
	for m in range(1,len(iyoku_out_data)):
		iyoku_out_file_name.write(OUT_FILE_PREFIX + str(m) + ',' + iyoku_out_data[m]+'\n')
	iyoku_out_file_name.close()

