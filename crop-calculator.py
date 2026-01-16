#GOAL OF PROJECT : Suggest the best crop to plant in Stardew given the season and days

#Creation of Dictionary:
spring_crops = {
    "Parsnip": {"cost": 20,"days": 4, "sales_price": 35},
    "Garlic": {"cost": 40, "days": 4, "sales_price": 60},
    "Kale": {"cost": 70, "days": 6, "sales_price": 110},
    "Potato": {"cost": 50,"days": 6, "sales_price": 80},
    "Strawberry": {"cost": 100,"days": 8, "sales_price": 120}
}
#Create a profit function
def calc_profit_per_day(crop_info):
    profit = crop_info["sales_price"] - crop_info["cost"]
    profit_per_day = profit/crop_info["days"]
    return profit_per_day

#Test
crop_profit = calc_profit_per_day(spring_crops["Kale"])
print(crop_profit)