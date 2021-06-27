def malfunctioning_keyboard(data):
    total = 0
    adjacent_keys = {}
    for element in range(0, len(data) - 1):
        if data[element] == 'Q' or data[element] == 'q':
            adjacent_keys = {1: 1, 2: 1, 'w': 1, 'a': 1}
        if data[element] == 'W' or data[element] == 'w':
            adjacent_keys = {'q': 1, 's': 1, 'e': 1, 2: 1}
        if data[element] == 'E' or data[element] == 'e':
            adjacent_keys = {'w': 1, 'd': 1, 'r': 1, 3: 1}
        if data[element] == 'R' or data[element] == 'r':
            adjacent_keys = {'e': 1, 'f': 1, 't': 1, 4: 1}
        if data[element] == 'T' or data[element] == 't':
            adjacent_keys = {'r': 1, 'g': 1, 'y': 1, 5: 1}
        if data[element] == 'Y' or data[element] == 'y':
            adjacent_keys = {'t': 1, 'h': 1, 'u': 1, 6: 1}
        if data[element] == 'U' or data[element] == 'u':
            adjacent_keys = {'y': 1, 'j': 1, 'i': 1, 7: 1}
        if data[element] == 'I' or data[element] == 'i':
            adjacent_keys = {'u': 1, 'k': 1, 'o': 1, 8: 1}
        if data[element] == 'O' or data[element] == 'o':
            adjacent_keys = {'i': 1, 'l': 1, 'p': 1, 9: 1}
        if data[element] == 'P' or data[element] == 'p':
            adjacent_keys = {'o': 1, "'": 1, '[': 1, 0: 1}

        if data[element] == 'A' or data[element] == 'a':
            adjacent_keys = {'q': 1, 's': 1, 'z': 1}
        if data[element] == 'S' or data[element] == 's':
            adjacent_keys = {'a': 1, 'w': 1, 'd': 1, 'x': 1}
        if data[element] == 'D' or data[element] == 'd':
            adjacent_keys = {'s': 1, 'e': 1, 'c': 1, 'f': 1}
        if data[element] == 'F' or data[element] == 'f':
            adjacent_keys = {'d': 1, 'r': 1, 'g': 1, 'v': 1}
        if data[element] == 'G' or data[element] == 'g':
            adjacent_keys = {'f': 1, 't': 1, 'h': 1, 'b': 1}
        if data[element] == 'H' or data[element] == 'h':
            adjacent_keys = {'g': 1, 'y': 1, 'j': 1, 'n': 1}
        if data[element] == 'J' or data[element] == 'j':
            adjacent_keys = {'h': 1, 'u': 1, 'k': 1, 'm': 1}
        if data[element] == 'K' or data[element] == 'k':
            adjacent_keys = {'j': 1, 'i': 1, 'l': 1, ",": 1}
        if data[element] == 'L' or data[element] == 'l':
            adjacent_keys = {'k': 1, 'o': 1, ';': 1, '.': 1}

        if data[element] == 'Z' or data[element] == 'z':
            adjacent_keys = {'a': 1, 'x': 1}
        if data[element] == 'X' or data[element] == 'x':
            adjacent_keys = {'z': 1, 's': 1, 'c': 1}
        if data[element] == 'C' or data[element] == 'c':
            adjacent_keys = {'x': 1, 'd': 1, 'v': 1}
        if data[element] == 'V' or data[element] == 'v':
            adjacent_keys = {'c': 1, 'f': 1, 'b': 1}
        if data[element] == 'B' or data[element] == 'b':
            adjacent_keys = {'v': 1, 'g': 1, 'n': 1}
        if data[element] == 'N' or data[element] == 'n':
            adjacent_keys = {'b': 1, 'h': 1, 'm': 1}
        if data[element] == 'M' or data[element] == 'm':
            adjacent_keys = {'n': 1, 'j': 1, 'k': 1, ',': 1}
        total = total + adjacent_keys.get(data[element + 1], 0)
    return total


if __name__ == '__main__':
    Sentence_One = 'Qwuality isd mucxh bettedr than quanmtity. Oine homke run is much bvetter than two doubnles'
    Sentence_Two = 'Quality is much better than quantity. One home run is much better than two doubles'
    score_a = malfunctioning_keyboard(Sentence_One)
    score_b = malfunctioning_keyboard(Sentence_Two)
    print(score_a)
    print(score_b)
    if score_a > score_b:
        print("The first sentence is more likely to be an incorrect sentence")
    if score_a < score_b:
        print("The second sentence is more likely to be an incorrect sentence")
    if score_a == score_b:
        print("Both sentences have the same probability to be incorrect")
