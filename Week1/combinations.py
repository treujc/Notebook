import math
from scipy.misc import comb
from itertools import combinations
from itertools import permutations
from math import factorial
def permu(n, k):
    return factorial(n) / factorial(n - k)

lefthand_beers = ["Milk Stout", "Good Juju", "Fade to Black", "Polestar Pilsner"]
lefthand_beers += ["Black Jack Porter", "Wake Up Dead Imperial Stout","Warrior IPA"]
choices = len(lefthand_beers)
choose = 4

print(comb(choices,choose))

#print(list(combinations('Milk Stout',4)))

print(permu(12,9))
