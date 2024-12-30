import pandas as pd

import numpy as np

dataFrameNot=pd.read_excel("OgrenciNotlari.xlsx")
dataFrameNot.set_index("Ogrenci_No",drop=True,inplace=True)


dataFrameTablo2=pd.read_excel("tablo2.xlsx")
dataFrameTablo1=pd.read_excel("tablo1.xlsx")

dataFrameTablo1.index=[1,2,3,4,5,6,7,8,9,10]


tablo3dataframeNew=None
weightlist=dataFrameTablo2.columns.to_list()


weightdict=dict()
newtablo2value=dataFrameTablo2.loc[0].to_list()

sayac=2

for column in range(len(weightlist)):
    weightdict[weightlist[column]]=newtablo2value[column]
    

dataFrameTablo2.drop(0,axis=0,inplace=True)




def tablo3_Create(originalFrame):

  
    tablo3dataframe = originalFrame.copy()

  
    columns = tablo3dataframe.columns.to_list()
    columns.pop(0)  

   
    for column in columns:        
        coefficient = int(weightdict[column])  
        tablo3dataframe[column] = tablo3dataframe[column].apply(lambda x: x * (coefficient / 100))

    
    tablo3dataframe["TOPLAM"] = tablo3dataframe[columns].sum(axis=1)  

   
    tablo3dataframe.to_excel("tablo3.xlsx", index=False)

    return tablo3dataframe








def Ogrenci_tablo4_Create(StudentNo):

    tablo3_Create(dataFrameTablo2)
    tablo3dataframeNew=tablo3_Create(dataFrameTablo2)
    tablo3dataframeNew.drop("Ders Çıktı",axis=1,inplace=True)
    toplamFrame=tablo3dataframeNew["TOPLAM"]
    
    tablo3dataframeNew.drop("TOPLAM",axis=1,inplace=True)

    StudentDatatablo4=dataFrameNot.loc[StudentNo]

    StudentDataFrame=pd.DataFrame(np.ones((5,5)),columns=["Ödev1","Ödev2","Quiz","Vize","Final"],index=[1,2,3,4,5])

  

    


    indexs=StudentDataFrame.index.to_list()
    columns=StudentDataFrame.columns.to_list()
  

    for row in indexs:


        for column in columns:
            
            StudentDataFrame.loc[row,column]=tablo3dataframeNew.loc[row,column]*StudentDatatablo4[column]

    StudentDataFrame["TOPLAM"]=StudentDataFrame[columns].sum(axis=1)
    StudentDataFrame["MAX"]=toplamFrame*100
    StudentDataFrame["% Başarı"]=(StudentDataFrame["TOPLAM"]/ StudentDataFrame["MAX"])*100
    global sayac
    StudentDataFrame.to_excel("tablo4/tablo4_"+str(StudentNo)+".xlsx",index=False)
    
    Ogrenci_tablo5_Create(StudentNo,StudentDataFrame)

def Ogrenci_tablo5_Create(StudentNo,tablo4frame):

    DataFrameTablo5=dataFrameTablo1.copy()

    tablo5columnslist=tablo4frame["% Başarı"].to_list()
   
    tablo5columnslist = [round(x * 10) / 10 for x in tablo5columnslist]
    
    columns_to_rename = {1.0: tablo5columnslist[0], 2.0: tablo5columnslist[1],3.0:tablo5columnslist[2],4.0:tablo5columnslist[3],5.0:tablo5columnslist[4],"İlişki Değ.":"Başarı Oranı"}
    
    
    
    
    for index in DataFrameTablo5["Prg Çıktı"].to_list():

        for column in DataFrameTablo5.columns.to_list()[1:-1]:
            
            DataFrameTablo5.loc[index,column]=columns_to_rename[column]*dataFrameTablo1.loc[index,column]
    DataFrameTablo5.rename(columns=columns_to_rename,inplace=True)  
    prgiliskidict=dict()
    for index in dataFrameTablo1["Prg Çıktı"].to_list():
        
        prgiliskidict[index]=dataFrameTablo1.loc[index,"İlişki Değ."]

    newcolumns=DataFrameTablo5.columns.to_list()
    newcolumns.pop(0)
    newcolumns.pop(len(newcolumns)-1)
    DataFrameTablo5["Başarı Oranı"] = DataFrameTablo5["Başarı Oranı"].astype(float)

    DataFrameTablo5.columns=['Prg Çıktı',"{}-a".format(newcolumns[0]),"{}-b".format(newcolumns[1]),"{}-c".format(newcolumns[2]),"{}-d".format(newcolumns[3]),"{}-e".format(newcolumns[4]),'Başarı Oranı']
    newcolumns1=DataFrameTablo5.columns.to_list()
    
    newcolumns1.pop(0)
    newcolumns1.remove("Başarı Oranı")
    for index in DataFrameTablo5["Prg Çıktı"].to_list():
        total=0
        
        for column in DataFrameTablo5.columns[1:-1]:
         
            total+=DataFrameTablo5.loc[index,column]
            
            DataFrameTablo5.loc[index,"Başarı Oranı"]=(DataFrameTablo5.loc[index, newcolumns1].sum()/5)/prgiliskidict[index]
            

    
    global sayac
    DataFrameTablo5.to_excel("tablo5/tablo5_"+str(StudentNo)+".xlsx",index=False)
    sayac=sayac+1
   
    
    
    

def WhichStudent(StudentNo):
    Ogrenci_tablo4_Create(StudentNo)



for index in dataFrameNot.index.to_list():
    
    row = dataFrameNot.loc[index] 
    has_null = bool(row.isnull().any())  
  

    if not  has_null:
        WhichStudent(index)




