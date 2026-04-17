# reading the file

# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# writing to a file in write mode

# with open("new_file.txt",mode="w") as file:
#     file.write("this is the new file")

# writing to a file with append mode

# with open("my_file.txt",mode="a") as file:
#     file.write("\nnew line inserted")


# absolute path

# with open("../files_directories/my_file.txt") as file:
#     content = file.read()
#     print(content)

with open("input/letters/starting_letters.txt") as file:
    content = file.read()
    print(content)

with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)
    for name in names:
        name = name.strip()
        with open(f"./output/greet_{name}.txt",mode='w') as greet_file:
            greet_file.write(content.replace("[name]",name))