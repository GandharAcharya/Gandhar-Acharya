f= open("Sample")
print(f.tell())
print(f.readline())
f.seek(0)
print(f.tell())
print(f.tell())
f.close()
