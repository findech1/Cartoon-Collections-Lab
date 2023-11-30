def roll_call_dwarves(dwarves):
    for index, name in enumerate(dwarves, start=1):
        print(f"{index}. {name}")

dwarf_names = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarf_names)

def roll_call_dwarves(list):
    for dwarf in list:
        print(f"{list.index(dwarf) + 1}. {dwarf}")

def summon_captain_planet():
    pass
def summon_captain_planet(planeteer_calls):
    planeteer_calls = [item.capitalize() + "!" for item in planeteer_calls]
    return planeteer_calls 

def long_planeteer_calls():
    pass
def long_planeteer_calls(planeteer_calls):
    value_list = list()
    for i in planeteer_calls:
        if len(i) > 4:
            value_list.append(i)
            break    
        else:
            pass
    return bool(value_list)

def find_the_cheese(food_list):
    cheese_list = ["cheddar", "gouda", "camembert"]
    for item in food_list:
        if item in cheese_list:
                return item
        
        return "No Cheese found"
 
def find_the_cheese(snacks):
    cheeses = ["cheddar", "gouda", "swiss"]  

    for item in snacks:
        if item in cheeses:
            return item  
    return "No cheese found"  

no_cheese_list = ["pretzels", "apple", "banana", "crackers"]
no_cheese_result = find_the_cheese(no_cheese_list)
print(no_cheese_result)  # Output: "No cheese found"
# Example usage:
snack_list = ["pretzels", "apple", "cheddar", "crackers"]
result = find_the_cheese(snack_list)
print(result)  # Output: "cheddar"



    