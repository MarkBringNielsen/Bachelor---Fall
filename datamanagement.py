import json

def load():
    with open('smaller_schedule.json') as data:
        data = json.load(data)




        



        shifts = data['shifts']
        employees = data['employees']

        return shifts, employees

