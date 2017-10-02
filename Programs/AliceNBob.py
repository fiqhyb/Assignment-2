import time
from Programs.hidden import hidden as h
def ANB():####Game Of Stones####
    ston=int(input("#############################\nNumber of stones on ground  :"))
    if ston==0:print("There is no stones")
    elif ston<0:print(h.a)
    elif ston / 2==0:print("Bob wins")
    else:print("Alice Wins")
    time.sleep(3)