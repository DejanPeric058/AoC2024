import numpy as np
# A PART
with open("23.txt") as f:
    text = f.read()
counter = 0
commands = text.split('\n')
#print(commands)
V = set()
E = {}
for c in commands:
    a, b = c.split('-')
    V.add(a)
    V.add(b)
    try:
        E[a].append(b)
    except:
        E[a] = [b]
    try:
        E[b].append(a)
    except:
        E[b] = [a]
V = list(V)
stevilke = []
for z, v in enumerate(V):
    if v[0] == 't':
        stevilke.append(z)
# print(V,E)
Em = []
for v in V:
    n = []
    for v1 in V:
        if v1 in E[v]:
            n.append(1)
        else:
            n.append(0)
    Em.append(n)
settt= set()

def find_triangles():
    global Em
    global settt
    for i in range(len(E)):
        for j, a in enumerate(Em[i]):
            if a == 1:
                for k, b in enumerate(Em[j]):
                    if b == 1 and Em[i][k] == 1:
                        sez = sorted([i, j, k])
                        if sez[0] in stevilke or sez[1] in stevilke or sez[2] in stevilke:
                            settt.add(str(sez))

find_triangles()
print(len(settt))
# print(settt)
# Am = np.matrix(Em)
# Am_cubic = Am @ Am @ Am
# print(Am_cubic)
# trace = []
# for i in range(len(V)):
#     trace.append(Am_cubic.item((i,i)))
# print(sum(trace)//6)


import networkx as nx
G = nx.Graph()
for v in V:
    G.add_node(v)
print(G)
for c in commands:
    a, b = c.split('-')
    G.add_edge(a,b)
sez = sorted(max(nx.algorithms.clique.find_cliques(G), key = len))
print(','.join(sez))