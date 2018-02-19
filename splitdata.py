import numpy as np
from sklearn.model_selection import train_test_split
import sys
import datetime

filepath = sys.argv[1]

matrix = np.loadtxt(filepath, skiprows=1)

seed1 = int(str(datetime.datetime.now().time()).split('.')[-1][0:2])
seed2 = int(str(datetime.datetime.now().time()).split('.')[-1][2:4])
seed3 = int(str(datetime.datetime.now().time()).split('.')[-1][4:6])

X_train1, X_test1 = train_test_split(matrix, test_size=0.2, random_state=seed1)

# total = X_train1.shape[0] + X_test1.shape[0]
# print X_train1.shape, X_test1.shape, "Total", total, "X_train1 fraction", X_train1.shape[0]*1.0/total, "X_test1 fraction", X_test1.shape[0]*1.0/total

# with open('X_train1.txt','w') as f:
#     f.write("Node1\tNode2\tDirect_Edge\tCommon_Groups")
#
# with open('X_test1.txt','w') as f:
    # f.write("Node1\tNode2\tDirect_Edge\tCommon_Groups")

np.savetxt('X_train1.txt', X_train1, delimiter='\t', header='Node1\tNode2\tDirect_Edge\tCommon_Groups', comments='', fmt='%i')
np.savetxt('X_test1.txt', X_test1, delimiter='\t', header='Node1\tNode2\tDirect_Edge\tCommon_Groups', comments='', fmt='%i')


X_train2, X_test2 = train_test_split(matrix, test_size=0.2, random_state=seed2)


# total = X_train2.shape[0] + X_test2.shape[0]
# print X_train2.shape, X_test2.shape, "Total", total, "X_train2 fraction", X_train2.shape[0]*1.0/total, "X_test2 fraction", X_test2.shape[0]*1.0/total

np.savetxt('X_train2.txt', X_train2, delimiter='\t', header='Node1\tNode2\tDirect_Edge\tCommon_Groups', comments='', fmt='%i')
np.savetxt('X_test2.txt', X_test2, delimiter='\t', header='Node1\tNode2\tDirect_Edge\tCommon_Groups', comments='', fmt='%i')


X_train3, X_test3 = train_test_split(matrix, test_size=0.1, random_state=seed3)

# total = X_train3.shape[0] + X_test3.shape[0]
# print X_train3.shape, X_test3.shape, "Total", total, "X_train3 fraction", X_train3.shape[0]*1.0/total, "X_test3 fraction", X_test3.shape[0]*1.0/total

np.savetxt('X_train3.txt', X_train3, delimiter='\t', header='Node1\tNode2\tDirect_Edge\tCommon_Groups', comments='', fmt='%i')
np.savetxt('X_test3.txt', X_test3, delimiter='\t', header='Node1\tNode2\tDirect_Edge\tCommon_Groups', comments='', fmt='%i')
