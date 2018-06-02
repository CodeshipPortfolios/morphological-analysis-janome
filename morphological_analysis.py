from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from janome.charfilter import *

print("文字を入力してください")
text = input()
# text = '昨日はアイスを食べてました。とても美味いし、楽しかったです！'

# 文字列に関するフィルタ。文字コード変換ややHTMLタグの排除などできる
char_filter = []
# 実際に形態素解析を行うインスタンス？
t = Tokenizer()
# 取得した要素に対してフィルタをかけるフィルタ
# token_filter = [POSKeepFilter(['形容詞'])]
token_filter =[]
# char_filter,tokenizer,token_filterを合体させる
analize = Analyzer(char_filter,t,token_filter)
# 取得
for token in analize.analyze(text):
  print(token)