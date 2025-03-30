data=[1,2,3,12,20,100,6,9,12,8,8,3]

def avg():
    sum=0
    cnt=0
    for i in data:
        sum=sum+i
        cnt=cnt+1
    return sum/cnt

print('平均值为',avg())

def max():
    m=0
    for i in data:
        if i>m:
            m=i
    return m

print('最大值为',max())

def bubbleSort(data):
    for i in range(1,12):
        for j in range(0,12-i):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
    return data

print(bubbleSort(data))
