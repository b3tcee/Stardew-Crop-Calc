#GOAL OF PROJECT : Suggest the best crop to plant in Stardew given the season and days

#Creation of Dictionary:
spring_crops = {
    "Parsnip": {"cost": 20,"days": 4, "sales_price": 35},
    "Garlic": {"cost": 40, "days": 4, "sales_price": 60},
    "Kale": {"cost": 70, "days": 6, "sales_price": 110},
    "Potato": {"cost": 50,"days": 6, "sales_price": 80},
    "Strawberry": {"cost": 100,"days": 8, "sales_price": 120},#regrows
    "Jazz": {"cost": 30,"days": 7, "sales_price": 50},
    "Carrot": {"cost": 0,"days": 3, "sales_price": 35},
    "Cauliflower": {"cost": 80,"days": 12, "sales_price": 175},
    "Green Bean": {"cost": 60,"days": 10, "sales_price": 40}, #regrows
    "Rhubarb": {"cost": 100,"days": 13, "sales_price": 220},
    "Tulip": {"cost": 20,"days": 6, "sales_price": 30},
    "Rice Shoot": {"cost": 40,"days": 6, "sales_price": 30},
}
#print(spring_crops["Tulip"]['days'])

#Create a profit function
def calc_profit_per_day(crop_info):
    profit = crop_info["sales_price"] - crop_info["cost"]
    profit_per_day = profit/crop_info["days"]
    return profit_per_day

# #User inputs crop name
def best_crop_name():
    name_crop = input('What crop do you want to plant? ').capitalize()
   
    crop_profit = calc_profit_per_day(spring_crops[name_crop])
    print (f"{name_crop} will give ${crop_profit:.2f} per day")

best_crop_name()

#Variables to track the best crop and best profit
best_crop = ''
best_profit = 0

#Loop runs through and gives a list of all the crops and profits
for crop_name,crop_info in spring_crops.items():
    profit = calc_profit_per_day(crop_info)
    print(f'{crop_name}: ${profit:.2f} per day')
#Tells us the best crop to plant in spring
    if profit > best_profit:
        best_profit = profit
        best_crop = crop_name



print (f"\n The best crop to plant in Spring is {best_crop} with ${best_profit:.2f} per day")
