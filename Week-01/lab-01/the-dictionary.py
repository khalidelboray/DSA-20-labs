names = ['ali', 'ahmed', 'ibrahim', 'islam', 'fatma', 'fahim', 'fadi']
dic = {}
for name in names:
    let = name[0]
    dic.setdefault(let, []).append(name)
print(dic)