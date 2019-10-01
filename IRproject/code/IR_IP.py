import numpy as np
from collections import Counter
import nltk
import string
import os
import pandas as pd

#替换特殊符号
def remove_symbols(text):
    del_estr = string.punctuation + string.digits
    replace = ' ' * len(del_estr)
    tran_tab = str.maketrans(del_estr,replace)
    text=text.translate(tran_tab)
    return text

# 文件处理函数
def  dealFile(path,num,list):
    if os.path.isfile(path):
        content = open(path, encoding='utf-8').read()
        num[0] += 1

        # 文本预处理
        content = remove_symbols(content)
        content = content.lower()
        content = nltk.word_tokenize(content)
        # 词频统计
        result = Counter(content)
        words = dict(result)
        words['vsm_length']=len(content)
        list.append(words)
        # np.save('wf.npy',wf)
        # for wf1 in wf:
        #     print("%s=%d" % (wf1, wf[wf1]))
        # print(words)
    elif os.path.isdir(path):
        for s in os.listdir(path):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            newDir = os.path.join(path, s)
            dealFile(newDir, num, list)

# 文本读取
path='D:\\安然数据集/maildir/allen-p/_sent_mail'
count=[]
count.append(0)
list=[]
dealFile(path, count, list)
df=sum(map(Counter, list), Counter())
df=dict(df)
vsm=pd.DataFrame(list,columns=df.keys())
vsm.at['vsm_df']=df.values()
print(vsm)
vsm.to_csv('D:\\python输出文件.csv', index=True)

#矩阵转置












