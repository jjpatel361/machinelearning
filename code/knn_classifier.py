''''
    Nearest Neighbour Classifier
    :arg dataset.data
    :arg trainlabel.0
    :arg eta
'''

import sys;
import os;
'''
    Read the data set file and labels file
'''
ds_file = sys.argv[1];
fh = open(ds_file, mode='r');

dataset = [];
for line in fh:
    arr = line.split();
    arr = [float(i) for i in arr];
    dataset.append(arr);

labels_file = sys.argv[2];

labels = {};
fh = open(labels_file, mode= 'r');
for line in fh:
    arr = line.split();
    labels[arr[1]] = float(arr[0]);

fh.close()

#print('Dataset',dataset)
#print('Labels',labels)

rows = len(dataset);
cols = len(dataset[0]);


'''
    Split dataset into seperate classes
'''
classes = {};
testing = {};
for index in range(rows):
    xi = dataset[index];
    if str(index) in labels:
        yi = int(labels.get(str(index)));
        if str(yi) not in classes:
            # Add class and then add item
            classes[str(yi)] = [];
        classes[str(yi)].append(xi);
    else:
        # use sample for testing
        #testing.append(xi);
        testing[index] = xi;

#print('Classes', classes)

'''
    Find mean of each feature Xi
'''

mean_c = {};
for i in range(len(classes)):
    ds = classes.get(str(i));
    yi = i;
    mean = [];
    # Find mean of each column
    for k in range(cols):
        feature_vec = [i[k] for i in ds];
        mean_k = sum(feature_vec)/len(feature_vec);
        mean.append(mean_k);
    mean_c[yi] = mean;


#print('Mean ',mean_c)


'''
    Prediction on test
    Those samples whose labels are not found are used for testing.
'''


def eculideanDistance(a, b):
    dist = 0;
    if(len(a)==len(b)):
        for i in range(len(a)):
             dist += (a[i]-b[i])**2;
    return dist**0.5


def nearestNeighbour(result):
    result_class = min(result.items(), key=lambda x: x[1])[0]
    return result_class


## Prepare output directory and write result to it.
current_dir = os.getcwd();
result_dir = os.path.join(os.getcwd(),'knn_results');


if not os.path.exists(result_dir):
    os.makedirs(result_dir)
#else:
#    os.removedirs(result_dir)
#    os.makedirs(result_dir)

output_file = os.path.join(result_dir,'knn_result.'+sys.argv[3]+'.txt');
f = open(output_file,'w');


for index, xtest in testing.items():
    result = {};
    # Find mean for all classes
    for l, mc in mean_c.items():
        #print('Label',l,'MC',mc)
        dist = eculideanDistance(xtest, mc);
        result[l] = dist;

    #print(result)
    # Find class of nearest mean to the sample
    predicted_class = nearestNeighbour(result);
    print(predicted_class,index,file=f);


