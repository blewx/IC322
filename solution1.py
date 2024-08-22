array = []
size = 0
with open("numbers.txt", "r") as f: 
    for word in f:
        for num in word.split():
            size += 1
            array.append(num)

with open("numbers.txt", "r") as f: 
    for word in f:
        for num in word.split():
            i = 0
            while i < size-1:
                if array[i] > array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
                    i -= 1
                    print(array[i] + "is greater than" + array[i+1])
                i += 1
                print("i = " + str(i))
                for k in range(size):
                    print(array[k])
                    k += 1
                print()

print("end")
for i in range(size):
   print(array[i])
   i += 1
