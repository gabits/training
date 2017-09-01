def presses(phrase):
    sum_of_presses = 0
    keypresses = (
                      (['1', 'a', 'd', 'g', 'j', 'm', 'p', 't', 'w', '*', ' ', '#'], 1),
                      (['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x', '0'], 2),
                      (['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y'], 3),
                      (['2', '3', '4', '5', '6', 's', '8', 'z'], 4),
                      (['7', '9'], 5),
    )
    for letter in phrase:
        print(letter)
        for characters in keypresses:
            print(characters[0])
            if letter in characters[0]:
                print(int(keypresses[characters])
                sum_of_presses += int(keypresses[characters])
    return sum_of_presses
