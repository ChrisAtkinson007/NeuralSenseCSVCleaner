import pandas as pd
import os

path=os.getcwd()+'\processed'
try:
    os.mkdir(path)
except:
    print("file already exists")

ClientCode=input("Please input a 4 character client code: ")
while len(ClientCode)!=4:
    ClientCode=input("Incorrect Client Code Length, Please try again")

ProjDate=input("Please input 6 digits yy/mm/dd representing the project date: ")
while len(ProjDate)!=6:
    ProjDate=input("Incorrect Date Length, Please try again")

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.csv'):
        print(filename)
        RespCode = filename[-6:-4]
        Fname = ClientCode + "_" + ProjDate + "_" + RespCode + "_e.csv"
        print(Fname)
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
        direc=path + "\\"+Fname
        print(direc)
        data.to_csv(direc)