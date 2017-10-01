def interface():
    while True:
        print("#############################")
        list=("1. KMP\n2. Modulo42\n3. AliceNBob\n4. CupsNBall\nEnter 'Q' to quit\n")
        select=input(list+"Enter a program to run    :").upper()
        import Programs.KMP as a
        import Programs.Modulo42 as b
        import Programs.AliceNBob as c
        import Programs.CupsNBall as d
        if select=="1":
            a.kmp()
        elif select=="2":
            b.Mod42()
        elif select=="3":
            c.ANB()
        elif select=="4":
            d.CNB()
        elif select=="Q":
            quit()