f1 = "file2.txt"
f2 = "file2.txt"
f3 = "file3.txt"
fd = ""
with open('file1.txt', 'r+') as fd1:
    file1_values = fd1.read()
    with open('file2.txt', 'r+') as fd2:
        file2_values = fd2.read()
        with open('file3.txt', 'w+') as fd:
            fd.write(file1_values)
            fd.write(file2_values)
            print(fd)

