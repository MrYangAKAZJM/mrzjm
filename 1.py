import lab05_util

def print_info(restaurant):
    print("{} ({})".format(restaurant[0], restaurant[5]))
    address_parts = restaurant[3].split('+')
    for part in address_parts:
        print("\t{}".format(part))
    avg_score = sum(restaurant[6]) / len(restaurant[6])
    print("Average Score: {:.2f}".format(avg_score))
restaurants = lab05_util.read_yelp('yelp.txt')

# Print details for restaurants 0, 4, and 42
print_info(restaurants[0])
print_info(restaurants[4])
print_info(restaurants[42])
