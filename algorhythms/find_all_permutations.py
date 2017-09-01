"""
Write an algorithms that generates all permutations of the string
'abcdefghklmnopqrstuvwxyz0123456789'
As it's permutation, order is important.
ref. https://brilliant.org/wiki/permutations-with-repetition/
"""


"""
1. Permutate all positions for string[x]
2. Permutate all positions for string[x+1:x+n] through all of a's permutations
3. Cumulative permutation will cover all of them including all repetitions
4. Remove all repetitions? = Unefficient.
5. Something is failing in the algorithm when permutating the second for the
first ones because it's returning 4 repetitions for 4 letters!
"""

# def permutate_a(string):
#     for string[0]:
#

####

def receive(string):
    permutations_dict = {'original_string': [string, ]}            # used for the results to interate through
    for character in string:
        perm_list = []
        for permutations in permutations_dict.values():         # accesses the list of lists
            for permutation in permutations:            # accesses each permutation within each of the lists
                # now it should do actually the permutation for each character
                # e.g. 'bcdefghijkAlmnopqrstuvwxyz0123456789'
                for char in permutation:            # maybe I should use range iteration to make this part more optmised
                    if permutation.index(char) > string.index(character):
                        # if char not index
                        new_permutation = list(permutation)
                        index = new_permutation.index(char)
                        new_permutation.remove(character)
                        new_permutation.insert(index, character)
                        new_permutation = ''.join(new_permutation)
                        perm_list.append(new_permutation)
                    else:
                        pass
        permutations_dict[character] = perm_list
    return permutations_dict


def test_receive(dict_of_strings):
    test_list = []
    errors = {}
    for lists in dict_of_strings.values():
        for string in lists:
            if string in test_list:
                if string in errors.keys():
                    errors[string] += 1
                else:
                    errors[string] = 2           # means that occurs twice at least
            else:
                test_list.append(string)
    print("{} duplicates found.".format(len(errors)))
    if len(errors) > 0:
        print(errors)


# assert equal {'bdgw': 2, 'abc': 3} and test_receive({'a': ['abc'], 'b':['abc'], 'c':['bdgw'], 'd': ['abc'], 'e':['bdgw']})

dict_of_strings = receive(str(input('type str: ')))
test_receive(dict_of_strings)




"""
        permutar a por todos
        [bacde...]
        permutar b todos os as permutados menos o indice de a
        b quer se permutar pela lista 1 e por todas as listas geradas por a
        [acade...]
        permutar c todos os as e bs permutados menos o inidice de a e b

        pode ser um dicionario
        pelo qual a chave eh o a e o valor sao as strings permutadas

para cada valor no dicionario vc se permutara por tudo menos pelos ultimos n (dois) q foram permutados primeiro
dict = {a[or index]: ['bacdef...', 'bcadef...', 'bcdaef'...],
pular 'abcdef'    b: ['acbdef...', 'acebdf...', 'acedfb...'               # PULE abcdef (a primeira n - 1 (b idex))
                      'cbadef...' , 'cabdef', 'cadbef'
                      'cbdaef', 'cdbaef', 'cdabef']
                  c: ['']               # 1a permuts c a ja acontece,  2a permuts c a ja acontece


"""
