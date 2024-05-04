import csv
first = False
with open('data.csv', newline='') as f:
    data = csv.reader(f)
    fare_not_survived= []
    fare_survived = []
    for raw in data:
        if first:
            if int(raw[1]) == 0:
                fare_not_survived.append(float(raw[9]))
            if int(raw[1]) == 1:
                fare_survived.append(float(raw[9]))
        first = True
    sum_survived = 0.0
    for fare in fare_survived:
        sum_survived += fare
    print(f"Средняя стоимость билета у спасённых {sum_survived/len(fare_survived)}")
    sum_not_survived = 0.0
    for fare in fare_not_survived:
        sum_not_survived += fare
    print(f"Средняя стоимость билета у погибших {sum_not_survived / len(fare_not_survived)}")