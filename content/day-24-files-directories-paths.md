## Files, Directories and Paths

### How to open, read, write and close thhe files


#### Open, read and close the file
- using open method open('file path'), by default the file will be opened in the read mole
- open() method returns the file object, using the file object call read() method, to read the content of the file,
- store the file content in a string or you can directly print
- close the file using close() method
- to avoid explicit closing, you can open the like,
> with open('file path') as file:
>   file.read()

- with code block will take care of closing the file, no explicit call to close() mthod is required.

#### Open, write and close the file

- using open method open('file path'), by default the file will be opened in the read mole, we need to specify the mode write('file path',mode='w'),
    - to append the content to the file write('file path',mode='a'),
- open() method returns the file object, using the file object call write(content) method, to write the content of the file,
- close the file using close() method
- to avoid explicit closing, you can open the like,
> with open('file path') as file:
>   file.write(content)

- with code block will take care of closing the file, no explicit call to close() mthod is required. if  the file is not closed then it will eat the memory or process unneccessrily

#### How to derive the path?

- Abosulte path
    - absolute path starts from root directory like /usr/username/

- relative path
    - starts from the current working directory
    - ./man.txt, file in current directory
    - ./abc/cde.txt, from current directory, with in the folder, abc, there is a file cde.txt
    - ../ previous directory



