text = ""
with open("raw_text.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        text += line.strip() + " "

text = text.lower().replace("ę", "e").replace("ó", "o").replace("ą", "a").replace("ś", "s").replace("ł", "l").replace("ż", "z").replace("ź", "z").replace("ć", "c").replace("ń", "n").replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("%", "").replace("„", "").replace("”", "").replace(":", "").replace("–", " ").replace("/", " lub ").replace(" – ", " ").replace("-", " ").replace(" - ", " ").replace("&", "")

def remove_brackets(s):
    i = 0
    while i < len(s):
        if s[i] == "(":
            end = -1
            for j in range(i + 1, len(s)):
                if s[j] == ")":
                    end = j
                    break
            if end != -1:
                s = s[:i - 1] + s[j + 1:]
        i += 1
    return s

def normalize_numbers(s: str):
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i + 1

            while j < len(s):
                if s[j].isdigit():
                    j += 1
                elif s[j] == " " and j + j < len(s) and s[j + 1].isdigit():
                    j += 1
                else:
                    break
            s = s[:i] + "0" + s[j:]
        i += 1
    return s


text = " ".join(text.split())
text = remove_brackets(text)
text = normalize_numbers(text)
with open("plaintext.txt", "w", encoding="utf-8") as writer:
    writer.write(text)