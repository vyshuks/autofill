import autofill

words = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]

autofill.register_words(words)

result = autofill.search(word="mo", limit=3)
print(result)

print(autofill.search("mouse"))

print(autofill.find_top_k_matches())
