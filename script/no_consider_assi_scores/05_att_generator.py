
# TASS Script Phase 5
# 出欠管理の各回の記録Webページを.htmlファイルに保存したもの
# ??講義の出欠更新 自動出欠管理.htm (.htmまたは.html，??は授業回，01,02,...)
# から，
# out/???????_att.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ att?,1 (?は順に授業回，1は出席，2は遅刻，0は欠席)

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'att'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
SHUSSEKI_FILES_NAME = DATA_DIR + '??講義の出欠更新 自動出欠管理.htm*'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

shusseki_byID = {}

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	shusseki_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[0]

###


shusseki_files = glob.glob(SHUSSEKI_FILES_NAME)
shusseki_files.sort()
#print(shusseki_files)

for shusseki_file_input_name in shusseki_files:
	shusseki_file_name = open(shusseki_file_input_name, 'r', encoding='utf-8')
	shusseki_file_number = shusseki_file_input_name.split(DATA_DIR)
	shusseki_file_number = shusseki_file_number[1][0:2]

	for shusseki_file_line in shusseki_file_name:
		if(len(re.findall('cell c3',shusseki_file_line)) != 0):
			shusseki_file_line = shusseki_file_line.replace('</td','')
			shusseki_file_data = shusseki_file_line[:-1].split('>')
			shusseki_studentID = shusseki_file_data[1]

		if(len(re.findall('checked',shusseki_file_line)) != 0):
			if(len(re.findall('cell c5',shusseki_file_line)) != 0):
				shusseki_byID[shusseki_studentID] = shusseki_byID[shusseki_studentID] + ',1'
			if(len(re.findall('cell c6',shusseki_file_line)) != 0):
				shusseki_byID[shusseki_studentID] = shusseki_byID[shusseki_studentID] + ',2'
			if(len(re.findall('cell c7',shusseki_file_line)) != 0):
				shusseki_byID[shusseki_studentID] = shusseki_byID[shusseki_studentID] + ',2'
			if(len(re.findall('cell c8',shusseki_file_line)) != 0):
				shusseki_byID[shusseki_studentID] = shusseki_byID[shusseki_studentID] + ',0'
			if(len(re.findall('cell c9',shusseki_file_line)) != 0):
				shusseki_byID[shusseki_studentID] = shusseki_byID[shusseki_studentID] + ',0'

	shusseki_file_name.close()

for shussekiFinal in sorted(shusseki_byID.keys()):
	shusseki_out_file_name = open(OUT_DIR + shussekiFinal + '_' + OUT_FILE_PREFIX + '.csv', 'w', encoding='utf-8')
	shusseki_out_data = shusseki_byID[shussekiFinal].split(',')
	for m in range(1,len(shusseki_out_data)):
		shusseki_out_file_name.write(OUT_FILE_PREFIX + str(m) + ',' + shusseki_out_data[m]+'\n')
	shusseki_out_file_name.close()

