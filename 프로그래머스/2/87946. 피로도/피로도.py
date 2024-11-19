import itertools
def solution(k, dungeons):
    li = list(itertools.permutations(dungeons))
    # print(li)
    
    cnt = list()
    for i in range(len(li)) :
        c = 0
        k_ = k
        for j in li[i] :
            if k_ < j[0] :
                break
            else :
                k_ -= j[1]
                c += 1
        cnt.append(c)
    
    return max(cnt)