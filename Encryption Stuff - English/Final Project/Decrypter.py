import file_encryption
import os
import time

def main():
    print("Welcome to my project, you have now opened a decryption software.\nThis will attempt to decrypt a weird file that you found somewhere online\nsomewhere deep, hidden behind a few false trails and more.\nIt was an endeavour to locate.\n\nBut you found it, and that is all that matters. Now, all that stands in your\nway is an encryption algoithm. This program should break it, but to do that,\nyou need a key. A key that will break the encryption algorithm and discover\nthe secrets held behind it.\n\nFrom what you can gather, your best guess of the key is that it is a single,\ncapital letter, like 'A', or 'B'. Easy enough to guess right?\nJust enter what you think the key is, don't worry, you have unlimited guesses")
    key = input("\nEnter your guess here, followed by the enter key: ")
    while key.upper() != "R":
        print("Oh no, that doesn't seem to be right, try again?")
        key = input("Enter your guess here, followed by the enter key: ")
    file = file_encryption.open_encrypted_file("Encrypted_File.txt")
    file = file_encryption.str_to_encrypted_list(file)
    file = file_encryption.decrypt_int_list(file, key.upper())
    file = file_encryption.to_bytes_list(file)
    if os.path.isfile("Decrypted_File.pdf"):
        os.remove("Decrypted_File.pdf")
    file_encryption.write_file("Decrypted_File.pdf", file)
    print("\nYay! You were correct! Congratulations, happy decrypting!")
    print("(Don't worry, this will close soon)")
    time.sleep(10)

if __name__ == "__main__":
    main()
