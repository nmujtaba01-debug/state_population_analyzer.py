states = [
    {'name':'West Bengal', 'population':91276115},
    {'name':'Rajasthan', 'population':68548437},
    {'name':'Assam', 'population':31205576},
    {'name':'Sikkim', 'population':610577}
]

print("STATE POPULATION ANALYZER")
print("-------------------------")

highest_population = states[0]['population']
highest_population_state = states[0]['name']

lowest_population = states[0]['population']
lowest_population_state = states[0]['name']

total_population = 0

for state in states:
    total_population += state['population']

    if state['population'] > highest_population:
        highest_population = state['population']
        highest_population_state = state['name']

    if state['population'] < lowest_population:
        lowest_population = state['population']
        lowest_population_state = state['name']

average_population = total_population / len(states)

print('highest population:', highest_population)
print('highest population state:', highest_population_state)

print('lowest population:', lowest_population)
print('lowest population state:', lowest_population_state)

print('average population:', average_population)
print('total population:', total_population)