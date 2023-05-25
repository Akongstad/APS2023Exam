import sys


def count_repeated_words(line):  # Count repeated words in line
    output_lines = []  # Output lines

    for length in range(1, len(line) + 1):  # Iterate through all possible lengths
        repeated_words = set()  # Set of repeated words
        # Iterate through all possible starting indices
        for i in range(len(line) - length + 1):
            word = line[i:i+length]  # Get word
            if word in line[i+1:]:  # If word is repeated
                repeated_words.add(word)  # Add word to set of repeated words

        if repeated_words:  # If there are repeated words
            # Append count of repeated words
            output_lines.append(str(len(repeated_words)))
        else:  # If there are no repeated words
            output_lines.append("")  # Append empty line
            break

    return output_lines  # Return output lines


for line in sys.stdin:
    line = line.strip().replace(" ", "")  # Remove spaces

    if not line:  # If line is empty
        break  # Break

    output = count_repeated_words(line)  # Count repeated words
    for line in output:  # Iterate through output lines
        print(line)  # Print line
