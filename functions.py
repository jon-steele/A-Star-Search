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

# heuristic returns the straight line distance between two city halls
# This was calculated using google earth
def heuristic(a, b):
    straight_line_distance = [
        [0, 7.8, 12.5, 10.6, 11.4, 21.5, 16.1, 21.8, 38.2, 62, 85, 121.8, 62.8], # Vancouver
        [7.8, 0, 11.2, 11.8, 18.9, 21.7, 17, 26.4, 38.6, 61.6, 83.7, 118, 60], # North Vancouver
        [12.5, 11.2, 0, 21.1, 21.6, 31.9, 27.3, 30.9, 49.3, 72.4, 94.8, 128.7, 71.9], # West Vancouver
        [10.6, 11.8, 21.1, 0, 14.9, 10.5, 6.1, 18.8, 27.8, 51.6, 74.8, 111.9, 50.9], # Burnaby
        [11.4, 18.9, 21.6, 14.9, 0, 21.3, 17.1, 10.5, 35.6, 60, 87, 125, 62.1], # Richmond
        [21.5, 21.7, 31.9, 10.5, 21.3, 0, 4.6, 19.6, 17, 40.4, 65.2, 104.1, 41.17], # Surrey
        [16.1, 17, 27.3, 6.1, 17.1, 4.6, 0, 17.3, 21.4, 45.5, 69.7, 108.3, 45.8], # New Westminister
        [21.8, 26.4, 30.9, 18.8, 10.5, 19.6, 17.2, 0, 28.8, 52.9, 81.9, 121, 56.6], # Delta
        [38.2, 38.6, 49.3, 27.8, 35.6, 17, 21.4, 28.8, 0, 24.7, 51.7, 93.4, 28.1], # Langley
        [62, 61.6, 72.4, 51.6, 60, 40.4, 45.5, 52.9, 24.7, 0, 30, 74.1, 11.8], # Abbotsford
        [85, 83.7, 94.8, 74.8, 87, 65.2, 69.7, 81.9, 51.7, 30, 0, 44.7, 23.6], # Chilliwack
        [121.8, 118, 128.7, 111.9, 125, 104.1, 108.3, 121, 93.4, 74.1, 44.7, 0, 50], # Hope
        [62.8, 60, 71.9, 50.9, 62.1, 41.17, 45.8, 56.6, 28.1, 11.8, 23.6, 50, 0] # Mission
    ]
    return straight_line_distance[a][b]

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