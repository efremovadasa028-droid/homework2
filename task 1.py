s = "Дом, в котором мы живём, — это не просто дом. В доме живут люди, и люди эти делают дом домом. Без людей дом — просто стены, а стены без дома и без людей — уже не дом, а коробка."
words = s.lower().split()

for i in range(len(words)):
    if len(words[i]) > 1 and not words[i][-1].isalpha():
        words[i] = words[i][:-1]

for word in words:
    if len(word) == 1 and not word.isalpha(): words.remove(word)

groups = {}
for w in words:
    key = w
    if key not in groups:
        groups[key] = 0
    groups[key] += 1
print(f"Общее количество слов в тексте - {len(words)}, количество уникальных слов - {len(groups)}")

ans = []
count = 0
for word in sorted(groups.items(), key = lambda item: item[1], reverse = True):
    ans.append((word[0], word[1]))
    count += 1
    if count == 5: break
print("Топ-5 слов:", *ans)

ma = 0
for word in words:
    ma = max(len(word), ma)
for word in words:
    if len(word) == ma:
        print(f"Самое длинное слово: {word}")
        break

groups = {}
for word in words:
    key = len(word)
    if key not in groups:
        groups[key] = 0
    groups[key] += 1
print(dict(sorted(groups.items())))