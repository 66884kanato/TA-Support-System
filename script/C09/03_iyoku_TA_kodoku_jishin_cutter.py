
# TASS Script Phase 2
# 各々のクラス(C01,C02,...)の各授業回(#01,#02,...)のactivity-report(Cover)解答
# 2022FP-C00-activity-report_FP22#??(Cover)-解答.csv
# から，
# 1. out/student_iyoku??.csvを生成する (学籍番号，意欲高さ(低1-3高))
# 2. out/student_TA??.csvを生成する (学籍番号，TA必要性(低1-3高))
# 3. out/student_kodoku??.csvを生成する (学籍番号，孤独感(低1-6高))
# 4. out/student_jishin??.csvを生成する (学籍番号，自信無い(低1-6高))

import sys
import re
import os
import io
import glob

####################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX_IYOKU = OUT_DIR + 'student_iyoku'
OUT_FILE_PREFIX_TA = OUT_DIR + 'student_ta'
OUT_FILE_PREFIX_KODOKU = OUT_DIR + 'student_kodoku'
OUT_FILE_PREFIX_JISHIN = OUT_DIR + 'student_jishin'
INPUT_FILES_NAME = DATA_DIR + '*解答.csv'

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
iyokuByID = {}
taByID = {}
kodokuByID = {}
jishinByID = {}

cover_files = glob.glob(INPUT_FILES_NAME)
cover_files.sort()

for cover_file_input_name in cover_files:
#	print(cover_file_input_name) # debug
	cover_file_name = open(cover_file_input_name, 'r', encoding='utf-8')
	cover_file_number = cover_file_input_name.split('#')

	for cover_file_line in cover_file_name:
		if(len(re.findall('1023456',cover_file_line)) != 0):
			continue
		if(len(re.findall('所属組織',cover_file_line)) != 0):
			continue
		if(len(re.findall('IDナンバー',cover_file_line)) != 0):
			continue

#		print(cover_file_line) # debug
		cover_file_data = cover_file_line[:-1].split(',')
		studentID = cover_file_data[2]
		iyokuByID[studentID] = '-'
		taByID[studentID] = '-'
		kodokuByID[studentID] = '-'
		jishinByID[studentID] = '-'
# 意欲
		if(len(re.findall('この授業の試験範囲の内容に取り組みたい',cover_file_line)) != 0):
			iyokuByID[studentID] = '1'
		if(len(re.findall('余裕があればこの授業の高度な内容に取り組みたい',cover_file_line)) != 0):
			iyokuByID[studentID] = '2'
		if(len(re.findall('この授業に関連する高度な内容に取り組みたい',cover_file_line)) != 0):
			iyokuByID[studentID] = '3'
# TAへの希望
		if(len(re.findall('教員やTAには、質問がある時のみ教えて欲しい',cover_file_line)) != 0):
			taByID[studentID] = '1'
		if(len(re.findall('教員やTAには、定期的に学習の進捗を確認して欲しい',cover_file_line)) != 0):
			taByID[studentID] = '2'
		if(len(re.findall('教員やTAには、内容がわかるまで十分に教えて欲しい',cover_file_line)) != 0):
			taByID[studentID] = '3'

# 孤独，自信
#
#		print(cover_file_data)
		kodokuByID[studentID] = '-'
		jishinByID[studentID] = '-'
		if(len(cover_file_data)>13):
			if(len(re.findall('1.全く当てはまらない',cover_file_data[12])) != 0):
				kodokuByID[studentID] = '1'
			if(len(re.findall('2.当てはまらない',cover_file_data[12])) != 0):
				kodokuByID[studentID] = '2'
			if(len(re.findall('3.どちらかというと当てはまらない',cover_file_data[12])) != 0):
				kodokuByID[studentID] = '3'
			if(len(re.findall('4.どちらかというと当てはまる',cover_file_data[12])) != 0):
				kodokuByID[studentID] = '4'
			if(len(re.findall('5.当てはまる',cover_file_data[12])) != 0):
				kodokuByID[studentID] = '5'
			if(len(re.findall('6.強く当てはまる',cover_file_data[12])) != 0):
				kodokuByID[studentID] = '6'

			if(len(re.findall('1.全く当てはまらない',cover_file_data[13])) != 0):
				jishinByID[studentID] = '1'
			if(len(re.findall('2.当てはまらない',cover_file_data[13])) != 0):
				jishinByID[studentID] = '2'
			if(len(re.findall('3.どちらかというと当てはまらない',cover_file_data[13])) != 0):
				jishinByID[studentID] = '3'
			if(len(re.findall('4.どちらかというと当てはまる',cover_file_data[13])) != 0):
				jishinByID[studentID] = '4'
			if(len(re.findall('5.当てはまる',cover_file_data[13])) != 0):
				jishinByID[studentID] = '5'
			if(len(re.findall('6.強く当てはまる',cover_file_data[13])) != 0):
				jishinByID[studentID] = '6'
#		print(kodokuByID[studentID])

	cover_file_name.close()

# 意欲書き込み
	iyoku_out_file_name = open(OUT_FILE_PREFIX_IYOKU+cover_file_number[1][0:2]+'.csv', 'w', encoding='utf-8')
	for iyokuFinal in sorted(iyokuByID.keys()):
		iyoku_out_file_name.write(iyokuFinal+","+iyokuByID[iyokuFinal])
		iyoku_out_file_name.write("\n")
	iyoku_out_file_name.close()
	iyokuByID.clear()

# TA希望書き込み
	ta_out_file_name = open(OUT_FILE_PREFIX_TA+cover_file_number[1][0:2]+'.csv', 'w', encoding='utf-8')
	for taFinal in sorted(taByID.keys()):
		ta_out_file_name.write(taFinal+","+taByID[taFinal])
		ta_out_file_name.write("\n")
	ta_out_file_name.close()
	taByID.clear()

# 孤独書き込み
	kodoku_out_file_name = open(OUT_FILE_PREFIX_KODOKU+cover_file_number[1][0:2]+'.csv', 'w', encoding='utf-8')
	for kodokuFinal in sorted(kodokuByID.keys()):
#		print(kodokuFinal+","+kodokuByID[kodokuFinal])
		kodoku_out_file_name.write(kodokuFinal+","+kodokuByID[kodokuFinal])
		kodoku_out_file_name.write("\n")
	kodoku_out_file_name.close()
	kodokuByID.clear()

# 自信書き込み
	jishin_out_file_name = open(OUT_FILE_PREFIX_JISHIN+cover_file_number[1][0:2]+'.csv', 'w', encoding='utf-8')
	for jishinFinal in sorted(jishinByID.keys()):
		jishin_out_file_name.write(jishinFinal+","+jishinByID[jishinFinal])
		jishin_out_file_name.write("\n")
	jishin_out_file_name.close()
	jishinByID.clear()
