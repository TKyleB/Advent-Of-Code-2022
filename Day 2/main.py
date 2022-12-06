from pathlib import Path

def calculate_move_score(move):
    match move:
        case "X":
            return 1
        case "Y":
            return 2
        case "Z":
            return 3

def calculate_game_score(opponent_move, your_move):
    def convert_to_standard(move):
        match move:
            case "X": return "A"
            case "Y": return "B"
            case "Z": return "C"

    converted_move = convert_to_standard(your_move)

    # Draw
    if opponent_move == converted_move: return 3
    # Win
    elif opponent_move == "A" and converted_move == "B": return 6
    elif opponent_move == "B" and converted_move == "C": return 6
    elif opponent_move == "C" and converted_move == "A": return 6
    # Lose
    else:
        return 0

def calculate_move(opponent_move, desired_result):
    match desired_result:
        # Lose
        case "X":
            if opponent_move == "A": return "Z"
            if opponent_move == "B": return "X"
            if opponent_move == "C": return "Y"
        # Draw
        case "Y":
            if opponent_move == "A": return "X"
            if opponent_move == "B": return "Y"
            if opponent_move == "C": return "Z"
        # Win
        case "Z":
            if opponent_move == "A": return "Y"
            if opponent_move == "B": return "Z"
            if opponent_move == "C": return "X"

def main_part_2():
    result_score = 0
    file_path = Path(__file__).with_name("input.txt")
    with open(file_path) as f:
        for line in f:
            opponent_move, desired_result = line.strip().split(" ")
            your_move = calculate_move(opponent_move, desired_result)
            result_score += calculate_move_score(your_move) + calculate_game_score(opponent_move, your_move)
    print(f"The final score is {result_score}")
    

main_part_2()