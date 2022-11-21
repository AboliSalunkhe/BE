
profit = [60, 100, 120]
weight = [10, 40, 30]
WTarget = 70


for i in range(3):
    for j in range(3):
        if(i!=j and i<j):
            print(i,j)
            if((weight[i]+weight[j])==WTarget):
                print(profit[i]+profit[j])
           

 
