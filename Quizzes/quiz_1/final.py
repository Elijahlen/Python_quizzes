L = [2, 7, 7, 2, 6, 5, 6, 1, 1, 1]
n = len(L)
Z = []
for x in range(n-2,-1,-1):
    for y in range(n,x+1,-1):
        H = L[x:y]
        K = sorted(H) #到此已给出单个排序列表
        j = 0
        for i in range(0,len(K) - 1):
            if (K[i+1] - K[i] == 1 or K[i+1] - K[i] == 0):
                j = j + 1
                if j == len(K) - 1:    #当他为顺子时
                    if (len(K) >= len(Z)):
                        Z = H
if Z == []:
    Z = L[0]
        
                
                
                       
        
print(Z)
        
        
        
        