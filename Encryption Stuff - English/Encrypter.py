import file_encryption
import os

def main():
    file = file_encryption.open_file("Encryption Stuff - English/Pascal EBNF.pdf")
    file = file_encryption.to_int_list(file)
    file = file_encryption.encrypt_int_list(file, "R")
    os.remove("Encryption Stuff - English/test.pdf")
    file_encryption.write_encrypted_file("Encryption Stuff - English/test.pdf", file)

if __name__ == "__main__":
    main()