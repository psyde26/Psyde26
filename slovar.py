gor = {
    'city': 'Москва',
    'temperature': 20 }
print(gor['city'])
gor['temperature'] = gor['temperature'] - 5
print(gor['temperature'])
print(len(gor))
print(gor.get('country'))
print(gor.get('country','Russia'))
gor['date'] = '27.05.19'
print(gor['date'])
print(len(gor))