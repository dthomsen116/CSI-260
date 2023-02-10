def numArray():
    n = int(input("input an integer" + '\n'))
    
    array = [[abs(i-j) for i in range(n)] for j in range(n)] 
    for row in array:
        print(*row)

numArray()