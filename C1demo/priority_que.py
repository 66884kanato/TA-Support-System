	# -*- coding: utf-8 -*-
import os
import sys
import csv
dir_path = "./student" 

test_data = []
test_student_id = []
test_result = []
ta_data=[]
ta_student_id=[]
ta_result=[]

que1_first=[]
que2_first=[]
que3_first=[]
que1 = []
que2 = []
que3 = []
que1_final =[]
que1_make = []
que2_final =[]
que2_make = []
que3_final =[]
que3_make = []


a=0
b=0
c=0
d=0
e=0
f=0


#dir_path内探索，current_dirは現在のディレクトリ，sub_dirsはサブディレクトリ，failes_listはファイルリスト
for current_dir, sub_dirs, files_list in os.walk(dir_path): #walkで探索
  for file_name in files_list: 
    
    if file_name[-9:] == "_test.csv": #ファイル名が"_test.csvで終わるファイルを探す
      with open(os.path.join(current_dir,file_name)) as f:
        reader = csv.reader(f)
        test_length = 0
        for test in reader:
          test_data.append(test)
          test_length = test_length + 1
        test_data.append((file_name.replace('_test.csv', ''))) #'_test.csv'を取りのぞくので最後は学籍番号になる

    if file_name[-7:] == '_ta.csv': #ファイル名が"_ta.csvで終わるファイルを探す
      with open(os.path.join(current_dir,file_name)) as g:
        reader = csv.reader(g)
        ta_length=0
        for ta in reader:
          ta_data.append(ta)
          ta_length=ta_length+1
        ta_data.append((file_name.replace('_ta.csv', '')))


const_test = '0'
#test_resultに順番にその学生の確認問題の点数を入れる
for j in range(int(len(test_data)/(test_length+1))):
  b=j*(test_length+1)-2
  #'-'を0点にする
  if test_data[b][1] == "-":
    test_data[b][1] = test_data[b][1].replace('-',const_test)
  if test_data[b][2]:
    if test_data[b][2] == "-":
      test_data[b][2] = test_data[b][2].replace('-',const_test)

  test_result.append(float(test_data[b][1])+float(test_data[b][2])) #最新授業の確認問題の点数が順番に入っている

#test_student_idに順番に学籍番号を入れる
for i in range(int(len(test_data)/(test_length+1))): #1学生1ループ
  a = i*(test_length+1)-1
  test_student_id.append(test_data[a]) #test_resultとtest_student_idは対応している




const_ta = '1'
#ta_resultに順番にその学生の希望度を入れる
for l in range(int(len(ta_data)/(ta_length+1))):
  d = l*(ta_length+1)-2 #dによって最新の授業にアクセスする
  if ta_data[d][1] == "-":
    if d==0 or ta_data[d-1][1]=='-':
      ta_data[d][1] = ta_data[d][1].replace('-',const_ta) #前回の希望度引き継ぎできなかったら3を入れる
    else:
      ta_data[d][1] = ta_data[d][1].replace('-',str(ta_data[d-1][1])) #前回の希望度引き継ぎ
    
  ta_result.append(float(ta_data[d][1])) #最新授業のta希望度が順番に入っている

#ta_student_idに順番に学籍番号を入れる
for k in range(int(len(ta_data)/(ta_length+1))):
  c = k*(ta_length+1)-1
  ta_student_id.append(ta_data[c]) #ta_resultとta_student_idは対応している


#こいつらは同じ
#print(len(test_student_id))
#print(len(ta_student_id))
#print(len(ta_result))
#print(len(test_result))

