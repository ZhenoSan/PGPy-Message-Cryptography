import pgpy
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm, CompressionAlgorithm
'''
# we can start by generating a primary key. For this example, we'll use RSA, but it could be DSA or ECDSA as well
key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)

# we now have some key material, but our new key doesn't have a user ID yet, and therefore is not yet usable!
uid = pgpy.PGPUID.new('Syed Zain Zaidi', comment='PGP Assignment', email='zain.naqi@abc.com')

# now we must add the new user id to the key. We'll need to specify all of our preferences at this point
# because PGPy doesn't have any built-in key preference defaults at this time
# this example is similar to GnuPG 2.1.x defaults, with no expiration or preferred keyserver
key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
            hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384, HashAlgorithm.SHA512, HashAlgorithm.SHA224],
            ciphers=[SymmetricKeyAlgorithm.AES256, SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
            compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])
            
            
            
# assuming we already have a primary key, we can generate a new key and add it as a subkey thusly:
subkey = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)

# preferences that are specific to the subkey can be chosen here
# any preference(s) needed for actions by this subkey that not specified here
# will seamlessly "inherit" from those specified on the selected User ID
key.add_subkey(subkey, usage={KeyFlags.EncryptCommunications})

# ASCII armored
keystr = str(key)

print(keystr)
'''

