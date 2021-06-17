def main():
    f = open('sample_input.txt')
    T = int(f.readline())
    for t in range(T):
        ans = 99999999999999
        N, K = map(int, f.readline().split())
        rings = []
        for i in range(K):
            rings.append(list(f.readline().rstrip()))

        for i in range(len(rings)):
            cnt = 0
            for j in range(N):
                if rings[i][j] == '1':
                    continue
                else:
                    qq = 100001
                    for p in range(K):
                        if rings[p][j] == '1':
                            qq = min(qq, min(abs(p-i), K-abs(p-i)))
                    cnt += qq

            ans = min(ans, cnt)
        print('#', t+1, ' ', ans, sep = '')

main()
