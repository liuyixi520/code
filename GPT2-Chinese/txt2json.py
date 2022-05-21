import json

dic = {}
with open("train.txt", "r", encoding="utf8") as f:
    merge_line = ""
    for line in f:
        line = line.strip()
        merge_line += line
        if len(merge_line) > 500:
            dic[merge_line] = 1
            merge_line = ""

with open("./data/train.json", "w", encoding="utf8") as f:
    json.dump(dic, f, ensure_ascii=False)
