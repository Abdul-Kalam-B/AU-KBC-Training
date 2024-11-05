import csv 
	
# opening the CSV file 
with open('6505_ED_sen_Curated_Rishi.xlsx', mode ='r', encoding='utf-8', errors='replace')as file: 
	data = csv.reader(file)
	for i in data: 
		print(i)
	file.close()	  
	
# displaying the contents of the CSV file 

# reading the CSV file 

