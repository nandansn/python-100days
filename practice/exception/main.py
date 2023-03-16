try:
    with open('./file-11.txt', 'r') as data_file:
        data_file.read()
    map = {'key':'value'}
    map['key']
    list = []
    list[1]
except KeyError:
    print("key error")
except IndexError as error_mesasge:
    print(error_mesasge)
except:
    with open("./file-11.txt", 'w') as data_file:
        data_file.write('hello')
else:
    print('file exists no exception')