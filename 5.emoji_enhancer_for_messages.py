

# get a dictionary of emojis and their corresponding unicode characters
emoji_map_function = {
    "happy": "😄",
    "sad": "😢",
    "love": "❤️",
    "thumbs_up": "👍",
    "laughing": "😂",
    "wink": "😉",
    "crying": "😭",
    "angry": "😠",
    "surprised": "😮",
    "cool": "😎",
    "code": "👨‍💻",
    "tea": "🍵",
    "coffee": "☕",
    "party": "🎉",
    "music": "🎵",
    "sun": "☀️",
    "moon": "🌙",
    "star": "⭐",
    "food": "🍔",
}

# get user input for a message
input_message = input("Enter a message: ")

updated_words = []
#process each word
for word in input_message.split():
    clean_word = word.strip(".,!?;:()\"'")  # remove punctuation
    if clean_word in emoji_map_function:
        updated_words.append(f"{word} {emoji_map_function[word]} ")
    else:
        updated_words.append(word)

# join the updated words into a new message
updated_message = " ".join(updated_words)
print("Enhanced message with emojis:")
print(updated_message)