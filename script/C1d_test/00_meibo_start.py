
# TASS Script Phase 1
# 教務課の名簿データ(Shift-JISからUTF-8に変換したもの)
# RSMeiboCsv_utf8.csv
# と，出欠管理の各回の記録Webページを.htmlファイルに保存したもの
# ??講義の出欠更新 自動出欠管理.htm (.htmまたは.html，??は授業回，01,02,...)
# 名簿 _roman_name_meibo.csv を生成するプログラム

import sys
import re
import io
import os
import glob

##################

DATA_DIR = './data/'
ROMAN_OUT_FILE = DATA_DIR + '_roman_name_meibo.csv'
SHUSSEKI_FILES_NAME = DATA_DIR + '??講義の出欠更新 自動出欠管理.htm*'
KYOMU_FILE_NAME = DATA_DIR + 'RSMeiboCsv_utf8.csv'
KANA_TO_ROMAN_KANA = ['ｶﾞ','ｷﾞ','ｸﾞ','ｹﾞ','ｺﾞ','ｻﾞ','ｼﾞ','ｽﾞ','ｾﾞ','ｿﾞ','ﾀﾞ','ﾁﾞ','ﾂﾞ','ﾃﾞ','ﾄﾞ','ﾊﾞ','ﾋﾞ','ﾌﾞ','ﾍﾞ','ﾎﾞ','ﾊﾟ','ﾋﾟ','ﾌﾟ','ﾍﾟ','ﾎﾟ','ｶ','ｷ','ｸ','ｹ','ｺ','ｻ','ｼ','ｽ','ｾ','ｿ','ﾀ','ﾁ','ﾂ','ﾃ','ﾄ','ﾅ','ﾆ','ﾇ','ﾈ','ﾉ','ﾊ','ﾋ','ﾌ','ﾍ','ﾎ','ﾏ','ﾐ','ﾑ','ﾒ','ﾓ','ﾔ','ﾕ','ﾖ','ﾗ','ﾘ','ﾙ','ﾚ','ﾛ','ﾜ','ｦ','ﾝ','ｱ','ｲ','ｳ','ｴ','ｵ']
KANA_TO_ROMAN_ROMAN = ['GA','GI','GU','GE','GO','ZA','JI','ZU','ZE','ZO','DA','DI','DU','DE','DO','BA','BI','BU','BE','BO','PA','PI','PU','PE','PO','KA','KI','KU','KE','KO','SA','SHI','SU','SE','SO','TA','CHI','TSU','TE','TO','NA','NI','NU','NE','NO','HA','HI','FU','HE','HO','MA','MI','MU','ME','MO','YA','YU','YO','RA','RI','RU','RE','RO','WA','WO','N','A','I','U','E','O']

# Windows環境の対策用

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

##################

kyomu_kana_names_byID = {}
shusseki_kanji_names_byID = {}

###

shusseki_files = glob.glob(SHUSSEKI_FILES_NAME)
shusseki_files.sort()
#print(shusseki_files)

for shusseki_file_input_name in shusseki_files:
	shusseki_file_name = open(shusseki_file_input_name, 'r', encoding='utf-8')
	
#	print(shusseki_file_name)

	for shusseki_file_line in shusseki_file_name:
#		print(shusseki_file_line)
		if(len(re.findall('cell c2',shusseki_file_line)) != 0):
			shusseki_file_line = shusseki_file_line.replace('</a></td','')
			shusseki_file_data = shusseki_file_line[:-1].split('>')
			shusseki_studentName = shusseki_file_data[2]
#			print(shusseki_studentName)

		if(len(re.findall('cell c3',shusseki_file_line)) != 0):
			shusseki_file_line = shusseki_file_line.replace('</td','')
			shusseki_file_data = shusseki_file_line[:-1].split('>')
			shusseki_studentID = shusseki_file_data[1]
#			print(shusseki_studentID)

			shusseki_kanji_names_byID[shusseki_studentID] = shusseki_studentName
			kyomu_kana_names_byID[shusseki_studentID] = ''

###

kyomu_file_name = open(KYOMU_FILE_NAME, 'r', encoding='CP932')

for kyomu_file_line in kyomu_file_name:
	if(len(re.findall('[開講所属]',kyomu_file_line)) != 0):
		continue
	if(len(re.findall('基礎プログラミング',kyomu_file_line)) != 0):
		continue
	if(len(kyomu_file_line) == 1):
		continue

#	print(kyomu_file_line)
	kyomu_file_line = kyomu_file_line.replace('"', '')
	kyomu_file_data = kyomu_file_line[:-1].split(',')

	kyomu_studentID = kyomu_file_data[1]
	kyomu_kana_name = kyomu_file_data[3]

	for m in range(0, len(KANA_TO_ROMAN_KANA)):
		kyomu_kana_name = kyomu_kana_name.replace(KANA_TO_ROMAN_KANA[m],KANA_TO_ROMAN_ROMAN[m])
	kyomu_kana_names_byID[kyomu_studentID] = kyomu_kana_name
#	print(kyomu_kana_name)

####

roman_out_file_name = open(ROMAN_OUT_FILE, 'w', encoding='utf-8')

for finalroman in sorted(shusseki_kanji_names_byID.keys()):
	if(kyomu_kana_names_byID[finalroman] != ''):
		roman_out_file_name.write(finalroman+','+shusseki_kanji_names_byID[finalroman]+' ('+kyomu_kana_names_byID[finalroman]+')\n')
	else:
		roman_out_file_name.write(finalroman+','+shusseki_kanji_names_byID[finalroman]+'\n')
roman_out_file_name.close()
