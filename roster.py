# https://goheels.com/sports/mens-basketball/roster

import pandas as pd 

roster = ["Bacot", "Davis","Cadeau"]
player = {"Last name": roster,
          "First Name": ["Armandoo", "RJ", "Elliot"],
          "height": [240, 180, 180]}
data = pd.DataFrame(player)
print(data)

roster = ["Bacot", "Davis", "Cadaeu"]
for player in roster:
    print (roster)