def solve(inp):
    new = []
    count = 0
    for i in inp:
        if i == 0: count +=1
        else:
            new.append(i)
    for i in range(count):
        new.append(0)
    return new

def solve2(inp):
    for i in range(len(inp)):
        if inp[i] == 0: 
            inp.append(0)
            del inp[i]
    return inp

def solve3(inp):
    l: int = len(inp)
    for i in range(l-1):
        if inp[i]==0:
            for j in range(i+1,l):
                if inp[j]!=0:
                    temp=inp[i]
                    inp[i]=inp[j]
                    inp[j]=temp
                    i+=1
    return inp

def solve4(inp):
    a = -1
    l = len(inp)
    for i in range(l):
        if inp[i] == 0:
            a = i
            break
    
    if a == -1 or a == l: return inp
    
    for j in range(a+1, l):
        print(a,j)
        if inp[j] == 0: continue
        inp[a], inp[j] = inp[j], inp[a]
        a+=1
    
    return inp
    
if __name__ =="__main__":
    inp = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
    print(solve([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))
    print(solve2([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))
    print(solve3([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))
    print(solve4([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))