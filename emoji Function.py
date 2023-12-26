def convert_2emoji(msg):
    message= msg
    output=""
    word=message.split()
    for words in word:
        output += emoji.get(words,words) + " "
    return output


emoji={
        ":)" : "😂",
        ":(" : "😞"
        }
msg=input("please enter a message with emoji's")
kava=convert_2emoji(msg)
print(kava)

