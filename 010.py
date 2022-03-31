# ===========================
#       tenkei 90 #010
# Author: kenkn(Sawada Kenta)
# ===========================

def main():
    n = int(input())
    cp = []
    for _ in range(n):
        c, p = map(int,input().split())
        cp.append((c, p))
    q_num = int(input())
    query = []
    for _ in range(q_num):
        l, r = map(int,input().split())
        query.append((l, r))
    
    cls_1 = [0]
    cls_2 = [0]
    for ccpp in cp:
        if ccpp[0] == 1:
            cls_1.append(cls_1[-1]+ccpp[1])
            cls_2.append(cls_2[-1])
        else:
            cls_1.append(cls_1[-1])
            cls_2.append(cls_2[-1]+ccpp[1])

    for q in query:
        print(cls_1[q[1]]-cls_1[q[0]-1], cls_2[q[1]]-cls_2[q[0]-1])


if __name__ == '__main__':
    main()