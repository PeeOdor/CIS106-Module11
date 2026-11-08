# Module 11 Problem 4 - Bowling average and average with handicap

def compute_bowling(game1, game2, game3, handicap):
    average = (game1 + game2 + game3) / 3
    average_with_handicap = average + handicap
    return average, average_with_handicap

last_name = input("Enter bowler's last name: ")
game1 = int(input("Enter game 1 score: "))
game2 = int(input("Enter game 2 score: "))
game3 = int(input("Enter game 3 score: "))
handicap = int(input("Enter handicap: "))

average, average_with_handicap = compute_bowling(game1, game2, game3, handicap)

print("Last name:                 ", last_name)
print("Average score:             ", format(average, ".1f"))
print("Average with handicap:     ", format(average_with_handicap, ".1f"))