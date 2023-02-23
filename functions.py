# cost returns the minimum distance between the two city halls
def cost(a, b):
    cost = [
        [0, 16.1, 17.4, 11.6, 14.2, 27.2, 18, 23.3, 44.3, 65.2, 100, 150, 71.9], # Vancouver
        [16.1, 0, 12.6, 15.3, 28.7, 32.5, 23.3, 35.1, 48.1, 69, 104, 154, 77.5], # North Vancouver
        [17.4, 12.6, 0, 26.5, 30.6, 42.1, 37, 39.8, 62.2, 80.1, 115, 165, 86.8], # West Vancouver
        [11.6, 15.3, 26.5, 0, 21.6, 13.4, 6.9, 28.5, 32.9, 54.4, 89.2, 139, 61.1], # Burnaby
        [14.2, 28.7, 30.6, 21.6, 0, 28.8, 22.6, 15.4, 44.5, 72.1, 107, 157, 86.2], # Richmond
        [27.2, 32.5, 42.1, 13.4, 28.8, 0, 7.1, 26.3, 18, 41.9, 76.7, 127, 53.4], # Surrey
        [18, 23.3, 37, 6.9, 22.6, 7.1, 0, 27.1, 27.4, 49.6, 84.4, 134, 59.8], # New Westminister
        [23.3, 35.1, 39.8, 28.5, 15.4, 26.3, 27.1, 0, 37, 59.9, 94.7, 148, 71.1], # Delta
        [44.3, 48.1, 62.2, 32.9, 44.5, 18, 27.4, 37, 0, 26.4, 62.4, 112, 38.8], # Langley
        [65.2, 69, 80.1, 54.4, 72.1, 41.9, 49.6, 59.9, 26.4, 0, 37.2, 87.1, 17.5], # Abbotsford
        [100, 104, 115, 89.2, 107, 76.7, 84.4, 94.7, 62.4, 37.2, 0, 52.5, 46.5], # Chilliwack
        [150, 154, 165, 139, 157, 127, 134, 148, 112, 87.1, 52.5, 0, 81.1], # Hope
        [71.9, 77.5, 86.8, 61.1, 86.2, 53.4, 59.8, 71.1, 38.8, 17.5, 46.5, 81.1, 0] # Mission
    ]
    return cost[a][b]

# heuristic returns the heuristic value between two city halls
def heuristic(a, b):
    return 0

# number_to_city converts an integer to a city name, as cities are stored as indices
def number_to_city(x):
    match x:
        case 0:
            return "Vancouver"
        case 1:
            return "North Vancouver"
        case 2:
            return "West Vancouver"
        case 3:
            return "Burnaby"
        case 4:
            return "Richmond"
        case 5:
            return "Surrey"
        case 6:
            return "New Westminster"
        case 7:
            return "Delta"
        case 8:
            return "Langley"
        case 9:
            return "Abbotsford"
        case 10:
            return "Chilliwack"
        case 11:
            return "Hope"
        case 12:
            return "Mission"