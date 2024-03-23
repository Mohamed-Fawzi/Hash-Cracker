import hashlib 
import pyfiglet 

green_color_code = '\033[92m'
red_color_code = '\033[91m'
reset_color_code = '\033[0m'

banner = pyfiglet.figlet_format( " Hash Cracker ")
print (green_color_code + banner )

print( ' Algorithme supported : MD5 | SHA1 | SHA224 | SHA512 | SHA384 | SHA256  ' + reset_color_code)

hash_type=str(input( " what's the hash type : "))
wordlist_location=str(input("Entrer the wordlist location "))
hash=str(input("Enter hash : "))

try:
    words=open(wordlist_location).read().splitlines()
except FileNotFoundError:
    raise Exception( "FILE NOT FOUND" )

test=False 
for word in words:
    if hash_type.lower()=="md5":
        hash1=hashlib.md5(word.encode("utf-8"))
        hash1 = hash1.hexdigest()
        if hash1==hash:
            test=True
            break
    elif  hash_type.lower()=="sha1":
        hash1=hashlib.sha1(word.encode("utf-8"))
        hash1 = hash1.hexdigest()
        if hash1==hash:
            test=True
            break
    elif  hash_type.lower()=="sha224":
        hash1=hashlib.sha224(word.encode("utf-8"))
        hash1 = hash1.hexdigest()
        if hash1==hash:
            test=True
            break
    elif  hash_type.lower()=="sha512":
        hash1=hashlib.sha512(word.encode("utf-8"))
        hash1 = hash1.hexdigest()
        if hash1==hash:
            test=True
            break
    elif  hash_type.lower()=="sha384":
        hash1=hashlib.sha384(word.encode("utf-8"))
        hash1 = hash1.hexdigest()
        if hash1==hash:
            test=True
            break
    elif  hash_type.lower()=="sha256":
        hash1=hashlib.sha256(word.encode("utf-8"))
        hash1 = hash1.hexdigest()
        if hash1==hash:
            test=True
            break

if test:
    print ( red_color_code + "HASH FOUND :" + reset_color_code,word )

else :
    print ( red_color_code + "HASH NOT FOUND " + reset_color_code )

