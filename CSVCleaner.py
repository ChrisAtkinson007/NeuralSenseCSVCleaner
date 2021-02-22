import pandas as pd
import os

#Create a folder called processed in the current working directory
path=os.getcwd()+'\processed'
try:
    os.mkdir(path)
except:
    print("file already exists")

#Prompt user input create the .csv name using the naming convention
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
        print("_____________________________ \n")
        print(filename)
        #This needs to change, to include all digits before the final .csv, if there are not 2-3 digits leading the .csv, it should ask for a manual respondent number.
        RespCode=filename.split("_")
        RespCode=RespCode[-1].split(".")
        RespCode=RespCode[0]
        Fname = ClientCode + "_" + ProjDate + "_" + SubCode + "_" + RespCode + "_EEG.csv"
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
        prelength=len(data)
        #Removing all NaN rows
        data=data.dropna()
        postlength=len(data)
        #Giving an indication of what % of data was removed as NaN
        print(str(round(((prelength-postlength)/prelength)*100)) + "% Of the data was removed as NaN values")
        direc=path + "\\"+Fname
        print(direc)
        data.to_csv(direc)
input("Press enter to exit the program")