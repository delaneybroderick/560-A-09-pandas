# https://goheels.com/sports/mens-basketball/roster

import pandas as pd 

player = {"Last name": ["Bacot", "Davis","Cadeau", "Claude", "Tyson", "Trimble","Powell", "Jackson", "Washington", "Hawkins", "Holbrook", "Lubin", "Withers", "Mayo Jr."],
          "First Name": ["Armandoo", "RJ", "Elliot", "Ty", "Cade", "Seth", "Drake", "Ian", "Jalen", "Russell", "John", "Ven-Allen", "Jae'Lyn", "Dante"],
          "height": [83, 72, 73, 73, 79, 75, 76, 74, 82, 71, 78, 78, 79, 71],
          "weight":[240, 180, 180, 251, 200, 195, 195, 190, 235, 175, 230, 230, 220, 175]}
data = pd.DataFrame(player)

#bmi = weight in kg/height in meters squared
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)

data["bmi"] = data["bmi"].round(2)
print(data)

data.to_csv("bmi.cvs")