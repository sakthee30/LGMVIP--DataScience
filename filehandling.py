#file handling I/O
def file_handling(file_path):
    try:
        extension = file_path.rsplit('.', 1)[-1]

        if extension == 'txt':
            print(f"The extension is {extension} - This file is a text file")
        elif extension == 'xlsx':
            print(f"The extension is {extension} - This file is a excel file")
        elif extension == 'csv':
            print(f" The extension is {extension} - This file is a csv file")
        else:
            print(f"The extension is {extension} - Unknown file type")
       
        print("Full Content")
        with open(file_path, 'r') as file:
            result = file.read()
            print(result)
            print('''
                  ''')
     
        print("Line by Line Content")
        content = []
        with open(file_path,'r') as file:
            for i, line in enumerate(file, start=1):
                 content.append(f"Line {i}: {line.strip()}")
                 print(f"Line {i}: {line.strip()}")
        
        return extension, result, content

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("Permission Denied")


file_path = r"C:\Users\sakthep\Downloads\simple.txt"
file_type, full_content, line_by_line_content  = file_handling(file_path)

try:
    
        file_path = r"C:\Users\sakthep\Downloads\simple.txt"
        with open(file_path, 'r') as file:
            result = file.read()
        print(result)

except FileNotFoundError:
        print("File not found")

except PermissionError:
        print("Permission Denied")


#Reading the file line by line and printing
try:
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("Permission Denied")

#Input a word from user and find how many occurrences of the word in the file
def word_count(file_path,word):
    try:
        with open(file_path, 'w') as file:
            text = file.read().lower()
            count = text.count(word)
            return count
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission Denied")

file_path = r"C:\Users\sakthep\Downloads\simple.txt"
word = input("Enter the word to search : ")
count_of_word = word_count(file_path,word)

if count_of_word is not None:
    print(f"The Word {word} occurred {count_of_word} times.")

#writing normal content to a .txt file
def convert_content(file_path, content):
    content = """Python is a powerful programming language. It is widely used for web development, data science, machine learning, AI and more."""
    with open('newfile.txt', 'w') as file:
        file.write(content)

print("File written successfully")

