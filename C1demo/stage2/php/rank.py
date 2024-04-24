# -*- coding: utf-8 -*-
import os
import sys
import csv
dir_path = "../../../now_result/"

result_sum = []
#dir_path内探索，current_dirは現在のディレクトリ，sub_dirsはサブディレクトリ，failes_listはファイルリスト
for filename in os.listdir(dir_path):
    file_path = os.path.join(dir_path, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        result_each = None
        for each in reader:
            result_each = each
    result_sum.append(result_each)

#点数が高い順に並び替え
result_sum = sorted(result_sum, reverse=True, key=lambda x: (int(x[0]), int(x[1]), int(x[2]))) #点数が同じ場合は声掛け数でソート（クエストも同じ）

#rank.csv更新
rank_path = "../../../result/rank.csv"
with open(rank_path, 'w', newline='') as empty_file:
    writer = csv.writer(empty_file)
    writer.writerows([])  # 空の行を書き込むことでファイルを空にする

with open(rank_path, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(result_sum)