def built_list(l , h , r , h_list):
    # 每次覆蓋的範圍只有 l ~ r - 1 ， 所以不用擔心下一個建築無法覆蓋到目前建築的高度
    for i in range(l , r):
        if h > h_list[i]:
            h_list[i] = h

def main():
    the_begin = 10005
    the_end = 0
    h_list = [0] * 10001

    while(True):
        try:
            line = input().strip()
            if not line:
                continue
            l , h , r = [int(i) for i in line.split()]

            # 紀錄有高度建築的範圍，讓最後輸出時不用額外跑其他地方
            the_begin = min(the_begin , l)
            the_end = max(the_end , r)
            
            built_list(l , h , r , h_list)
                
        except EOFError:
            ans = []
            for i in range(the_begin , the_end+1):
                if h_list[i] != h_list[i-1]:
                    ans.extend([str(i) , str(h_list[i])])
            print(" ".join(ans))
            break

if __name__ == "__main__":
    main()

# d424.00105 - The Skyline Problem
# https://zerojudge.tw/ShowProblem?problemid=d424