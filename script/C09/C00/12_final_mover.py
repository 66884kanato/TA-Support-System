
import sys
import re
import io
import os
import glob
import shutil

##################

OUT_DIR = './out/'
FINAL_DIR = './final/'
ZASEKI_FILES_NAME = OUT_DIR + 'ip??.csv'
ZASEKI_FINAL_NAME = FINAL_DIR + 'ip.csv'
IYOKU_LISTS_NAME = OUT_DIR + 'student_iyoku??.csv'
IYOKU_FINAL_NAME = FINAL_DIR + 'student_iyoku.csv'
TA_LISTS_NAME = OUT_DIR + 'student_ta??.csv'
TA_FINAL_NAME = FINAL_DIR + 'student_ta.csv'
TEST_LISTS_NAME = OUT_DIR + 'student_test??.csv'
TEST_FINAL_NAME = FINAL_DIR + 'student_test.csv'
KODOKU_LISTS_NAME = OUT_DIR + 'student_kodoku??.csv'
KODOKU_FINAL_NAME = FINAL_DIR + 'student_kodoku.csv'
JISHIN_LISTS_NAME = OUT_DIR + 'student_jishin??.csv'
JISHIN_FINAL_NAME = FINAL_DIR + 'student_jishin.csv'
ATTEND_FILES_NAME = OUT_DIR + '*att.csv'
IYOKU_FILES_NAME = OUT_DIR + '*iyoku.csv'
KADAI_FILES_NAME = OUT_DIR + '*kadai.csv'
TA_FILES_NAME = OUT_DIR + '*ta.csv'
TEST_FILES_NAME = OUT_DIR + '*test.csv'
KODOKU_FILES_NAME = OUT_DIR + '*kodoku.csv'
JISHIN_FILES_NAME = OUT_DIR + '*jishin.csv'

iyokuByID = {}
TAByID = {}
testByID = {}
kodokuByID = {}
jishinByID = {}

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

##################
# 座席表(最新)のコピー

zaseki_files = glob.glob(ZASEKI_FILES_NAME)
zaseki_files.sort()
#print(zaseki_files)

if(os.path.exists(FINAL_DIR) == False):
	os.mkdir(FINAL_DIR)

zaseki_move_file = zaseki_files[-1]
shutil.copy2(zaseki_move_file,ZASEKI_FINAL_NAME)

#####################
# 意欲(最終回答)の集計とコピー

iyoku_files = glob.glob(IYOKU_LISTS_NAME)
iyoku_files.sort()
#print(iyoku_files)

for iyoku_file_input_name in iyoku_files:
	iyoku_file_name = open(iyoku_file_input_name, 'r', encoding='utf-8')
	for iyoku_file_line in iyoku_file_name:
		iyoku_file_data = iyoku_file_line[:-1].split(',')
		iyokuByID[iyoku_file_data[0]] = iyoku_file_line[:-1]
	iyoku_file_name.close()

iyoku_out_file_name = open(IYOKU_FINAL_NAME, 'w', encoding='utf-8')
for iyokuFinal in sorted(iyokuByID.keys()):
	iyoku_out_file_name.write(iyokuByID[iyokuFinal])
	iyoku_out_file_name.write("\n")
iyoku_out_file_name.close()

#####################
# TA(最終回答)の集計とコピー

TA_files = glob.glob(TA_LISTS_NAME)
TA_files.sort()
#print(TA_files)

for TA_file_input_name in TA_files:
	TA_file_name = open(TA_file_input_name, 'r', encoding='utf-8')
	for TA_file_line in TA_file_name:
		TA_file_data = TA_file_line[:-1].split(',')
		TAByID[TA_file_data[0]] = TA_file_line[:-1]
	TA_file_name.close()

TA_out_file_name = open(TA_FINAL_NAME, 'w', encoding='utf-8')
for TAFinal in sorted(TAByID.keys()):
	TA_out_file_name.write(TAByID[TAFinal])
	TA_out_file_name.write("\n")
