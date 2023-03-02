import pandas as pd
    

table = pd.read_csv("ClassDataWItemNum.csv")
table.to_html("Index.html")
htmlFile = table.to_html()