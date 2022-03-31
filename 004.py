# ===========================
#       tenkei 90 #004
# Author: kenkn(Sawada Kenta)
# ===========================

def main():
    colsize, rowsize = map(int,input().split())
    a = []
    for i in range(colsize):
        aa = list(map(int,input().split()))
        a.append(aa)

    rowsum = []
    for i in range(colsize):
        rowsum.append(sum(a[i]))

    colsum = []
    for i in range(rowsize):
        s = 0
        for j in range(colsize):
            s += a[j][i]
        colsum.append(s)
    
    ans = [[0 for _ in range(rowsize)] for _ in range(colsize)]
    for i in range(colsize):
        for j in range(rowsize):
            ans[i][j] = rowsum[i] + colsum[j] - a[i][j]
    
    for i in range(colsize):
        print(*ans[i])

if __name__ == '__main__':
    main()