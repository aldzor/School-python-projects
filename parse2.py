import json
data = {}
i = 0

with open('data/L233_19_12.json', 'r') as dataSet:
    rawdata = json.load(dataSet)

for item in range(len(rawdata)):
    timestamp = rawdata[i]['Time']
    try:
        data[timestamp][rawdata[i]['Sensor']] = rawdata[i]['Measurement']
    except KeyError as err:
        data[timestamp] = {}
        data[timestamp][rawdata[i]['Sensor']] = rawdata[i]['Measurement']
    i = i+1

with open('data/parsed/L233_19_12.json', 'w') as writeFile:
    json.dump(data, writeFile, sort_keys=True, indent=4)
