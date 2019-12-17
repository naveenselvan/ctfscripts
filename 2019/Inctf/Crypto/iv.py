from Crypto.Cipher import AES
import binascii, sys

KEY="YELLOW SUBMARINE"
IV="Welcome to InCTFj finals! Hope you are having a great time here ;)"
print(len(IV))
IV=IV[:16]
cipher1="1614ad13f934ca0e410da7785ddb3b248377eab15cb6cd46f355f5896ce848ce6675b8d48f284bf4186c982ac74f9f9302d2d0c78ab3cd87fd61f5fa02003b38418c2e33c09882de5da99a8066a2f4e7"

def decrypt(cipher,passphrase):
    aes = AES.new(passphrase,AES.MODE_CBC,IV)
    return aes.decrypt(cipher)

print "decrypted data: " + decrypt(binascii.unhexlify(cipher1), KEY)

