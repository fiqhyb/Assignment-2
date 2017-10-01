import time
def CNB():
    t = [0, 1, 0, 0]
    s = list(input("#############################\nEnter moves :").upper())
    for mov in s:
        if   mov == "A":t[0],t[1],t[2],t[3] = t[0],t[2],t[1],t[3]
        elif mov == "B":t[0],t[1],t[2],t[3] = t[0],t[1],t[3],t[2]
        elif mov == "C":t[0],t[1],t[2],t[3] = t[0],t[3],t[2],t[1]
    print("The ball is inside cup",t.index(1))
    time.sleep(3)