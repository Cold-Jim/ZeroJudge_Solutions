from itertools import permutations

while(True):
    try:
        line = input().strip()
        if not line:
            continue
        
        Colors = ["B" , "C" , "G"]

        n = [int(i) for i in line.split()]
        total_b = sum(n) 

        # 每一箱瓶子做區分，然後交換 C 和 G ， 方便後面操作
        nums = [[n[i] , n[i + 2] , n[i + 1]] for i in range(0 , 9 , 3)]

        ans_n = float("inf") # 表示正無限大
        ans_b = ""

        # permutations 會按數字大小自動產生字典序排列：(0,1,2) = BCG, (0,2,1) = BGC, (1,0,2) = CBG...
        for p in permutations(range(3)):
            # i , colors_idx 是 第 i 箱的第 colors_idx (顏色)
            # enumerate 是前面每一個組合前面加上 index 來標示
            # nums[i][colors_idx] 代表第 i 箱保留 colors_idx 顏色（例如第 0 箱取 0=B，第 1 箱取 1=C，第 2 箱取 2=G）
            # 這邊要看設立的顏色 list 的順序，題目是 BGC ，所以換成 BCG
            stay_b = sum(nums[i][colors_idx] for i , colors_idx in enumerate(p))   

            # 移動最少 = 留在原地不動的瓶子最多（總數 - 原地保留數 = 搬移數）
            moves = total_b - stay_b  
            
            # 用嚴格小於（<）：若遇到相同移動次數，「 不進行覆蓋 」，自動保留先出現（字典序較小）的解答
            if moves < ans_n:
                ans_n = moves
                ans_b = "".join( Colors[c] for c in p)

        print(ans_b , ans_n)
        
    except EOFError:
        break

# version 2
# => 使用迴圈與枚舉

# c081.00102 - Ecological Bin Packing
# https://zerojudge.tw/ShowProblem?problemid=c081