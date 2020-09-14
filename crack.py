import haslib 

flag = 0

pass_hass = input("Enter mmd5 hash: ")

wordlist = input("file name: ")

try:
pass_file = open (wordlist, 'r')
except
print("no file found")
quit()

for word in pass_file:

enc_wrd = word_encode('utf-8')
digest = hashlib.md5(enc_wrd.strip()).hexdigest()

print(word)
print(digest)
print(pass_hash)

if digest == pass_hash:
print("Password found")
print("Password is " + word)
flag = 1
break

if flag == 0:
print("password not in the list " )
