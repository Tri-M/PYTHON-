def psum(it):
    "This function makes explicit how many calls to sum() are done."
    print ("Another call!")
    return sum(it)

raw = [0.07,0.14,0.07]
print("How many calls to sum()?")
print [ r/psum(raw) for r in raw]

print("\nAnd now?")
s = psum(raw)
print [ r/s for r in raw]


print ("\nAnd now?")
print [ r/s  for s in [psum(raw)] for r in raw]