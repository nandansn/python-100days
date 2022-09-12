## Excecption

### try, catch, else, finally

- try, block of code, which may cause the exception
- catch, block to catch exception that thrown in the try block
- else, In some situations, you might want to run a certain block of code if the code block inside try  ran without any errors. For these cases, you can use the optional else keyword with the try statement.
- finally, block which will get executed, if there is exception or no exception
- using raise, we can throw the  exception
- use except (a, b) liek this you can multiple exception in except

- you can catch specific exception
- you can print the error message caused by the exception

### how to create custom exception
- custome exceptions are created using the user defined class,
- user defined class should be derived from Exception class

- code reference [Ref] (https://www.programiz.com/python-programming/user-defined-exception)


## use json 
- use 'json' lib to read write json data
- json.dump() -> to write data, data should be dictionary format
- json.load() -> to read the data
- for update,
    read json data using old_data = json.load() 
    create new data dict new_dict = {}
    old_data.update(new_dict)
    json.dump(old_data,data_file)
