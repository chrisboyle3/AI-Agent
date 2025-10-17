from functions.get_files_info import get_files_info

if __name__ == "__main__":
    # 1️⃣ Current directory
    print('Result for current directory:')
    print(get_files_info("calculator", "."))
    print()

    # 2️⃣ pkg directory
    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print()

    # 3️⃣ /bin directory (outside allowed boundary)
    print('Result for "/bin" directory:')
    print(get_files_info("calculator", "/bin"))
    print()

    # 4️⃣ ../ directory (outside allowed boundary)
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))
