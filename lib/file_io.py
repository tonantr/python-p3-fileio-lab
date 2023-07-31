def write_file(file_name, file_content):
    f = open(str(file_name) + '.txt', 'w')
    f.write(file_content)
    f.close()

def append_file(file_name, append_content):
    f = open(str(file_name) + '.txt', 'a')
    f.write(append_content)
    f.close()

def read_file(file_name):
    f = open(str(file_name) + '.txt', 'r')
    return f.read()
    




