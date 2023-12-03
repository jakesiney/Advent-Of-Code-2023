test_input = ["Game 1: 1 green, 1 blue, 1 red; 1 green, 8 red, 7 blue; 6 blue, 10 red; 4 red, 9 blue, 2 green; 1 green, 3 blue; 4 red, 1 green, 10 blue"]


games_colour_count = {}


def get_bags_count(games):
    for line in games:
        parts = line.split(":")
        game_id = parts[0].strip()
        colours = parts[1].replace(";", ",").split(",")

        if game_id not in games_colour_count:
            games_colour_count[game_id] = {}

        for colour_count in colours:
            print(f"Processing: {colour_count}")  # Debug
            count, colour = colour_count.strip().split()
            print(f"Colour: {colour}, Count: {count}")  # Debug
            if colour not in games_colour_count[game_id]:
                games_colour_count[game_id][colour] = 0
            games_colour_count[game_id][colour] += int(count)

    return games_colour_count


with open("Day-2/input.txt", "r") as file:
    games = file.readlines()


print(get_bags_count(test_input))
