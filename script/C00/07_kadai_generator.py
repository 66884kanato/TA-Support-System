
# TASS Script Phase 7
# 課題の提出確認画面のWebページを.htmlファイルに保存したもの
# ??課題.htm (.htmまたは.html，??は授業回，01,02,...)
# から，
# out/???????_kadai.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ kadai?,1 など．
# ?は順に授業回，提出状況．
# 課題の点数は考慮しているが，late-submissionは考慮していない．

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'kadai'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
KADAI_FILES_NAME = DATA_DIR + '??課題.htm*'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

kadai_byID = {}
kadai_teishutsu_byID = {}

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	kadai_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[0]
	kadai_teishutsu_byID[meibo_kanji_file_line[0]] = ''

###

kadai_files = glob.glob(KADAI_FILES_NAME)
kadai_files.sort()
#print(kadai_files) # debug

for kadai_file_input_name in kadai_files:
	kadai_file_name = open(kadai_file_input_name, 'r', encoding='utf-8')
	kadai_file_number = kadai_file_input_name.split(DATA_DIR)
	kadai_file_number = kadai_file_number[1][0:2]
#	print(kadai_file_name) # debug

	for kadai_file_line in kadai_file_name:
		if(len(re.findall('評定のために提出済み',kadai_file_line)) != 0):
#			print(kadai_file_line) #debug
			kadai_studentID = kadai_file_line.split('_c3')
			kadai_studentID = kadai_studentID[1].split('td')
			kadai_studentID = kadai_studentID[2].split('">')
			kadai_studentID = kadai_studentID[1].split('@')
			kadai_studentID = kadai_studentID[0][1:]
			#print(kadai_studentID) #debug
			#score = kadai_file_line.split('&nbsp;/&nbsp;')[0]
			#print(kadai_file_line.split('&nbsp;/&nbsp;'))
			
			# "&nbsp;/&nbsp;"で分割して点数を取得
			score_match = re.search(r'(\d+\.\d+)&nbsp;/&nbsp;\d+\.\d+', kadai_file_line)
			#print(score_match)
			if score_match:
				# 抽出した点数から整数部分のみを取得
				score_float = float(score_match.group(1))  # 浮動小数点数に変換
				score_int = int(score_float)  # 整数に変換
				#print(f"抽出した点数（整数）: {score_int}")
				kadai_teishutsu_byID[kadai_studentID] = str(score_int)
			else:
				#print('点数が見つかりませんでした。')
				kadai_teishutsu_byID[kadai_studentID] = '-'

	for kadaiShukei in sorted(kadai_byID.keys()):
		if(kadai_teishutsu_byID[kadaiShukei] != '-' and kadai_teishutsu_byID[kadaiShukei] != ''):
			kadai_byID[kadaiShukei] = kadai_byID[kadaiShukei] + ',' + kadai_teishutsu_byID[kadaiShukei]
			kadai_teishutsu_byID[kadaiShukei] = ''
		else:
			kadai_byID[kadaiShukei] = kadai_byID[kadaiShukei] + ',0'
#		print(kadai_byID[kadaiShukei]) #debug
	kadai_file_name.close()

for kadaiFinal in sorted(kadai_byID.keys()):
	kadai_out_file_name = open(OUT_DIR + kadaiFinal + '_' + OUT_FILE_PREFIX + '.csv', 'w', encoding='utf-8')
	kadai_out_data = kadai_byID[kadaiFinal].split(',')
	for m in range(1,len(kadai_out_data)):
		kadai_out_file_name.write(OUT_FILE_PREFIX + str(m) + ',' + kadai_out_data[m]+'\n')
	kadai_out_file_name.close()


