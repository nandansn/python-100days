with open('./file1.txt') as fp:
    print(fp.read())


with open('./file2.txt', mode="w") as fw:
    fw.write("happy always")    


with open('./file2.txt', mode="r") as fr:
    print(fr.read())

with open('./file1.txt', mode="a") as fa:
    fa.write("how are you?")

with open('./file1.txt') as f1:
    print(f1.read())