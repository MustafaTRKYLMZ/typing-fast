import time

print("Welcome to the typing test!")
print("You have 180 seconds to type the following text:")

text = (
    "This is a typing test designed to improve your typing speed and accuracy. "
    "Typing tests are a great way to practice typing and challenge yourself to be faster and more precise. "
    "In this test, you will have to type the text as accurately as you can within the given time limit. "
    "Mistakes will be counted, and your accuracy will be calculated based on the total number of words. "
    "Typing quickly is an essential skill in today's digital age, whether you are sending emails, writing reports, or chatting with friends. "
    "Good typing skills can help you save time and increase your productivity. "
    "Accuracy is just as important as speed; practice makes perfect. "
    "The more you practice, the better your typing skills will become. "
    "Keep an eye on the clock and try to type as quickly as possible without making too many mistakes. "
    "This test is also an opportunity to learn new words and phrases. "
    "Focus on the text and avoid distractions. "
    "Typing can be a fun and rewarding skill to develop. "
    "Are you ready to take on the challenge? "
    "Start typing now and aim for 90 correct words to win. "
    "Don't worry if you don't achieve it on your first attempt; practice regularly, and you will see improvement!"
)

print("\n" + text + "\n")

start_time = time.time()

correct_words = 0
incorrect_words = 0

typed_text = input("Start typing: ")

end_time = time.time()
elapsed_time = int(end_time - start_time)
print("\nElapsed time:", elapsed_time, "seconds")

if elapsed_time > 180:
    print("\nTime's up! You didn't finish in time.")
else:
    text_words = text.split()
    typed_words = typed_text.split()

    if len(typed_words) == 0:
        print("\nYou didn't type anything!")
    else:
        for i in range(len(typed_words)):
            if i < len(text_words) and typed_words[i] == text_words[i]:
                correct_words += 1
            else:
                incorrect_words += 1

print("\nTyping test is over!")
print("You typed:", typed_text)
print("Correct words:", correct_words)
print("Incorrect words:", incorrect_words)
print("Total words in the text:", len(text.split()))
print("Accuracy:", correct_words / len(text.split()) * 100, "%")

print("\n")
print("\n" + "***" * 10 + "\n")
if correct_words >= 90:
    print("You won!")
else:
    print("Don't give up, next time will be better")
print("\n" + "====" * 10 + "\n")