i = 0
for i in range(len(ta_student_id)):

  if ta_result[i]==3: #希望度高，声掛けレベル123

    if test_result[i]==4.0 or test_result[i]==3.0: #声掛けレベル1
      que1_first.append([ta_student_id[i], 1, ta_result[i], test_result[i]])
    elif test_result[i]==2.0: #声掛けレベル2
      que1_first.append([ta_student_id[i], 2, ta_result[i], test_result[i]])
    else: #声掛けレベル3
      que1_first.append([ta_student_id[i], 3, ta_result[i], test_result[i]])

  elif ta_result[i]==2: #希望度中，声掛けレベル456

    if test_result[i]==4.0 or test_result[i]==3.0: #声掛けレベル4
      que2_first.append([ta_student_id[i], 4, ta_result[i], test_result[i]])
    elif test_result[i]==2.0: #声掛けレベル5
      que2_first.append([ta_student_id[i], 5, ta_result[i], test_result[i]])
    else: #声掛けレベル6
      que2_first.append([ta_student_id[i], 6, ta_result[i], test_result[i]])

  else: #希望度低，声掛けレベル789
    
    if test_result[i]==4.0 or test_result[i]==3.0: #声掛けレベル7
      que3_first.append([ta_student_id[i], 7, ta_result[i], test_result[i]])
    elif test_result[i]==2.0: #声掛けレベル8
      que3_first.append([ta_student_id[i], 8, ta_result[i], test_result[i]])
    else: #声掛けレベル9
      que3_first.append([ta_student_id[i], 9, ta_result[i], test_result[i]])

que1_first = sorted(que1_first, key=lambda x: x[1]) #2番目(レベル)でソート
que2_first = sorted(que2_first, key=lambda x: x[1])
que3_first = sorted(que3_first, key=lambda x: x[1]) 

#print(que1_first)


#ip.csv(student_ip)と比べることによって欠席している人を外す
student_id = []
ipPath = './student/ip.csv'
#ip.csvを開く(withを使えばファイルのopen,closeを気にする必要がない)
with open(ipPath) as f:

    reader = csv.reader(f) #fにはファィルのパスが入る

    #一行ごとに入れてく
    for ip in reader:

        #それぞれのアドレスに座っている学生の学籍番号
        student_id.append(str(ip[1]))

#print(student_id)

for l in range(len(que1_first)):
  for m in range(len(student_id)):
    if que1_first[l][0] == student_id[m]:
      que1.append(que1_first[l])

for n in range(len(que2_first)):
  for o in range(len(student_id)):
    if que2_first[n][0] == student_id[o]:
      que2.append(que2_first[n])

for p in range(len(que3_first)):
  for q in range(len(student_id)):
    if que3_first[p][0] == student_id[q]:
      que3.append(que3_first[p])

#print(que1)


que_all = [] #全部まとめたやつ
  
for i in range(len(que1)):
  
  que1_make.append(que1[i][0]) #student_id
  que1_make.append(0) #ta_id
  que1_make.append(que1[i][1]) #level
  que1_make.append(0) #completion
  que1_make.append(0) #again
  que1_make.append(0) #skip
  que1_final.append(que1_make)
  que_all.append(que1_make)
  del que1_make
  que1_make = []

for j in range(len(que2)):
  que2_make.append(que2[j][0]) #student_id
  que2_make.append(0) #ta_id
  que2_make.append(que2[j][1]) #level
  que2_make.append(0) #completion
  que2_make.append(0) #again
  que2_make.append(0) #skip
  que2_final.append(que2_make)
  que_all.append(que2_make)
  del que2_make
  que2_make = []
  
for k in range(len(que3)):
  que3_make.append(que3[k][0]) #student_id
  que3_make.append(0) #ta_id
  que3_make.append(que3[k][1]) #level
  que3_make.append(0) #completion
  que3_make.append(0) #again
  que3_make.append(0) #skip
  que3_final.append(que3_make)
  que_all.append(que3_make)
  del que3_make
  que3_make = []

#print(que_all)


with open('./que/que1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que1_final)

with open('./que/que2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que2_final)

with open('./que/que3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que3_final)

with open('./que/que_all.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que_all)


#ta1.csvを空にする
que_empty = []
with open('./que/ta1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que_empty)

#ta2.csvを空にする
que_empty = []
with open('./que/ta2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que_empty)

#end1.csvを空にする
que_empty = []
with open('./que/end1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que_empty)

#end2.csvを空にする
que_empty = []
with open('./que/end2.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(que_empty)