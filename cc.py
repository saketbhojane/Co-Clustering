import os
import sys
from collections import defaultdict
import numpy as np
from coclust.coclustering import CoclustMod
from coclust.evaluation.internal import best_modularity_partition
from coclust.visualization import (plot_max_modularities)

path = sys.argv[1]

def metric(filename, predicted_row_labels, numcategories, labels):
    numcircles = 0
    circlescore = 0
    with open(filename,'r') as f:
        for line in f:
            numcircles += 1
            line = line.split()[1:]
            numpeople = len(line)
            print "numpeople", numpeople,

            cats = defaultdict(int)
            for people in line:
                idx = labels.index(people)

                cats[predicted_row_labels[idx]] += 1
            print max(cats.values())*1.0/sum(cats.values())
            circlescore += max(cats.values())*1.0/sum(cats.values())
    return circlescore*1.0/numcircles

egono = 1
for fn in os.listdir(path):
     if os.path.isfile(fn) and fn.endswith(".feat"):
        print "Computing for ego", egono
        egono += 1
        matrix = []
        labels = []
        with open(fn,'r') as f:
            for line in f:
                matrix.append(line.split()[1:])
                labels.append(line.split()[0])
        # print matrix[0]
        X = np.array(matrix)
        # print X

        # model = CoclustMod(n_clusters=4)
        # model.fit(X)

        clusters_range = range(2, 100)
        model, modularities = best_modularity_partition(X, clusters_range, n_rand_init=1)

        print "\nmodularity", model.modularity
        predicted_row_labels = model.row_labels_
        predicted_column_labels = model.column_labels_

        print "\npredicted_row_labels", predicted_row_labels
        print "\npredicted_column_labels", predicted_column_labels

        print "\nNumber of clusters", max(predicted_row_labels)
        print ""

        accuracy = metric(fn.split(".")[0] + ".circles", predicted_row_labels, model.modularity,labels)
        print accuracy
        print ""
