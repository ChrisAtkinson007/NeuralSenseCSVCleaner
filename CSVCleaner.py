import pandas as pd
import os

for filename in os.listdir('C:/Users/Chris (Admin)/PycharmProjects/NSenseCSVCleaner'):
    if filename.endswith('.csv'):
        print(filename)
        #Read in files from working directory
        data=pd.read_csv(filename)
        #Isolate first row of data, as the new headers
        header=data.iloc[0]
        #Rename Event source to ESource to deal with duplicate column header issue
        header[2]="ESource"
        data=data[1:]
        #Rename headers from #DATA, Unnamed, e.t.c to actual headers
        data=data.rename(columns = header)
        data.index = data.Timestamp
        #print(data.head())
        #Remove all rows where Event Source = 1,these are slide event rows
        data=data[data.ESource!='1']

        #Removing all the unwanted columns
        data=data.drop(['Timestamp', 'Row', 'ESource', 'SlideEvent', 'StimType', 'Duration', 'CollectionPhase', 'EventSource'], axis=1)
        #Removing all NaN rows
        data=data.dropna()
        direc=r'C:\Users\Chris (Admin)\PycharmProjects\NSenseCSVCleaner\Processed\proc' + filename
        data.to_csv(direc)