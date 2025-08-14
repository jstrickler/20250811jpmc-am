def shout(word: str, times: int = 1) -> str:
    return word.upper() * times

a: str = shout('Python')
print(f"{a = }")
b: list[float] = []
b.append(shout('Python', 3))
print(f"{b = }")
print()
shout(50, 5)

def read_files(*file_paths: str) -> None:
    for file_path in file_paths:
        print(f"Opening {file_path}")
        with open(file_path) as file_in:
            pass

read_files('../DATA/mary.txt', '../DATA/parrot.txt')
print()

