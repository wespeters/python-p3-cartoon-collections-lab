def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, start=1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [f"{call.capitalize()}!" for call in planeteer_calls]

def long_planeteer_calls(planeteer_calls):
    return any(len(call) > 4 for call in planeteer_calls)

def find_the_cheese(cheese_list):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in cheese_list:
        if item in cheeses:
            return item
    return None
