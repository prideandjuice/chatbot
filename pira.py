import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what's your name ?",
        ["I am a chatbot created for you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good, how about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "Alright :)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, so I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse.",]
    ],
    [
        r"(.*) created ?",
        ["I was created by a user as a project",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm in the cloud.",]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is awesome like always.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]

def chatbot():
    print("Hi, I'm your chatbot.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
