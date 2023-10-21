#學生總分為300
#有些學生可以加分5%
#如果加分超過300，就以300為準

import pyinputplus as pyip

scores = pyip.inputInt("請輸入學生分數(最高300分):", min=0, max=300)
print(scores)
isYes = pyip.inputMenu(["y","n"],prompt="學生是否符合加分條件(請選擇1或2)?\n",numbered=True)

if isYes == "y":
    scores *= 1.05
    if scores > 300:
        scores = 300
    
print(f"學生分數為{scores}")
