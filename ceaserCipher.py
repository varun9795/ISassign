from collections import defaultdict

def frqAttack(Cc):
    # Converting the string to uppercase to avoid any snag in frequency attack
    N, S = (len(Cc), Cc.upper())

    # List to store the top plain texts
    Text = []              

    # storing the english letters in their decreasing order of frequency
    frequency_of_letter = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # dictionary to store frequency of the letters in cipher text  
    frequency = defaultdict(int)    

    # calculating the frequency of the letters in cipher text
    for c in Cc: frequency[c] += 1

    
    # Sorting frequency and storing it in a tuple
    sorted_frequency = tuple(sorted(frequency.items(), key = lambda i: i[1], reverse=True))


    for i in range(26):
        # calculating the key
        key = (26 + ord(sorted_frequency[0][0]) - ord(frequency_of_letter[i])) % 26
        txt = ""

        # time complexity : O(26 * N)
        for j in range(len(Cc)):
            # traversing on string and decoding it
            if(Cc[j] >= 'A' and Cc[j] <= 'Z'):
                txt += chr(65 + (ord(Cc[j]) - 65 + key) % 26)
            else: 
                txt += Cc[j]

        Text.append(txt)

    return Text

# S = input("Enter encoded string: ")
pt = int(input("Enter Number of plain texts you want (max: 26): "))

Cc = "ka hshsk okuhba unyds yus akla lopams fgaht dhbhjk jbnxhgg rrdsdr lkkkkeh dhbdh bggsa ovsta mkdjdj"

# calling the function to get plaintexts
Text = frqAttack(Cc)

print("\n\nPLAIN TEXTs AFTER DECODING:\n")
# printing the plaintexts
for i in range(pt % 26):
    print( i + 1, end = ": ")
    print( Text[i], end = "\n\n")