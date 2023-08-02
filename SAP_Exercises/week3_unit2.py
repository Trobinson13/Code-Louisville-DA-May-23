emoji_dict = {
"happy": "😃",
"heart": "😍",
"rotfl": "🤣",
"smile": "😊",
"crying": "😭",
"kiss": "😘",
"clap": "👏",
"grin": "😁",
"fire": "🔥",
"broken": "💔",
"think": "🤔",
"excited": "🤩",
"boring": "🙄",
"winking": "😉",
"ok": "👌",
"hug": "🤗",
"cool": "😎",
"angry": "😠",
"python": "🐍"
}

string_to_translate = input("Please enter a sentence: ")

# Method 1

# user input string into individual words
words = string_to_translate.split()
# Create empty placeholder for new sentence
translated_words = []

# Loop over every word
for word in words:
    # If lowercase match of "word" is found in emoji_dict, set "translated_word".
    # If not found, sets "translated_word" to default value of word
    translated_word = emoji_dict.get(word.lower(), word)
    translated_words.append(translated_word)

emoji_sentence = " ".join(translated_words)
print(emoji_sentence)

# Method 2
for key, value in emoji_dict.items():
    string_to_translate = string_to_translate.replace(key, value)

print(string_to_translate)
