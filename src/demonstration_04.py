"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("
- emotify("Make me mad") ➞ "Make me :P"

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    data = {
        "smile": ":D",
        "grin": ":)",
        "sad": ":(",
        "mad": ":P"
    }

    for k, v in data.items():
        txt = txt.replace(k, v)
        
    return txt

    

print(emotify("Make me smile"))
print(emotify("Make me grin"))
print(emotify("Make me sad"))
print(emotify("Make me mad"))