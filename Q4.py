from collections import defaultdict
from itertools import permutations

def frequencyAttack(S):
    # calculating the length of string & converting the string to uppercase to avoid any snag in frequency attack
    N, S = (len(S), S.upper())

    # List to store the top plain texts
    plaintext = []

    
    frequency = defaultdict(int)    # dictionary to store frequency of letters

    # calculating the frequency of the letters in cipher text
    for c in S:
        if(c >= 'A' and c <= 'Z'):
            frequency[c] += 1

    # storing the english letters in their decreasing order of frequency
    english_letter_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # generating top permutations
    ch = len(frequency)
    permute = english_letter_frequency = english_letter_frequency[:ch]

    # this will generate top 720 permuatatons based on the english letter frequency trends
    if(ch>6):
        permute = english_letter_frequency[-6:]
        toppermutations = [english_letter_frequency[:-6] + ''.join(perm) for perm in tuple(permutations(permute))]
    else:
        toppermutations = [''.join(perm) for perm in tuple(permutations(permute))]

    # Sorting frequency and storing it in a tuple
    sorted_frequency = tuple(sorted(frequency.items(), key = lambda i: i[1], reverse=True))

    # using top permutations string will be decoded
    for perm in toppermutations:
        txt = ['' for _ in range(N)]

        pointer = 0
        # time complexity : O(26 * N)
        for char, freq in sorted_frequency:
            # traversing on string and decoding it
            for j in range(len(S)):
                if(S[j] == ' '):
                    txt[j] = ' '
                elif(S[j] == char):
                    txt[j] = perm[pointer]

            pointer += 1

        plaintext.append(''.join(txt))

    return plaintext

# The program will work best if the length of the encoded string is large
S = input("Enter encrypted string: ")
pt = 10 # as given in requirement

# calling the function to get plaintexts
plaintext = frequencyAttack(S)

print("\n\nDecrypted PLAIN TEXTS:\n")
# printing the plaintexts
for i in range(pt % 720):
    print( i + 1, ": ", plaintext[i], end = "\n\n")