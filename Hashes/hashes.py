import hashlib

key = b"str"
my_string= "This is a normal string. Nothing to see here".encode()

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print("First", hashed)


for i in range(10):
    hashed = hash(key)
    print(hashed)