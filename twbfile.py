def extract_twbx(file_path):
    twbx_content = []
    with open(file_path, 'r') as file:
        text = file.readlines()
        for line in text:
            if "Errno" in line:
                split_words = line.split('/')[-1]
                twbx_content.append(split_words)
    
    return twbx_content

path = r"C:\Users\sakthep\Downloads\status_report_20250612_115626.txt"
extract_content = extract_twbx(path)
print(extract_content)


def demo_func(file_path):
    store_content = []
    with open(file_path, 'r') as file:
        content = file.read()
        for line in content:
            if '.twbx' in line:
                split_words = line.split('/')[-1]
                store_content.append(split_words)

    return store_content

path = r"C:\Users\sakthep\Downloads\status_report_20250612_115626.txt"
to_call = demo_func(path)
print(to_call)







