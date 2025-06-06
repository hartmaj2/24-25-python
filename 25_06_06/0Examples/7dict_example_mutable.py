# Example of how a dictionary works

# It works like a real dictionary, you give it a word and it gives you the "translation"

slovnicek = {}

slovnicek["sila"] = 10
slovnicek["rycholst"] = 20
slovnicek["inteligence"] = 14

print(50*"-")

print(slovnicek)

print(50*"-")

for klic in slovnicek:
    print(klic)

print(50*"-")

for klic in slovnicek:
    print(f"{klic}: {slovnicek[klic]}")