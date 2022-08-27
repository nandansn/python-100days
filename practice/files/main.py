

file = open('./person.txt', mode='r')
content = file.read()
print(content)
file.close()


wfile = open('./new_file.txt', mode='w')
wfile.write(content+'\n'+'hello')
wfile.close()


with open('./new_file.txt', mode='r') as  readFile:
    print(readFile.read())

with open('./new_file.txt', mode='a') as writeFile:
    writeFile.write("done")