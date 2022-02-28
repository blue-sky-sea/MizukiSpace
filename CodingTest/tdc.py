import sys
def has_pattern(l):
    pattern_list = ['SSS','SS.','.SS','.S.','S']
    for pattern in pattern_list:
        i = l.find(pattern)
        if(i!=-1):
            l = motivate(l,i)
            return i,l
        else:
            continue
    return -1,l



def motivate(l,i):
    l = list(l)
    l[i]="."
    l[i+1]="."
    l[i+2]="."
    l = ''.join(l)
    return l

def count__(l):
    n=0
    for i in l:
        if(i=="."):
            n=n+1
    return n
def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    n=0
    k=0
    for i, v in enumerate(lines):
        #print("line[{0}]: {1}".format(i, v))

        if(i==0):
            n,k = map(int,v.split())
        elif(i==1):
            list_s = list(v)
            s = v

            #print("for ,",k)
            motivate_k=0
            l=s
            while(True):
                #print("start for ,",k)
                if(motivate_k>=k):
                    #print("MAX")
                    break
                i,l = has_pattern(l)
                #print(i,"##",l)

                motivate_k = motivate_k+1       
            n = count__(l)
            #print(l)
            print(n)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
