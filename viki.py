
# coding:utf-8

def remove_tag(s):
    s = s.replace('<i>','')
    s = s.replace('</i>','')
    s = s.replace('<br>','')
    return s


# This read Korean seq, and patch Chinese.
# So this is no orphan Chinese.
# If normal is false, reverse
def merge(k,c,normal=True):
    kr = open(k)
    lines = [ x.rstrip() for x in kr.readlines()]
    # [(t,content)]
    A = []
    for i in xrange(0,len(lines),4):
        A.append((lines[i+1],remove_tag(lines[i+2])))

    cn = open(c)
    lines = [ x.rstrip() for x in cn.readlines()]
    B = {}
    # key time, value content
    for i in xrange(0,len(lines),4):
        B[lines[i+1]] = remove_tag(lines[i+2])
    for i in xrange(len(A)):
        t,text = A[i]
        print i+2
        print t
        if normal:
            print text
            print B[t]
        else:
            print B[t]
            print text
        print

merge('kr.srt','cn.srt')
