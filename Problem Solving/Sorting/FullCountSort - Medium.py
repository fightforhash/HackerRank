n = int(input())
num_dict = {}
maxNum = 0

for i in range(n):
    x = input().strip().split()
    numX = int(x[0])
    linX = x[1]
    
    if i < n/2:
        linX = "-"
      
    if numX > maxNum:
        maxNum = numX
        
    if numX in num_dict:
        num_dict[numX].append(linX)
    else:
        num_dict[numX] = [linX]
        
    

output = []

for i in range(maxNum + 1):
    if i in num_dict:
        for line in num_dict[i]:
            output.append(line)

print (" ".join(map(str,output)))
