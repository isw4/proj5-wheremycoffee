import pre

def test_default_restaurants():
	data = pre.process(open('./data/restaurants.txt'))
	assert data[0]['address'] == "3215 W 11th Ave, Eugene, OR, 97402"
	assert data[0]['description'] == "Sushi Island Japanese Restaurant"
	assert data[len(data)-1]['address'] == "750 E 13th Ave, Eugene, OR 97401"
	assert data[len(data)-1]['description'] == "Duck Sushi"
	