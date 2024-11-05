import csv
with open('TVAQueries.txt', 'r' ,encoding='utf-8') as file1 , open('output.csv',"w",encoding='utf-8') as file2:
    fin =[]
    data = file1.readlines()  
    list=[]
    for i in data:
       list.append(i)
       if(len(list)==1000):
           fin.append(list)
           list=[]


    csv.writer(file2).writerows(fin)  

        



       
          


