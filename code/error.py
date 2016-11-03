import sys;

# take the first argument as master data
# second argument as the predicted results
correct_results = sys.argv[1];
predicted_results = sys.argv[2];

#print(correct_results)

fh = open(correct_results, 'r');
correct_labels = {};
for line_number, line in enumerate(fh):
    arr = line.split();
    correct_labels[arr[1]] = arr[0];

a=0;
b=0;
c=0;
d=0;
correct_count = 0;
testing_count = 0;
fh = open(predicted_results);
for line_number, line in enumerate(fh):
    testing_count +=1;
    arr = line.split();
    row_index = arr[1];
    prediction = int(arr[0]);
    actual_class = int(correct_labels[row_index]);
    #print('A:',actual_class,'P:',prediction)

    if(actual_class == prediction):
        correct_count+=1;
        if actual_class == 0 and prediction == 0:
            a+=1;
        elif actual_class == 1 and prediction == 1:
            d+=1;
    else:
        if actual_class == 0 and prediction == 1:
            b+=1;
        elif actual_class == 1 and prediction == 0:
            c+=1;




#print(a,b,c,d)
ber = 0.5*((b/(a+b))+(c/(c+d)))
#print('BER is ',ber)
#print('Total Test set', testing_count, ' correct prediction ', correct_count,'A',a,'B',b,'C',c,'D',d,' BER ',ber)
print(ber)
