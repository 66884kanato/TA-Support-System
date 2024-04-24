
# TASS Script Phase 2
# Phase 1で作成した名簿
# _roman_name_meibo.csv
# と，出欠管理の各回の記録Webページを.htmlファイルに保存したもの
# ??講義の出欠更新 自動出欠管理.htm (.htmまたは.html，??は授業回，01,02,...)
# から，毎回の授業回ごとの，IPアドレスと学籍番号のテーブル
# out/ip??.csv (??は授業回，ip01.csv,ip02.csv,...)
# を生成する．書式は各行が，IPアドレス,学籍番号,氏名　で構成される

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = OUT_DIR + 'ip'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
SHUSSEKI_FILES_NAME = DATA_DIR + '??講義の出欠更新 自動出欠管理.htm*'
IP_PC_ROOM1_MIN = 20
IP_PC_ROOM1_MAX = 102
IP_PC_ROOM2_MIN = 111
IP_PC_ROOM2_MAX = 192
IP_PC_ROOM_PREFIX = '172.21.16.'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

shusseki_names_byIP = {}
meibo_kanji_names_byID = {}
student_in_pc_room1 = 0
student_in_pc_room2 = 0

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	meibo_kanji_names_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[1]

###

shusseki_files = glob.glob(SHUSSEKI_FILES_NAME)
shusseki_files.sort()
#print(shusseki_files)

for shusseki_file_input_name in shusseki_files:
	shusseki_file_name = open(shusseki_file_input_name, 'r', encoding='utf-8')
	shusseki_file_number = shusseki_file_input_name.split(DATA_DIR)
	shusseki_out_file_name = open(OUT_FILE_PREFIX+shusseki_file_number[1][0:2]+'.csv', 'w', encoding='utf-8')

	# IPアドレスと氏名のテーブルの初期化
	for m in range(IP_PC_ROOM1_MIN, IP_PC_ROOM2_MAX + 1):
		shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)] = ''

	for shusseki_file_line in shusseki_file_name:
		if(len(re.findall('cell c3',shusseki_file_line)) != 0):
			shusseki_file_line = shusseki_file_line.replace('</td','')
			shusseki_file_data = shusseki_file_line[:-1].split('>')
			shusseki_studentID = shusseki_file_data[1]

		if(len(re.findall('cell c12',shusseki_file_line)) != 0):
			shusseki_file_line = shusseki_file_line.replace('</td','')
			shusseki_file_data = shusseki_file_line[:-1].split('>')
			if(shusseki_file_data[1] != '−'):
				shusseki_studentIP = shusseki_file_data[1]
				shusseki_names_byIP[shusseki_studentIP] = shusseki_studentID
#				print(shusseki_names_byIP)
				# 演習室外は除外
				if(len(re.findall(IP_PC_ROOM_PREFIX,shusseki_studentIP)) == 0):
					continue
				shusseki_studentIP4 = shusseki_studentIP.split('.')
				if(int(shusseki_studentIP4[3]) <= IP_PC_ROOM1_MAX):
					student_in_pc_room1 = student_in_pc_room1 + 1
				else:
					student_in_pc_room2 = student_in_pc_room2 + 1

	shusseki_file_name.close()

	if(student_in_pc_room1 > student_in_pc_room2):
		for m in range(IP_PC_ROOM1_MIN, IP_PC_ROOM1_MAX + 1):
			shusseki_out_file_name.write(IP_PC_ROOM_PREFIX+str(m)+','+shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)])
#			print(IP_PC_ROOM_PREFIX+str(m)+','+shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)],end='')
			if(shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)] != ''):
				shusseki_out_file_name.write(','+meibo_kanji_names_byID[shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)]])
#				print(','+meibo_kanji_names_byID[shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)]])
			else:
				shusseki_out_file_name.write('0,0')
#				print('0,0')
			shusseki_out_file_name.write('\n')
	else:
		for m in range(IP_PC_ROOM2_MIN, IP_PC_ROOM2_MAX + 1):
			shusseki_out_file_name.write(IP_PC_ROOM_PREFIX+str(m)+','+shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)])
#			print(IP_PC_ROOM_PREFIX+str(m)+','+shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)],end='')
			if(shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)] != ''):
				shusseki_out_file_name.write(','+meibo_kanji_names_byID[shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)]])
#				print(','+meibo_kanji_names_byID[shusseki_names_byIP[IP_PC_ROOM_PREFIX+str(m)]])
			else:
				shusseki_out_file_name.write('0,0')
#				print('0,0')
			shusseki_out_file_name.write('\n')

	shusseki_out_file_name.close()