KEY_PRIV = '''-----BEGIN PGP PRIVATE KEY BLOCK-----

xcZYBF6oTfIBEACvhqPSO0n/uDYlyl0o4DkdVIwMiUWWpxlA9kX+L5YSA2tSGDla
vZrj+Hpd7S/e2/+7HLbjCKjtxgtWXSlwLThwU7ysxAxKP4VaMqNmNl76wSg/WXg/
nJg3cGUy4jmr+NkPW1vwhJHL1j2S/5z0+ay1GdPv2UFcepnqE4vj1g5kzk6nVEjF
2FbpAMmUztLhf0jdwYEEQl9JE9SDcUp/Dkt28D6edzSQf+V+CkM1gf72bKBD61DN
bcI+01lmtRmWuRMhYfNov8LqRRnXPkwaamfdF1tMi+pXKl4E2XZKb1+f2Fy8nU5x
tqREd1uasTQH6REJmID24oguPagsllCmzw/zUHMrGwGGebu+HmjIUoB9CE7WKZya
wnn/lGk+1NSINmdEHWSV3K5alOUbw5I4VUkf2dbbcoPGB0L9cMJd+Mre1mNcny/6
gGSR34r3BVZ5gOsxokcd4yHdeWwWKyul+XbRXhvYGpVj6O0x90E8k1ayc6ICmbkS
IvZDArpxOIt+/2BJi69f4FlkqMKqx2S1qtTYNeOzmbpWvnl8ap0ZbC01iYljR0Sk
wl5WydiFb9bddAxk8veZBqjzM5iltABZbGz4STgZFNdlAI7iNckD39DQ2fnz8JcU
7bjdf/EXNv6+Y14wZPPEzM8CF1SB42l2XW9x67TvDBV4qZRwO6FIO7b2wQARAQAB
AA//RXNFoKpa5jayHhPK9qB5mNRaMZ+jDDADuwN2wFN90pTNwwbYssGw5qDrcfym
Y0yzDAsZhg1oIeSpmbt06PDLkw5e6hEMN9iYYA8HPisnO5pv3Vj+TlUcmVr8f7yp
SxVEdWIVp74cngWgCWjgZsHfhyy4Af/5b6kG+2pOgJCy00oaLvUXckjeYoUwPZP0
NssRPsUQ0mmcoCKbhIKwEkPKsj3u2O6bus0QNeXDoAlWo5RpeVZDe3UBVbB0gEIJ
5OxH2H6UPA8cBWvgBJ2eqRkPDZjvRANcbq7R0qNkvaEBuhJ25x5q6m10465CbZvN
1Y9vcVeJN6Z8cadtwm6bbNUjHt/chYhGLZs7W6beD/N8+V4RRmSMw/fDvihlrUzY
TJLBvmQlSRdg5KWZ8uuPLTtpmAeRpeJJqFkzmclM2HRymx4+5n7kxyUTyFm51CGK
S33FWuUUdfvnRw6m0twDbr85pOnoQzbz0ilsQ0Fi8S+tEqVulpcTqaKQ5lAg6Yhm
DGeByUSajFW0J/YFAr0f8wmZ25U1zsY/eq/+epe+fWDvr33LFsgjcq6TTWtdbNe0
AnQt3CJu/ZYNJeZTWPSJbOoPuaQ+C8zubjhOjlcjrhKq9K8cx/iS6py6Ftc4kian
kXXCkC0t1YDsKtQelPEx2ZcADLrz+Wg6sbSluCWMandefZEIAODepmhJgcSQMXjj
pBFelJnkX5N1Iz64erQH6+lY1WLBnnt/T5yrAnCK87bG1WzgcTYK3/yrWehu9R0i
nkNbL1AfTqJsV3JyMnSD6InGeP64MIkGOihLCaJdxmuQIljyVCQ4L2QSibfaMxzv
7BQtFE4E01UdffLBtTvXUMZJqULAnr93sOfidIu1lBcMSuzS42WKeq1QpG/tOyUy
WbBGWDxiQ/rGsjyJsmeF47d2NXS/ZmSutXF9g1ZnNPaqCsbi7ncurj1gYf17hcfG
mQ2OLWxQeOpzpYEnSmy4iSbrsdcveJWw95BjYBM8a2V8fcoW565IYBnicIQr6AoD
RnEleh0IAMfTQNZrjF6ZjF4vbn+72VYI4V4d+/oHkvP9AQiNJhN3/GRJElq6UXko
4N2Dy0rUAAuvz91aB7rXcEiUmvsONdbdEZzP5eRJQU1oouZlnBspukKdeMx9BOL5
Fz2gDEYNpPd++D4T9H0+vjtZ3jzlkwaSsKsSBTRqXoSF5USzTMCewFNSjn921SkE
RmaNeCnGeTsnVmbbb8CrrshxKi7xl2uNzw3W+l7+MeXN5980/UDH7oKk3BHFcjgG
tccyI+yVj/TZi78Wd/FY2yT2tOFa14iypCsfEeCP11vtPrTi4XOXGVnb2x5zg3LH
ZAB/3SbSmDWUFW9mR6RIm1p5LFBKLfUH/0mCw8hiSYJeVC07Pg2Z96Vxk+rZFtcP
bxnyqSGHKBAXUo6qNQ8p5prhwXVyqMxnq3fxgqePj6KNPCPOOeETk+nbChJhDLBj
hmaJKfml6yT6u2kupQqoj5/9OfUTx9+6TCmRnnvJtaHkoYleletV+ZNHubAW/FOk
EFQXzG+x7ieOtXnGzNQUa3gaM2xtqBUATqxcMaEWMD7m2vwocSFjCePPkGloI7AP
uVazf90TNX5lZArDi403Gz2suK4PpydzNLvk/a3BFqwAo+/IGQEknXcX18uSQv01
qRPmqbQeSAXwrpAk+jOdgjt6n17aJrbhUTfS1sOXc3Bh0dZIJQxKcQF+lc07U3ll
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
QO9vm2U7vtcQEu5KG5LSz8nAMxeuDLpS5PQ=
=nlBG
-----END PGP PRIVATE KEY BLOCK-----
'''.lstrip()

KEY_PUB = '''
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
=lQ+F
-----END PGP PUBLIC KEY BLOCK-----
'''.lstrip()

priv_key = pgpy.PGPKey()
priv_key.parse(KEY_PRIV)
pass

pub_key = pgpy.PGPKey()
pub_key.parse(KEY_PUB)
pass
#------------------

with open("Group 3_CustomerData.csv", "r") as csv_file:
    SOME_TEXT = csv_file.read()

msg = pgpy.PGPMessage.new(SOME_TEXT)

# this returns a new PGPMessage that contains an encrypted form of the
# unencrypted message
encrypted_message = pub_key.encrypt(msg)

pgpstr = str(encrypted_message)

with open("Encrypted_File", "w") as text_file:
    text_file.write(pgpstr)

print("Encryption Complete")

message_from_file = pgpy.PGPMessage.from_file("Encrypted_File")

raw_message = priv_key.decrypt(message_from_file).message
 
with open("Descrypted_File.csv","w") as csv_file:
    csv_file.write(raw_message)
    
print("Decryption Complete")
