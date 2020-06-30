import os
import pickle
import marshal
import json


cases = [
{'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}, 
{'name':'Saving Private Ryan', 'year':1998, 'director':'Steven Spielberg', 'Writer': 'Robert Rodat'},
dict(name='The Breakfast Club', year=1985, director='John Hughes'),
{'name': 'Catch Me If You Can', 'year': 2002, 'director': 'Steven Spielberg'},
dict([('name', 'python'), ('version', '3.5')]),
{'Colorado' : 'Rockies', 'Boston'   : 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle'  : 'Mariners'},
{1: 123, 2: 456},
{"jey": [1, 2, 3, 4]},
{1: 0},
{}
]

print('JSON    Pickle  Marshal')
for dic in cases:
	with open('p.pickle', 'wb') as file:
		pickle.dump(dic, file)

	with open('j.json', 'w') as file:
		json.dump(dic, file)

	with open('m.marshal', 'wb') as file:
		marshal.dump(dic, file)

	json_file = 'j.json'
	pickle_file = 'p.pickle'
	marshal_file = 'm.marshal'
	print(f"{os.path.getsize(json_file):<7} {os.path.getsize(pickle_file):<7} {os.path.getsize(marshal_file):<7}")