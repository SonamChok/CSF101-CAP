################################
# Sonam Choki
# 1ME
# 0230272
################################
# REFERENCES
# https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/
# https://stackoverflow.com/questions/51467707/simplify-python-code-rock-paper-scissors
# the problem
# http://link.to.an.article/video.com
################################
# SOLUTION
# Your Solution Score:
# 49801

################################
# Read the input.txt file
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        game_rounds = [(line.strip().split()[0], line.strip().split()[1]) for line in lines]
    return game_rounds

# Calculate the score based on the rules
def calculate_score(game_rounds):
    total_points = 0
    for round in game_rounds:
        opponent_choice, desired_outcome = round
        if desired_outcome == 'Z':
            # You need to win
            if opponent_choice == 'A':
                total_points += 2 + 6  # Paper defeats Rock
            elif opponent_choice == 'B':
                total_points += 3 + 6  # Scissors defeats Paper
            elif opponent_choice == 'C':
                total_points += 1 + 6  # Rock defeats Scissors
        elif desired_outcome == 'Y':
            # You need to draw
            if opponent_choice == 'A':
                total_points += 1 + 3 
            elif opponent_choice == 'B':
                total_points += 2 + 3  
            elif opponent_choice == 'C':
                total_points += 3 + 3  
        elif desired_outcome == 'X':
            # You need to lose
            if opponent_choice == 'A':
                total_points += 3 + 0  # Rock defeats Scissors
            elif opponent_choice == 'B':
                total_points += 1 + 0  # Paper defeats Rock
            elif opponent_choice == 'C':
                total_points += 2 + 0  # Scissors defeats Paper

    print("The total score is:", total_points)

# Running the code
if __name__ == "__main__":
    game_rounds = read_input("input_2_cap1.txt")
    calculate_score(game_rounds)
