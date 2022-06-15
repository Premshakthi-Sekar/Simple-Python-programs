def emo(message):
    word=message.split(" ")
    emoji_coverter={
        ":)": " 🙂",
        ":(": "☹",
    }
    output=""
    for ch in word:
        output+= emoji_coverter.get(ch, ch) + " "
    return output


message= input("enter: ")
print(emo(message))
