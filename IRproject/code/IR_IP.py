import numpy as np
from collections import Counter
import nltk
import string

#替换特殊符号
def remove_symbols(text):
    del_estr = string.punctuation + string.digits
    replace = ' ' * len(del_estr)
    tran_tab = str.maketrans(del_estr,replace)
    text=text.translate(tran_tab)
    return text

# 文本读取
# path = ''
# content = open(path).read()
content="hello world"

#文本预处理
content=remove_symbols(content)
content=content.lower()
content=nltk.word_tokenize(content)
print(content)

#词频统计
count=Counter(content)
wf=dict(count)
# np.save('wf.npy',wf)
print(wf)










