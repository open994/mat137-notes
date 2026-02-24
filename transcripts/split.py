import json

d: dict[str, list[str]]
with open('transcripts.json') as f:
    d = json.load(f)

for chapter in d:
    i = 1
    for content in d[chapter]:
        formatted = chapter.replace('Chapter ', '')
        with open(f'txt/{formatted}.{i}.txt', 'w') as f:
            f.write(content)
        i += 1