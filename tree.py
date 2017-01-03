import sys

d = dict()
def tree(cid):
    l = []
    if cid in d.keys():
        if d[cid] != None:
            s = d[cid].split(';')
            l+=s
            for cropid in s:
                tree(cropid)
    for cid in l:
        if cid in d.keys():
            print cid
    
def mk_dict():
    fin = open('emp.txt')
    for l in fin:
        s = l.split(':')
        d[s[0]]=s[7]

mk_dict()
tree(str(raw_input('Enter :')))


