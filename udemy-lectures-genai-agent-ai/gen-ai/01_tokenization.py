import tiktoken

enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
text = "hey its saurabh" # [9906, 11, 1917, 0]
text2 = "hey" # [9906, 11, 1917, 0]

encoded = enc.encode(text)
encoded_2 = enc.encode(text2)
print("encoded::", encoded)
print("encoded_2::", encoded_2)

decoded_text = enc.decode(encoded)
print("decoded_text::", decoded_text)