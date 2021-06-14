import file_encryption
import os

def main():
    file = file_encryption.open_file("Run Lola Run.pdf")
    file = file_encryption.to_int_list(file)
    file = file_encryption.encrypt_int_list(file, "R")
    os.remove("test.txt")
    file_encryption.write_encrypted_file("test.txt", file)

if __name__ == "__main__":
    main()
