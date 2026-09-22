while(True):
    try:
        line = input().strip()
        if not line:
            continue

        b1 , g1 , c1 , b2 , g2 , c2 , b3 , g3 , c3 = [int(i) for i in line.split()]

        dt = {"BCG" : 0 , "BGC" : 0 , "CBG" : 0 , "CGB" : 0 , "GBC" : 0 , "GCB" : 0}
        total = 0

        tb = b1 + b2 + b3
        tg = g1 + g2 + g3
        tc = c1 + c2 + c3

        dt["BCG"] = g1 + c1 + b2 + g2 + b3 + c3
        dt["BGC"] = g1 + c1 + b2 + c2 + b3 + g3 
        dt["CBG"] = g1 + b1 + c2 + g2 + b3 + c3
        dt["CGB"] = g1 + b1 + b2 + c2 + g3 + c3
        dt["GBC"] = b1 + c1 + c2 + g2 + b3 + g3
        dt["GCB"] = b1 + c1 + b2 + g2 + g3 + c3
        
        ans = sorted(dt.items() , key=lambda x : x[1])

        print(ans[0][0] , ans[0][1])

    except EOFError:
        break

# version 1
# 直接把每一個結果都枚舉出來

# c081.00102 - Ecological Bin Packing
# https://zerojudge.tw/ShowProblem?problemid=c081
