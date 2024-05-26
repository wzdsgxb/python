# bounce.py
#
# Exercise 1.5
height = 100
rebound = 0.6
for i in range(10):
    height = height * rebound
    print(i + 1, round(height, 4))