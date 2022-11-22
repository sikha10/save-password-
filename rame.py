from cryptography.fernet import Fernet

# key = Fernet.generate_key()

b = b'kzb1tN4tG0LoTBKIiZknad7K6Yi26UiS7oxI2XIN6Qw='

crypter = Fernet(b)

s = "password"


# pw = crypter.encrypt(s.encode())
k = b'gAAAAABjQdAiGTfu3mqPn5wA_29INk3ClH-QFumhFd7UdfsJybg8dSdCYbbYzMe4wXRf88Z7zcMP-F8brBqjYENXtTTG2dIQww=='

dec = crypter.decrypt(k)

# print(pw)
print(dec)
# print(key)

lst = [1,2,3]
lst2 = [4,5,6]
for i, s in zip(lst, lst2):
    print(i, "--", s)

tup = ("saba", "sikha")

print(type(tup))
print(tup[0])
