'''
 F score calculation for feature selection
 @:arg dataset
 @:arg labels
'''

import sys;
import statistics as stat;

fl = sys.argv[1];
fh = open(fl, mode='r');
ds = [];
for line in fh:
    arr = line.split();
    arr = [float(i) for i in arr];
    ds.append(arr);
fh.close();


fl = sys.argv[2];
labels = {};
fh = open(fl, mode='r');
labels = {};
fh = open(fl, mode= 'r');
for line in fh:
    arr = line.split();
    labels[arr[1]] = float(arr[0]);
fh.close()

#print(len(ds));
#print(len(labels))

'''
    seperate dataset based on class
'''

#print(labels)
c0 = [];
c1 = [];
whole =[];
for line,x in enumerate(ds):
    if(str(line) in labels):
        whole.append(x);
        yi = labels.get(str(line));
        if yi == float(0):
            c0.append(x);
        else:
            c1.append(x);

#
#print(len(c0))
#print(len(c1))
#print(len(whole))

def calculateMean(inputds,cols):
    result = [];
    for k in range(cols):
        feature_vector = [t[k] for t in inputds];
        feature_mean = stat.mean(feature_vector);
        result.append(feature_mean);
    return result;


number_of_features = len(ds[0])

# calculate whole mean of every feature vector
all_instances_mean = calculateMean(whole, number_of_features);

# calculate mean of only 0 instances
positive_instances_mean = calculateMean(c1, number_of_features);

# calculate mean of only 1 instances
negative_instance_mean = calculateMean(c0, number_of_features);

#print('Negative instances',negative_instance_mean)
#print('Positive instances', positive_instances_mean);
#print('All Instances', all_instances_mean);

count0 = len(c0);
count1 = len(c1);

def averageDistanceToMean(instances, mean_of_instances, feature_count):
    avg_distance = [];
    for k in range(feature_count):
        feature_vector = [i[k] for i in instances];
        mean_of_feature = mean_of_instances[k];
        # f is col or feature that we can loop
        t = [];
        for item in feature_vector:
            p = (item - mean_of_feature)**2;
            t.append(p);

        result = (1/(len(instances)-1))*sum(t);
        #result = stat.mean(t);
        avg_distance.append(result)

    return avg_distance;


# calculate the difference of each positive instance to its mean
# basically we are taking mean of the distance to the mean of the vector I guess
average_distance_c0 = averageDistanceToMean(c0, negative_instance_mean, number_of_features);
#print('Negative Instance', negative_instance_mean)
#print('Avg distance c0', average_distance_c0)

average_distance_c1 = averageDistanceToMean(c1, positive_instances_mean, number_of_features);
#print('Positive Instance', positive_instances_mean)
#print('Avg distance c1',average_distance_c1)

# this is denominator of the formula
denominator = [p+n for p,n in zip(average_distance_c0,average_distance_c1)];


# calculate numerator of f score formula
positive_discriminant = [(p-w)**2 for p,w in zip(positive_instances_mean, all_instances_mean)];
#print(positive_discriminant)
negative_discriminant = [(p-w)**2 for p,w in zip(negative_instance_mean, all_instances_mean)];
#print(negative_discriminant)

# this is numerator
numerator = [p+n for p,n in zip(positive_discriminant,negative_discriminant)];
#print(numerator)
#print(denominator)

# f score
fscore  = [n/d for n,d in zip(numerator,denominator)];
print(fscore)
