def ecncrypt(message, key):
  result = ""
  for char in message:
    if char.isalpha():
      base = ord('A') if char.isupper() else ord('a')
      shifted = (ord(char) - base + key) % 26 + base
      result += chr(shifted)
    else:
      result += char
  return result

def decrypt(message, key):
  return ecncrypt(message, -key)


print("Caesar Cipher Encryption and Decryption")
choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
if choice == "E":
  message = input("Enter a message to encrypt: ")
  key = int(input("Enter the shift key (number of positions to shift): "))
  encrypted_message = ecncrypt(message, key)
  print(f"Encrypted message: {encrypted_message}")
else:
  message = input("Enter a message to decrypt: ")
  key = int(input("Enter the shift key (number of positions to shift): "))
  decrypted_message = decrypt(message, key)
  print(f"Decrypted message: {decrypted_message}")
