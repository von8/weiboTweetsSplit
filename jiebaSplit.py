#-*-coding: utf-8 -*-
import re
import jieba

f=open('cleandata.txt')
ChineseWords = list()
try:
    while True:
        line=f.readline()
        if len(line)==0:
            break
        if line.count('\n')==len(line):
            continue
        seg_list = jieba.cut(line, cut_all=False)
        for x in seg_list:
            if x=='\n':
                continue
            ChineseWords.append(x)
    print(", ".join(ChineseWords))
finally:
    f.close()
