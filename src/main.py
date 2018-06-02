from read_dict import read_dictionary
from read_dict import enp_hantei
from morphological_analysis import morphological_analysis

# 入力待ち
print('解析文字を入力してください')
text = input()

#形態素解析実行
keitaiso = morphological_analysis(text)
yousos = list()
for youso in keitaiso:
  youso = str(youso)
  print(youso)
  tmp = youso.split('\t')
  yousos.append(tmp[0])
# 感情判定
enp_hantei(yousos)

