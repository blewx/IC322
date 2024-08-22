
'''
Brendan Lewis 263708
IC322 Lab1 solution2.py
'''
words = {}
size = 0
with open("words.txt", "r") as f: 
    for word in f:
        for X in word.split():
            x = X.lower()
            if x in words:
                words[x] += 1
            else:
                words[x] = 1

temp = dict(sorted(words.items(), key=lambda words: words[1],reverse=True))

to_fix = list(temp.items())[:5]

for i in range(5):
    to_print = str(to_fix[i]).replace('(','').replace(')','').replace('\'','').replace(',',':')
    i +=1
    print(to_print)            

