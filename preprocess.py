import sys
import os

egoinfo = {}
direct_edges_file = sys.argv[1]
with open(direct_edges_file,'r') as f:
    for edge in f:
        tup = tuple(map(int, edge.split()))
        egoinfo[tup] = [1, 0]

dataset = sys.argv[2]
dataset.strip()

if dataset[-1] == "/":
    dataset = dataset[:-1]

def find_group_edges(circle):
    length = len(circle)

    for i in range(length - 1):
        for j in range(i + 1, length):
            tup = (circle[i], circle[j])

            if egoinfo.get(tup) == None:
                egoinfo[tup] = [0, 1]
            else:
                egoinfo[tup][1] += 1

for fn in os.listdir(dataset):
    if fn.endswith(".circles"):
         with open(dataset + "/" + fn,'r') as f:
             for circle in f:
                 circle = circle.split()
                 circle[0] = fn.split(".")[0]
                 circle = [int(i) for i in circle]
                 circle.sort()

                 find_group_edges(circle)

print "Node1\tNode2\tDirect_Edge\tCommon_Groups"

for key, value in egoinfo.iteritems():
    print key[0], "\t", key[1], "\t", value[0], "\t", value[1]
