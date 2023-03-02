import pandas as pd
# import csv
# with open('ClassDataWItemNum.csv', 'r') as file:
#     reader = csv.reader(file)

#     for line in reader:
#         id = line[1]
#         print(id[0:4])

    

table = pd.read_csv("ClassDataWItemNum.csv")
table.to_html("Index.html")
htmlFile = table.to_html()