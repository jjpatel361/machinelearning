'''
    Reads datasest files and returns list
'''



class DataSetReader:
    def __init__(self):
        print('Dataset Reader ready to use !!')

    def readDataFile(self,filepath):
        fh = open(filepath, mode='r');
        dataset = [];
        for line in fh:
            arr = line.split();
            arr = [float(i) for i in arr];
            dataset.append(arr);

        fh.close();
        return dataset;

    def readLabels(self,labels_file):
        labels = {};
        fh = open(labels_file, mode= 'r');
        for line in fh:
            arr = line.split();
            labels[arr[1]] = float(arr[0]);
        fh.close()
        return labels;




