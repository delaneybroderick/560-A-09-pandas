# https://goheels.com/sports/mens-basketball/roster

import pandas as pd 

player = {"Last name": ["Bacot", "Davis","Cadeau"],
          "First Name": ["Armandoo", "RJ", "Elliot"],
          "height": [83, 72, 73],
          "weight":[240, 180, 180]}
data = pd.DataFrame(player)
print(data)

roster = ["Bacot", "Davis", "Cadaeu"]
for player in roster:
    print (roster)