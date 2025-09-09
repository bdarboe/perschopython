'''text = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"
letters_only = [ch for ch in text if ch.isalpha()]
count = len(letters_only)
print(count)


text = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"
n = 24

filtered = "".join(ch for ch in text if ch.isalpha())  # keep only letters
result = filtered[:n]

print(result)'''

text = "malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn"
start, end = 90, 110  # 3rd to 5th letter only

filtered = "".join(ch for ch in text if ch.isalpha())
result = filtered[start-1:end]

print(result)

text = "giveqcctsicslyqlenycn"
letters_only = [ch for ch in text if ch.isalpha()]
count = len(letters_only)
print(count)

