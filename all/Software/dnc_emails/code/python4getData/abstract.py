import time
import os
import File_Interface as FI
import json
import xlrd
import xlwt
'''
edges = FI.load_pickle('.\\temp_res\\edge.pkl')
edges = list(edges.values())

f1 = open(".\\temp_res\\edge1.csv", 'w+')
f2 = open(".\\temp_res\\edge2.csv", 'w+')
f3 = open(".\\temp_res\\edge3.csv", 'w+')
for edge in edges:
    #print('{a}\t{b}\t{c}'.format(a=edge[0],b=edge[1],c=edge[2]),file=f)
    print('{a}'.format(a=edge[0]), file=f1)
    print('{b}'.format(b=edge[1]), file=f2)
    print('{c}'.format(c=edge[2]), file=f3)
'''

nodes = FI.load_pickle('.\\temp_res\\node.pkl')
nodes = list(nodes.values())
f111 = open(".\\temp_res\\node_name.csv", 'w+')
for node in nodes:
   #print('{a}'.format(a=node['receive']), file=f111)
   #if  node['name'] == None:
       # node['name'] = '\t'
   #print('{a},{c},{d},{e},{f},'.format(a=node['mail'],  c=node['receive'],d=node['ori_mail'],e=node['cc'],f=node['send']), file=f111)