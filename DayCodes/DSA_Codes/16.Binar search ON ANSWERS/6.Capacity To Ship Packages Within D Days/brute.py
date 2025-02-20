def leastWeightCapacity(weights, d):
    def finddays(weights,capacity):
        posiidays=1
        load=0
        for i in range(0,len(weights)):
            if load+weights[i]>capacity:
                posiidays+=1
                load=weights[i]
            else:
                load=load+weights[i]
        return posiidays
    
    for i in range(max(weights),sum(weights)+1):#imp +1
        posiidays=finddays(weights,i)
        if posiidays<=d:
            return i