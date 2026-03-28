
'''

Завдання 2
Напишіть програму, яка аналізує файл log.txt, визначає 10
найпоширеніших слів, що зустрічаються найчастіше, і записує їх
разом з їхньою частотою в word_stats.txt.

'''
text = ""

def analyze_log():
    try:
        with open("log.txt", "r", encoding="utf-8") as f:
            text = f.read().lower()
    except FileNotFoundError:
        file = open("log.txt", "a")
        file.close()
    words = text.split(" ")

    word_count = {}

    for word in words:
        if word == "":
            continue
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    top_10 = sorted_words[:10]

    with open("word_stats.txt", "w", encoding="utf-8") as f:
        for word, count in top_10:
            f.write(f"{word}: {count}\n")

if __name__ == "__main__":
    analyze_log()