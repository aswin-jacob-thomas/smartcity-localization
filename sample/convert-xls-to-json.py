import xlrd
from collections import OrderedDict
import json
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('./localtest.xlsx')
sh = wb.sheet_by_index(0)
# List to hold dictionaries
data_list = []
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(0, sh.nrows):
    data = OrderedDict()
    row_values = sh.row_values(rownum)
    data['latitude'] = row_values[0]
    data['longitude'] = row_values[1]
    data['compass'] = row_values[2]
    data['image'] = "random.jpeg"
    data_list.append(data)
data_list = {'data': data_list} # Added line
# Serialize the list of dicts to JSON
j = json.dumps(data_list)
# Write to file
with open('geo.json', 'w') as f:
    f.write(j)