def modify_content(content):
    
    #  convert the content to uppercase
    return content.upper()

def main():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Open the file and read its content
        with open(filename, "r") as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file cannot be read.")

if __name__ == "__main__":
    main()
