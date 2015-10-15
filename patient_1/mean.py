import csv
import numpy

id = 1
sum = 0
value = 0
j = 1
count = 0
list1 = []
list2 = []
f = open("F:\E\entertainment\Machine Learning\Hackerrank\Xerox 15\id_time_vitals_train.csv")
csv_f = csv.reader(f)
next(csv_f,None)

for row in csv_f:
    if (row[0] == str(j+1)):
        
        print("%d  %f",id,sum/count)
        #print(count)
        sum = 0
        id = id +1
        count = 0
        j = j + 1
        if(row[2] == "NA"):
                value = 0
        else:
                value = row[2]
        sum = sum + float(value)
        count = count + 1
    else:
        
        
        #if (row[0] == "1"):
        
           if(row[2] == "NA"):
                value = 0
           else:
                value = row[2]
           sum = sum + float(value)
           count = count + 1


f.close()
