import jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read()
excludes={"将军","却说","二人","不可","不能","如此","商议","如何","主公","军士","军马"\
         ,"左右","引兵","次日","大喜","天下","于是","今日","不敢","陛下","一人"\
         ,"都督","人马","不知","只见","众将","上马","大叫","太守","此人","夫人"\
         ,"先主","后人","背后","城中","天子","一面","何不","大军","忽报","先生","百姓"\
         ,"何故","然后","先锋","不如","赶来","原来","令人","下马","喊声","正是","忽然"\
         ,"因此","不见","未知","大败","大事","之后","一军","引军","起兵","军中","接应"\
         ,"进兵","大惊","可以","以为","大怒","不得","心中","下文","一声","追赶","粮草"\
         ,"一齐","分解","回报","分付","只得","出马","三千","大将","随后","报知","前面"\
         ,"之兵","且说","领兵","众官","何人","星夜","精兵","城上","之计","不肯"}
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="诸葛亮"or word=="孔明曰":
        rword="孔明"
    elif word=="关公"or word=="云长":
        rword="关羽"
    elif word=="玄德"or word=="玄德曰":
        rword="刘备"
    elif word=="孟德"or word=="丞相":
        rword="曹操"
    elif word=="后主":
        rword="刘禅"
    elif word=="江东"or word=="东吴":
        rword="东吴"
    elif word=="魏兵"or word=="曹兵":
        rword="魏兵"
    elif word=="许都":
        rword="许昌"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(40):
    word,count=items[i]
    print("{0:<10}{1:>5}次".format(word,count))
