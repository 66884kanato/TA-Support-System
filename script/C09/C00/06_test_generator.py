
# TASS Script Phase 6
# 各々のクラス(C01,C02,...)の各授業回(#02,#03,...)の
# 学習の確認問題の評定ファイルを.csvファイルでダウンロードしたもの
# 2022FP-C00-学習の確認問題_FP22#??-評定.csv
# から，
# out/???????_test.csvを生成する．ファイル名の???????は学籍番号．
# ファイルの中身は一行ずつ test?,2,1 など．
# ?は順に授業回，ただし2回目から実施．その次は，1問目の点数，2問目の点数．
# 点数は2点が満点，1点が部分点，0点が不正解，-は未受験

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
OUT_DIR = './out/'
OUT_FILE_PREFIX = 'test'
MEIBO_KANJI_FILE = DATA_DIR + '_roman_name_meibo.csv'
TEST_FILES_NAME = DATA_DIR + '*評定.csv'

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if(os.path.exists(OUT_DIR) == False):
	os.mkdir(OUT_DIR)

##################

test_byID = {}
test_unit_byID = {}
past_test_file_number = 0
comma = ''

meibo_kanji_file_input = open(MEIBO_KANJI_FILE, 'r', encoding='utf-8')

for meibo_kanji_file_line in meibo_kanji_file_input:
	meibo_kanji_file_line = meibo_kanji_file_line[:-1].split(',')
	test_byID[meibo_kanji_file_line[0]] = meibo_kanji_file_line[0]

###

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
#	print(past_test_file_number)
	comma = ','
	if(int(test_file_number) - int(past_test_file_number) > 1):
		for m in range(1,int(test_file_number) - int(past_test_file_number)):
			comma = comma + ','
	past_test_file_number = test_file_number

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

		test_file_data = test_file_line[:-1].split(',')
		if(len(re.findall('電通',test_file_data[0])) != 0):
			continue
		test_studentID = test_file_data[2]
#		print(test_studentID)
		test_unit_byID[test_studentID] = test_file_data[11] + '/' + test_file_data[12]

	test_file_name.close()

	for test_unitFinal in sorted(test_byID.keys()):
		if test_unitFinal in test_unit_byID:
			test_byID[test_unitFinal] = test_byID[test_unitFinal] + comma + test_unit_byID[test_unitFinal]
			test_unit_byID[test_unitFinal] = '-/-'
		else:
			test_byID[test_unitFinal] = test_byID[test_unitFinal] + comma + '-/-'

for testFinal in sorted(test_byID.keys()):
	test_out_file_name = open(OUT_DIR + testFinal + '_' + OUT_FILE_PREFIX + '.csv', 'w', encoding='utf-8')
	test_out_data = test_byID[testFinal].split(',')
#	print(test_out_data)
	for m in range(1,len(test_out_data)):
		test_out_data[m] = test_out_data[m].replace('/',',')
		test_out_file_name.write(OUT_FILE_PREFIX + str(m) + ',' + test_out_data[m]+'\n')
	test_out_file_name.close()

