import pybase64
import matplotlib

f1 = open("flag.png", "rb")
flag_raw = f1.read()
flag_encoded = pybase64.b64encode(flag_raw)

f2 = open("universe.png", "rb")
universe_raw = f2.read()
universe_encoded = pybase64.b64encode(universe_raw)

#result = flag_encoded ^ universe_encoded
'''
for i, j in flag_encoded, universe_encoded:
    c = i ^ j
    result = result + c
'''


img = matplotlib.imread("flag.png")
print(type(img))

print(result)
