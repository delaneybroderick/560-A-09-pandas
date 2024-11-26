# https://goheels.com/sports/mens-basketball/roster

import pandas as pd 
roster = ["Bacot", "Davis","Cadeau"]
player = {"Last name": roster}
data = pd.DataFrame(player)
print(data)

roster = ["Bacot", "Davis", "Cadaeu"]
for player in roster:
    print (roster)