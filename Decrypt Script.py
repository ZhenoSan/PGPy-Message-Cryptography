import pgpy

with open("Private Key.txt", "r") as key_file:
    KEY_PRIV = key_file.read().lstrip()

priv_key = pgpy.PGPKey()
priv_key.parse(KEY_PRIV)
pass

#------------------

message_from_file = pgpy.PGPMessage.from_file("Encrypted_File")

raw_message = priv_key.decrypt(message_from_file).message
 
with open("Decrypted_File.csv","w") as csv_file:
    csv_file.write(raw_message)
    
print("Decryption Complete")