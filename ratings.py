"""Restaurant rating lister."""


def restaurant_rating(restaurant_file):
    restaurant_info = open(restaurant_file)

    restaurant_ratings_dict = {}

    for line in restaurant_info:
        line = line.rstrip()
        line = line.split(":")

        for restaurant in line:
            restaurant_name = line[0]
            restaurant_rating = line[1]
            restaurant_ratings_dict[restaurant_name] = restaurant_rating

    for restaurant_name, restaurant_rating in restaurant_ratings_dict.items():
        print(f"{restaurant_name} is rated at {restaurant_rating}.")
        #print("{} is rated at {}.".format(restaurant_name, restaurant_rating))

    restaurant_info.close()

restaurant_rating('scores.txt')
