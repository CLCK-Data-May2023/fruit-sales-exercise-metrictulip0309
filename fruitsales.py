# add your code here

import pandas as pd


fruit_sales = pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]},index=['2017 Sales','2018 Sales'])

fs = pd.DataFrame(fruit_sales, index = ['2017 Sales', '2018 Sales'])
fs.to_csv('fruit.csv')

print(fs)
