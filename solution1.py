'''
Brendan Lewis m263708
IC322 Lab1 solution1.py 

'''
array = []
size = 0
with open("numbers.txt", "r") as f: 
    for word in f:
        for num in word.split():
            size += 1
            array.append(num)
array.sort(key=lambda x: float(x))
for i in range(size):
   print(format(float(array[i])))
   i += 1
