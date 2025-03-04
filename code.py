def shift_cipher(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha(): 
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char  
    return encrypted

message = "GOOD MORNING"
shift_value = 5

encrypted_message = shift_cipher(message, shift_value)
print("Encrypted Message:", encrypted_message)