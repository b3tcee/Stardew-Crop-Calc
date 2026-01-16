#GOAL OF PROJECT : Suggest the best crop to plant in Stardew given the season and days

#Creation of Dictionary:
spring_crops = {
    "Parsnip": {"cost": 20,"days": 4, "sales_price": 35},
    "Garlic": {"cost": 40, "days": 4, "sales_price": 60},
    "Kale": {"cost": 70, "days": 6, "sales_price": 110},
    "Potato": {"cost": 50,"days": 6, "sales_price": 80},
    "Strawberry": {"cost": 100,"days": 8, "sales_price": 120},
    "Jazz": {"cost": 30,"days": 7, "sales_price": 50},
    "Carrot": {"cost": 0,"days": 3, "sales_price": 35},
    "Cauliflower": {"cost": 80,"days": 12, "sales_price": 175},
    "Green Bean": {"cost": 60,"days": 10, "sales_price": 40},
    "Rhubarb": {"cost": 100,"days": 13, "sales_price": 220},
    "Tulip": {"cost": 20,"days": 6, "sales_price": 30},
    "Rice Shoot": {"cost": 40,"days": 6, "sales_price": 30},
}

#Create a profit function
def calc_profit_per_day(crop_info):
    profit = crop_info["sales_price"] - crop_info["cost"]
    profit_per_day = profit/crop_info["days"]
    return profit_per_day

#Test
#crop_profit = calc_profit_per_day(spring_crops["Rice Shoot"])
#print(crop_profit)

#Testing for loop
for crop_name,crop_info in spring_crops.items():
    profit = calc_profit_per_day(crop_info)
    print(f'{crop_name}: ${profit:.2f} per day')