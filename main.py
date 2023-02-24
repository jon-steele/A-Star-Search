from a_star import path_finder
from path import Path
from functions import number_to_city

print("""
      
    Cities: \n
    0 - Vancouver \n
    1 - North Vancouver \n
    2 - West Vancouver \n
    3 - Burnaby \n
    4 - Richmond \n
    5 - Surrey \n
    6 - New Westminster \n
    7 - Delta \n
    8 - Langley \n
    9 - Abbotsford \n
    10 - Chilliwack \n
    11 - Hope \n
    12 - Mission \n

""")

start = int(input("Input a starting node (0 - 12): "))
goal = int(input("Input an goal node (0 - 12): "))

path = path_finder(start, goal)

for x in path.visited_nodes:
    print(number_to_city(x))