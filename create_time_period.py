import csv
import json

def create_time_period():
    start_epoch = raw_input("Enter start epoch: ") 
    end_epoch = raw_input("Enter end epoch: ")
    filename = raw_input("Enter the json filename to which the excel row needs to be stored (default - result.json): ")
    filename = filename or 'result'
    with open('full_data.csv','r') as full_data:
        csvreader = csv.reader(full_data)
        fields = next(csvreader)
        # start_epoch = 988675200
        # end_epoch = 988678800
        # filename = 'aswin'
        data = []
        found_start = False
        for row in csvreader:
            if found_start == True:
                data.append(row)
            
            if row[0] == str(start_epoch):
                data.append(row)
                found_start = True
            
            if row[0] == str(end_epoch):
                break
        
        json_data = []
        for d in data:
            json_object = {}
            for field, value in zip(fields, d):
                json_object[field] = value
            json_data.append(json_object)
        if not filename.endswith('json'):
            filename = filename+'.json'
        with open(filename, 'w') as outfile:
            json.dump(json_data, outfile)


if __name__ == "__main__":
    create_time_period()