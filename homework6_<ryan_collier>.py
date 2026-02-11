#Homework Week 6 - Conditional Lists and Nested Dictionaries
#Defining Lists
web_users = ['BigRed1', 'blueLead6', 'shaKira7', 'exp33','olDannyBoi']
new_users = ['RedLeader6', 'shaKira7', 'olDannyBoi', 'Num12', 'Osprey8']

#Testing new users against web users - conditional
#ReadMe does not specify to print the specific username referenced, thus not included in printout
for user in new_users:
    if user in web_users:
        print("This user name is in use. Please choose another username")
    else: 
        print ("This user name is available")
#Line break for end output readability
print('\n')

#Part 2: Nested Dictionaries
#Empty 'cities' dictionary created. Cities dictionary populated
cities = {}
cities['Berlin'] = {'country': 'Germany', 'population':'3,680,000', 'fact': '30% of the city is green space'}
cities['Athens'] = {'country': 'Greece', 'population': '3,200,000', 'fact':'known as the birthplace of democracy'}
cities['Paris'] = {'country':'France', 'population':'2,000,000', 'fact':'nicknamed the City of Light'}
#Cities Keys populated
#Call to print Cities dictionary in format: City, Country, Population, Fact
#No other specific formatting requested / defined to further clean up printout 
print(cities)

