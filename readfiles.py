f = open("file.bin", "br")
binary = f.read()
data = list(binary)
print(data);
f.close()
