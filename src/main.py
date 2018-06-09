from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from janome.charfilter import *


def kaiseki(text):
  #形態素解析実行
  keitaiso = morphological_analysis(text)
  yousos = list()
  for youso in keitaiso:
    youso = str(youso)
    print(youso)
    tmp1 = youso.split('\t')
    tmp2 = tmp1[1].split(',')
    yousos.append(tmp2[6])
  # 感情判定
  # print(enp_hantei(yousos))
  return enp_hantei(yousos)


def read_dictionary():
  # 単語による判定
  file = open("dict/dict1.txt","r")
  read_data = {}
  for line in file:
    read_line = line.split('\t')
    read_data[read_line[0]] = read_line[1]
  file.close()
  return read_data


def enp_hantei(yousos):
  dictionary = read_dictionary()
  texts = yousos
  kaiseki_out='-----------感情解析-----------'
  print('-----------感情解析-----------')
  kanjou = 0
  count = 0
  for text in texts:
    if text in dictionary:
      print(text+'\t'+dictionary[text])
      kaiseki_out+=text+'\t'+dictionary[text]+'\n'
      if dictionary[text] == 'p':
        kanjou += 1
        count += 1
      elif dictionary[text] == 'n':
        kanjou -= 1
        count += 1
    else: 
      print(text+'\t'+'none')
      kaiseki_out+=text+'\t'+'none'+'\n'
  if kanjou == 0:
    r = {"kanjou":str(0),'kaisekibun':kaiseki_out}
  else:
    suuchi = kanjou/count
    r = {"kanjou":str(suuchi),'kaisekibun':kaiseki_out}
  return(r)

def morphological_analysis(text):
  # 文字列に関するフィルタ。文字コード変換ややHTMLタグの排除などできる
  char_filter = []
  # 実際に形態素解析を行うインスタンス？
  t = Tokenizer()
  # 取得した要素に対してフィルタをかけるフィルタ
  token_filter = [POSKeepFilter(['形容詞','名詞','動詞'])]
  # token_filter =[]
  # char_filter,tokenizer,token_filterを合体させる
  analize = Analyzer(char_filter,t,token_filter)
  # 取得
  # for token in analize.analyze(text):
  #   print(token)
  return analize.analyze(text)

