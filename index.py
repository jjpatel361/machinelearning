'''
    Home to start run all classifiers.
'''

from code.KNNClassifier import *;
from code.DataSetReader import *;

knn = KNNClassifier();
reader = DataSetReader();

ds = reader.readDataFile('datasets/dummy_ds/knn_data.txt');
labels = reader.readLabels('datasets/dummy_ds/knn_label.txt');

print(labels);
print(ds)

knn.setData(ds);
knn.setLabels(labels)