TA_out_file_name.close()

#####################
# 確認問題(最終回答)の集計とコピー

test_files = glob.glob(TEST_LISTS_NAME)
test_files.sort()
#print(test_files)

for test_file_input_name in test_files:
	test_file_name = open(test_file_input_name, 'r', encoding='utf-8')
	for test_file_line in test_file_name:
		test_file_datest = test_file_line[:-1].split(',')
		testByID[test_file_datest[0]] = test_file_line[:-1]
	test_file_name.close()

test_out_file_name = open(TEST_FINAL_NAME, 'w', encoding='utf-8')
for testFinal in sorted(testByID.keys()):
	test_out_file_name.write(testByID[testFinal])
	test_out_file_name.write("\n")
test_out_file_name.close()

#####################
# 孤独(最終回答)の集計とコピー

kodoku_files = glob.glob(KODOKU_LISTS_NAME)
kodoku_files.sort()
#print(kodoku_files)

for kodoku_file_input_name in kodoku_files:
	kodoku_file_name = open(kodoku_file_input_name, 'r', encoding='utf-8')
	for kodoku_file_line in kodoku_file_name:
		kodoku_file_dakodoku = kodoku_file_line[:-1].split(',')
		kodokuByID[kodoku_file_dakodoku[0]] = kodoku_file_line[:-1]
	kodoku_file_name.close()

kodoku_out_file_name = open(KODOKU_FINAL_NAME, 'w', encoding='utf-8')
for kodokuFinal in sorted(kodokuByID.keys()):
	kodoku_out_file_name.write(kodokuByID[kodokuFinal])
	kodoku_out_file_name.write("\n")
kodoku_out_file_name.close()

#####################
# 自信無し(最終回答)の集計とコピー

jishin_files = glob.glob(JISHIN_LISTS_NAME)
jishin_files.sort()
#print(jishin_files)

for jishin_file_input_name in jishin_files:
	jishin_file_name = open(jishin_file_input_name, 'r', encoding='utf-8')
	for jishin_file_line in jishin_file_name:
		jishin_file_dajishin = jishin_file_line[:-1].split(',')
		jishinByID[jishin_file_dajishin[0]] = jishin_file_line[:-1]
	jishin_file_name.close()

jishin_out_file_name = open(JISHIN_FINAL_NAME, 'w', encoding='utf-8')
for jishinFinal in sorted(jishinByID.keys()):
	jishin_out_file_name.write(jishinByID[jishinFinal])
	jishin_out_file_name.write("\n")
jishin_out_file_name.close()

#####################
# 個別の出席ファイルのコピー

attend_files = glob.glob(ATTEND_FILES_NAME)
attend_files.sort()
#print(attend_files)

for m in range(0,len(attend_files)):
#	print(attend_files[m])
	attend_file_name = attend_files[m].split('/')
	new_file_name = attend_file_name[2]
	attend_file_name2 = attend_file_name[2].split('_')
	student_ID = attend_file_name2[0]
#	print(student_ID)
#	print(new_file_name)

	if(os.path.exists(FINAL_DIR + student_ID) == False):
		os.mkdir(FINAL_DIR + student_ID)

	shutil.copy2(attend_files[m],FINAL_DIR + student_ID + '/' + new_file_name)

#####################
# 個別の意欲ファイルのコピー

iyoku_files = glob.glob(IYOKU_FILES_NAME)
iyoku_files.sort()
#print(iyoku_files)

for m in range(0,len(iyoku_files)):
#	print(iyoku_files[m])
	iyoku_file_name = iyoku_files[m].split('/')
	new_file_name = iyoku_file_name[2]
	iyoku_file_name2 = iyoku_file_name[2].split('_')
	student_ID = iyoku_file_name2[0]
