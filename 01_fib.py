

# print("hello Py !w")

# for i in range(1,11):
#     print(i,end="-")
# print("\n\n")

import time
corpus=[]
def fib1(n):
    pass
    if n==0:
        return 1
    if n==1:
        return 1
    return(fib(n-1)+fib(n-2))

def fib(n):
    if n<len(corpus):
        print(corpus[:n])
    else:
        # print("under const !")
        s=len(corpus)
        for i in range(s,n):
            if (i==1 or i==0):
                p=1
            else:
                p = corpus[i-1]+ corpus[i-2]
            corpus.append(p)
        print("in else")
        # print(len(corpus))
        print(corpus)


fib(15)
# fib(14)
# fib(24)
# fib(19)

# c=[1,2,3,4,5,6]
# print(c[1:4])
