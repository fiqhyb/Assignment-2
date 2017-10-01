import time
def Mod42():####Modulo by 42####
    print("#############################")
    list=[]
    for i in range(10):
        print(i+1,end=". ")
        num=int(input("Enter Number : "))
        list.append(num)
    cal=[num % 42 for num in list]
    print(" Distinct value  :",len(set(cal)))
    time.sleep(3)