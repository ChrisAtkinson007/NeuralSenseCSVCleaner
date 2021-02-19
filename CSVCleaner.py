import pandas as pd
import os

path=os.getcwd()+'\processed'
try:
    os.mkdir(path)
except:
    print("file already exists")

ClientCode=input("Please input a 4 character client code: ")
while len(ClientCode)!=4:
    ClientCode=input("Incorrect Client Code Length, Please try again ")

ProjDate=input("Please input 6 digits yy/mm/dd representing the project date: ")
while len(ProjDate)!=6:
    ProjDate=input("Incorrect Date Length, Please try again ")

SubCode=input("Please enter sub project code: ")
while (len(SubCode)<1) or (len(SubCode)>9):
    SubCode=input("Please try enter sub project code again: ")

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.csv'):
        print(filename)
        #This needs to change, to include all digits before the final .csv, if there are not 2-3 digits leading the .csv, it should ask for a manual respondent number.
        RespCode = "0"+filename[-6:-4]
        Fname = ClientCode + "_" + ProjDate + "_" + SubCode + "_" + RespCode + "_e.csv"
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