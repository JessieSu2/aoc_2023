file = open("info.txt") 
array= []
for line in file:
    left = 0
    right = (len(line)-1)
    answer = 0
   
    while left <= right:
        if line[left].isdigit() and line[right].isdigit():
            answer = (int(line[left]) * 10)  + int(line[right])
            array.append(answer)
            break
        elif line[left].isdigit() and line[right].isdigit() == False:
            right -=1
        elif line[left].isdigit() == False and line[right].isdigit():
            left +=1
        else:
            right -=1
            left +=1
print(array)

totalSum = 0
for i in range(len(array)):
    totalSum += array[i]
    
print(totalSum)