# You are given a string of available characters and a string representing a word or a phrase that you need to generate.
# Write a function that checks if you cab generate required word/phrase using the characters provided.
# If you can, then please return True, otherwise return False.
#
# NOTES:
#     You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
#     than frequency in the document string.
#
# FOR EXAMPLE:
#
#     characters = "cbacba"
#     phrase = "aabbccc"
#
#     In this case you CANNOT create required phrase, because you are 1 character short!
#
# IMPORTANT:
#     The phrase you need to create can contain any characters including special characters, capital letter, numbers
#     and spaces.
#
#     You can always generate an empty string.
#

def generate_phrase(characters, phrase):
    sorted_characters = sorted(characters)
    sorted_characters = ''.join(sorted_characters)

    sorted_phrase = sorted(phrase)
    sorted_phrase = ''.join(sorted_phrase)

    return sorted_characters == sorted_phrase


print(generate_phrase("cbacba", "aabbccc"))

print(generate_phrase("cbacba", "aabbcc"))