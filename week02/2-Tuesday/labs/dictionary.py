# 1. Create a dictionary called zodiac with the following inforation.
# Each key is the name of the zodiac
# zodiac = {
#     'Aries': 'The Warrior',
#     'Taurus': 'The Builder',
#     'Gemini': 'The Messenger',
#     'Cancer': 'The Mother',
#     'Leo': 'The King',
#     'Virgo': 'The Analyst',
#     'Libra': 'The Judge',
#     'Scorpio': 'The Magician',
#     'Sagittarius': 'The Gypsy',
#     'Capricorn': 'The Father',
#     'Aquarius': 'The Thinker',
#     'Pisces': 'The Mystic'
# }

# Aries - The Warrior
# Taurus - The Builder
# Gemini - The Messenger
# Cancer - The Mother
# Leo - The King
# Virgo -The Analyst
# Libra - The Judge
# Scorpio - The Magician
# Sagittarius - the Gypsy
# Capricorn - the Father
# Aquarius - The Thinker
# Pisces - TheMystic


# 1a. Retrieve information about your zodiac from the zodiac dictionary

# 2. Given the following dictionary

# phonebook_dict = {
#     'Alice': '703-493-1834',
#     'Bob': '857-384-1234',
#     'Elizabeth': '484-584-2923'
# }


# phonebook_dict["Kareem"] : "938-489-1234"
# # 2a. Print Elizabeth's phone number
# elizabeth= phonebook_dict['Elizabeth']
# print(elizabeth)
# 2b. Add a entry to the dictionary: Kareem's number is 938-489-1234.
# 2c. Delete Alice's phone entry.
# 2d. Change Bob's phone number to '968-345-2345'.
# 2e. Print all the phone entries.


# 3. Nested dictionaries

# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [
#         {
#             'name': 'Jasmine',
#             'email': 'jasmine@yahoo.com',
#             'interests': ['photography', 'tennis']
#         },
#         {
#             'name': 'Jan',
#             'email': 'jan@hotmail.com',
#             'interests': ['movies', 'tv']
#         }
#     ]
# }
# # 3a. Write a python expression that gets the email address of Ramit.
# ramit_email = ramit['email']
# print(ramit_email)
# # 3b. Write a python expression that gets the first of Ramit's interests.
# ramit_interest = ramit['interests'][0]
# print(ramit_interest)
# # 3c. Write a python expression that gets the email address of Jasmine.
# jasmine = ramit['friends'][0]['email']
# print(jasmine)
# # 3d. Write a python expression that gets the second of Jan's two interests.
# jan = ramit['friends'][1]['interests'][1]
# print(jan)

# 4. Letter Summary
# Write a letter_histogram function that takes a word as its input,
# and returns a dictionary containing the tally of how many times
# each letter in the alphabet was used in the word. For example:

# >>>letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}
# string = input('Input a word: ')
# def histogram(string):
#     freq = {}
#     for i in string: 
#         freq[i] = freq.get(i, 0) + 1
#     return freq

# print(histogram(string))

# Word Summary
# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each word in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to
