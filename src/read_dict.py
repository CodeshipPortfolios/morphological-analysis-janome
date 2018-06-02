#辞書ファイルを読み込むテスト
def read_dictionary():
  # 単語による判定
  file = open("../dict/dict1.txt","r")
  read_data = {}
  for line in file:
    read_line = line.split('\t')
    read_data[read_line[0]] = read_line[1]
  file.close()
  return read_data

def enp_hantei(yousos):
  dictionary = read_dictionary()
  texts = yousos
  print('-----------感情解析-----------')
  kanjou = 0
  count = 0
  for text in texts:
    if text in dictionary:
      print(text+'\t'+dictionary[text])
      if dictionary[text] == 'p':
        kanjou += 1
        count += 1
      elif dictionary[text] == 'n':
        kanjou -= 1
        count += 1
    else: 
      print(text+'\t'+'none')
  if kanjou == 0:
      print('------------------------\n感情数値:'+str(0))
  else:
    suuchi = kanjou/count
    print('------------------------\n感情数値:'+str(suuchi))