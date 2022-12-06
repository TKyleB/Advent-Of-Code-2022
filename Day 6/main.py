from pathlib import Path

file_path = Path(__file__).with_name("input.txt")
with open(file_path) as f:
    signal_found = False
    data = f.readline()
    start = 0
    end = 14
    while not signal_found:
        sequence = set(data[start:end])
        if len(sequence) == 14:
            signal_found = True
            print(f"The signal found was: {data[start:end]}")
            print(f"This occured after {end} characters")
        else:
            start += 1
            end += 1
