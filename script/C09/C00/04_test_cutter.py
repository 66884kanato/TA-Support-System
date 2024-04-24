
# TASS Script Phase 4
# 各々のクラス(C01,C02,...)の各授業回(#02,#03,...)の
# 学習の確認問題の評定ファイルを.csvファイルでダウンロードしたもの
# 2022FP-C00-学習の確認問題_FP22#??-評定.csv
# から，
# out/student_test??.csvを生成する (学籍番号，1問目の点数，2問目の点数)

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX_TEST = OUT_DIR + 'student_test'
TEST_FILES_NAME = DATA_DIR + '*評定.csv'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

testByID = {}

test_files = glob.glob(TEST_FILES_NAME)
test_files.sort()
#print(test_files)

for test_file_input_name in test_files:
	if(len(re.findall('activity-report',test_file_input_name)) != 0):
		continue
	test_file_name = open(test_file_input_name, 'r', encoding='utf-8')
	test_file_number = test_file_input_name.split('#')
	test_file_number = test_file_number[1][0:2]
#	print(test_file_number)

	for test_file_line in test_file_name:
		# ここから2行は特定学生を使った検証用
#		if(len(re.findall('2110481',test_file_line)) != 0):
#			print(test_file_line)
		if(len(re.findall('IDナンバー',test_file_line)) != 0):
			continue
		if(len(re.findall('全平均',test_file_line)) != 0):
			continue
		if(len(re.findall('期限切れ',test_file_line)) != 0):
			continue
		test_file_line = test_file_line.replace('.00','')
		test_file_line = test_file_line.replace('-','0')
#		print(test_file_line)

		test_file_data = test_file_line[:-1].split(',')
		if(len(re.findall('電通',test_file_data[0])) != 0):
			continue
		test_studentID = test_file_data[2]
#		print(test_studentID)
		testByID[test_studentID] = test_file_data[11] + ',' + test_file_data[12]
#		print(testByID[test_studentID])

	test_file_name.close()

# テスト書き込み
	test_out_file_name = open(OUT_FILE_PREFIX_TEST+test_file_number+'.csv', 'w', encoding='utf-8')
	for testFinal in sorted(testByID.keys()):
		test_out_file_name.write(testFinal+","+testByID[testFinal])
		test_out_file_name.write("\n")
	test_out_file_name.close()
	testByID.clear()
