import sys
import json


def addValues(dataTest, dataValue):
    for test in dataTest:
        v = next((item for item in dataValue if item['id'] == test['id']), None)
        if v:
            test['value'] = v['value']
        if 'values' in test:
            addValues(test['values'], dataValue)

valueF = open(sys.argv[1])
dataValue = json.load(valueF)['values']
testF = open(sys.argv[2])
dataTest = json.load(testF)['tests']
reportF = open(sys.argv[3], 'w')

addValues(dataTest, dataValue)
json.dump(dataTest, reportF, indent=4)

valueF.close()
testF.close()
reportF.close()


