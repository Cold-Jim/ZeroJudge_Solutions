import math

def main():
     while(True):
        try:
            line = input().strip()
            if not line:
                continue

            N = int(line)

            # 前設置
            total_pri = 0
            total_un = 0
            ans_list = [False] * (N + 1)

            #======================================================
            # 歐幾里得公式（Euclid's Formula）——「畢氏三元數生成公式」
            # x = m^2 - n^2
            # y = 2mn
            # z = m^2 + n^2

            # isqrt(N) 是回傳不大於 sqrt(N) 的最大整數，像是 isqrt(10) = 3
            the_end = math.isqrt(N)

            # 雙層迴圈找mn，範圍由於 m > n 且 m 包含 the_end , 故 2 ~ the_end + 1 
            for m in range(2 , the_end + 1):
                # 範圍由於 m > n , 故 1 ~ m
                for n in range(1 , m):

                    # 過濾
                    # 條件一 : m , n 最大公因數為 1
                    if math.gcd(m , n) != 1:
                        continue
                    # 條件二 : m , n 為一奇一偶
                    if (m - n) % 2 != 1:
                        continue
                
                    x = pow(m , 2) - pow(n , 2)
                    y = 2 * m * n
                    z = pow(m , 2) + pow(n , 2)

                    # 提早 break ，當 n 過大會使後面都超出範圍
                    if z > N:
                        break

                    # 找出一組解，且 x y z 互質。判斷完才能加入
                    total_pri += 1
                        
                    # 每次迴圈乘範圍內的最大倍數，可找出此組合的所有 x y z 
                    # 因為是倍數的關係，故其他的 m n 組合不會導致重複的 x y z
                    for i in range(1 , N//z + 1):
                        ans_list[x * i] = True
                        ans_list[y * i] = True
                        ans_list[z * i] = True

            total_un = sum([1 for i in range(1 , N + 1) if not ans_list[i]])

            print(total_pri, total_un)

        except EOFError:
            break
if __name__ == "__main__":
    main()