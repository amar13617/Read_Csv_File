import csv

with open(r'hello_world.csv','w') as f:
    f.write("Amar Kumar")
    
print(f)

with open("add_detail.csv", "a") as f:
    f.write("\nHello Amar")
    f.write("\nHow are you")
    f.write("\nFine")