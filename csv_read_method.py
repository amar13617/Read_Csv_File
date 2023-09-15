import csv

with open(r'C:\Users\LENOVO\Desktop\Employee_Detail.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    print(csv_reader)
    
    for line in csv_reader:
        print(line)
        
        