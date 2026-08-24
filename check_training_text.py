def check_for_alphanumeric_characters(text):
     for c in text:
          if c == " ":
               continue
          elif c.isdigit() and c != "0":
               return f"found forbidden character: {c}"
          elif not c.isalnum():
               return f"found forbidden character: {c}"
     return True

def get_word_count(text):
     return len(text.split())

if __name__ == "__main__":
     with open("plaintext.txt", "r", encoding="utf-8") as file:
          text = file.read()

     res = check_for_alphanumeric_characters(text)
     if res is True:
          print("TEST: OK")
     else:
          print(res)
          exit(1)

     size = get_word_count(text)
     print("Words: ", size)
