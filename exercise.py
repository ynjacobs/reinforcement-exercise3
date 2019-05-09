def get_trains(schedule, direction):
    trains = []
    for train in schedule:
        if train['direction'] == direction:
            trains.append(train)
    return trains


train_schedule = [
    {'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
    {'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
    {'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
    {'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
    {'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
    {'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
    {'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

direction_train_111 = "south"
frequency_train_80B = 30
direction_train_610 = "north"


print(get_trains(train_schedule, "east"))
print(get_trains(train_schedule, "north"))




# Now we want to (programmatically) make a new dictionary where the train frequencies are the keys
# and the values are a list of train names, like so: python 
# { 15: ['72C', '72D', '110', '111'], 5: ['610', '611'], 30: ['80A', '80B'] } 

train = train_schedule[0]
train['first_departure_time'] = 6
print(train_schedule)






