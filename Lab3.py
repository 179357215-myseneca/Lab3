def write_text_file():
    name = "Please write Your Name"  
    with open("output.txt", "w") as file:
        file.write(f"My name is {name}.")

write_text_file()


