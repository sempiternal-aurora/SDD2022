import file_encryption
import os

def main():
    file = file_encryption.open_encrypted_file("Encryption Stuff - English/test.pdf")
    file = file_encryption.str_to_encrypted_list(file)
    file = file_encryption.decrypt_int_list(file, "R")
    file = file_encryption.to_bytes_list(file)
    os.remove("Encryption Stuff - English/raw_data.pdf")
    file_encryption.write_file("Encryption Stuff - English/raw_data.pdf", file)

if __name__ == "__main__":
    main()