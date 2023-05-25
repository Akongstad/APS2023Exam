import sys


def count_repeated_words(line):
    line = line.strip().replace(" ", "")
    output_lines = []

    for length in range(1, len(line) + 1):
        repeated_words = set()
        for i in range(len(line) - length + 1):
            word = line[i:i+length]
            if word in line[i+1:]:
                repeated_words.add(word)

        if repeated_words:
            output_lines.append(str(len(repeated_words)))
        else:
            output_lines.append("")
            break

    return output_lines


for line in sys.stdin:
    line = line.strip()

    if not line:
        break

    output = count_repeated_words(line)
    for line in output:
        print(line)
