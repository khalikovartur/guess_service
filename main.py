import random
 
blue = ['Синий'] * 50
green = ['Зеленый'] * 30
red = ['Красный'] * 20
col = red + green + blue
random.shuffle(col)
colors = col
ran_color = random.randint(0, len(colors)-1)
guess = colors[ran_color]

print(colors,guess)