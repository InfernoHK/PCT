restaurants = ["taco bell", "buger king", "mr minors new diner"]

new_res = input("what restaurant would you like to rank your list")



def rank_restaurant(new_res, restaurants):
    for i in range(len(restaurants)):
        
        rank = input("do you like A) " + new_res + " more or B) " + restaurants[i] + " more? A/B")
        if rank == "A":
            restaurants.insert(i, new_res)
            break
        elif rank == "B":
            continue

    if new_res not in restaurants:
        restaurants.append(new_res)
        
    return restaurants


print("you new ranking of restaurants", rank_restaurant(new_res, restaurants))