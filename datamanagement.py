import json


with open('schedule.json') as data:
    data = json.load(data)
    shifts = data['shifts']
    employees = data['employees']

    print(shifts)