#	print(student_ID)
#	print(new_file_name)

	if(os.path.exists(FINAL_DIR + student_ID) == False):
		os.mkdir(FINAL_DIR + student_ID)

	shutil.copy2(iyoku_files[m],FINAL_DIR + student_ID + '/' + new_file_name)

#####################
# 個別の課題ファイルのコピー

kadai_files = glob.glob(KADAI_FILES_NAME)
kadai_files.sort()
#print(kadai_files)

for m in range(0,len(kadai_files)):
#	print(kadai_files[m])
	kadai_file_name = kadai_files[m].split('/')
	new_file_name = kadai_file_name[2]
	kadai_file_name2 = kadai_file_name[2].split('_')
	student_ID = kadai_file_name2[0]
#	print(student_ID)
#	print(new_file_name)

	if(os.path.exists(FINAL_DIR + student_ID) == False):
		os.mkdir(FINAL_DIR + student_ID)

	shutil.copy2(kadai_files[m],FINAL_DIR + student_ID + '/' + new_file_name)

#####################
# 個別のTA希望ファイルのコピー

ta_files = glob.glob(TA_FILES_NAME)
ta_files.sort()
#print(ta_files)

for m in range(0,len(ta_files)):
#	print(ta_files[m])
	ta_file_name = ta_files[m].split('/')
	new_file_name = ta_file_name[2]
	ta_file_name2 = ta_file_name[2].split('_')
	student_ID = ta_file_name2[0]
#	print(student_ID)
#	print(new_file_name)

	if(os.path.exists(FINAL_DIR + student_ID) == False):
		os.mkdir(FINAL_DIR + student_ID)

	shutil.copy2(ta_files[m],FINAL_DIR + student_ID + '/' + new_file_name)

#####################
# 個別のテストファイルのコピー

test_files = glob.glob(TEST_FILES_NAME)
test_files.sort()
#print(test_files)

for m in range(0,len(test_files)):
#	print(test_files[m])
	test_file_name = test_files[m].split('/')
	new_file_name = test_file_name[2]
	test_file_name2 = test_file_name[2].split('_')
	student_ID = test_file_name2[0]
#	print(student_ID)
#	print(new_file_name)

	if(os.path.exists(FINAL_DIR + student_ID) == False):
		os.mkdir(FINAL_DIR + student_ID)

	shutil.copy2(test_files[m],FINAL_DIR + student_ID + '/' + new_file_name)

#####################
# 個別の孤独ファイルのコピー

kodoku_files = glob.glob(KODOKU_FILES_NAME)
kodoku_files.sort()
#print(kodoku_files)

for m in range(0,len(kodoku_files)):
#	print(kodoku_files[m])
	kodoku_file_name = kodoku_files[m].split('/')
	new_file_name = kodoku_file_name[2]
	kodoku_file_name2 = kodoku_file_name[2].split('_')
	student_ID = kodoku_file_name2[0]
#	print(student_ID)
#	print(new_file_name)

	if(os.path.exists(FINAL_DIR + student_ID) == False):
		os.mkdir(FINAL_DIR + student_ID)

	shutil.copy2(kodoku_files[m],FINAL_DIR + student_ID + '/' + new_file_name)

#####################
# 個別の自信ファイルのコピー

jishin_files = glob.glob(JISHIN_FILES_NAME)
jishin_files.sort()
#print(jishin_files)

for m in range(0,len(jishin_files)):
#	print(jishin_files[m])
	jishin_file_name = jishin_files[m].split('/')
	new_file_name = jishin_file_name[2]
	jishin_file_name2 = jishin_file_name[2].split('_')
	student_ID = jishin_file_name2[0]
#	print(student_ID)
#	print(new_file_name)

	if(os.path.exists(FINAL_DIR + student_ID) == False):
		os.mkdir(FINAL_DIR + student_ID)

	shutil.copy2(jishin_files[m],FINAL_DIR + student_ID + '/' + new_file_name)
