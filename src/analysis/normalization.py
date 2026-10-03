def normalize_for_ngrams(raw_text: str):
     text = ""
     for c in raw_text.lower():
          if c.isspace():
               text += " "
          elif ("a" <= c and c <= "z") or ("0" <= c and c <= "9"):
               text += c
     text = normalize_numbers(text)
     return text

def join_multiple_lines(lines: list[str]):
     text = ""
     for line in lines:
          line = line.strip()

          if not line:
               continue
          text += line
     return text

def normalize_numbers(text: str):
     normalized_text = ""

     i = 0
     k = len(text)
     while i < k:
          if text[i].isdigit():
               normalized_text += "0"
               while i < k and text[i].isdigit():
                    i += 1
               continue
          normalized_text += text[i]
          i += 1
     return normalized_text