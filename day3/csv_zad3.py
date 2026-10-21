import pandas

# pip install pandas

data = pandas.read_csv('records_discount.csv')

print(data)
#    sku  exp_date    price
# 0    1     today   200.00
# 1    2     today   300.00
# 2    3  tomorrow   400.00
# 3    4     today  1200.00
# 4    5     today   900.00
# 5    6  tomorrow   200.99
# 6    7     today   100.00

print(data.columns)
# # Index(['sku', 'exp_date', 'price'], dtype='str')

print(data.values)
# [[1 'today' 200.0]
#  [2 'today' 300.0]
#  [3 'tomorrow' 400.0]
#  [4 'today' 1200.0]
#  [5 'today' 900.0]
#  [6 'tomorrow' 200.99]
#  [7 'today' 100.0]]

