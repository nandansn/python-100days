### BeautifulSoup

- library used to scrap or parse the content from the html 
- need to install 
> pip3 install beautifulsoup4

**Documentation**

[Ref] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


### How to get the html content?

**Option 1**

- go to the required website,
- right click and choose view source, 
- copy the content
- put it in a file

**option 2**
- make the request call of the html page
- get the response,
- from the response, use the content property to get the details
- to know the response properties, use response._attrs

### Making the soup

- To parse a document, pass it into the BeautifulSoup constructor. You can pass in a string or an open filehandle:

> from bs4 import BeautifulSoup
>
> with open("index.html") as fp:
>    soup = BeautifulSoup(fp, 'html.parser')

or

> soup = BeautifulSoup("<html>a web page</html>", 'html.parser')


### Scrapping an element

- using html element tag name
- using attributes like [id, name, class, etc]
- also we can use css path to find the element
- find(name='tagname', id='attr_value'), returns the first matching tag
- find_all(tagName, attributes) will list all the mtching elements

- to the get the attribute value of the tag.
- soup.tag.get('attr_name')

### Scrapping list of elements

- get the elements matching the conditions

- select('css path')
- select_one('css path')


### lxml library 

- used to parse the html file content
- you can pass the parser like this

- lxml is a new Python binding for libxml2 and libxslt, completely independent from these existing Python bindings. Its aims:

    - Pythonic API.
    - Documented.
    - Use Python unicode strings in API.
    - Safe (no segfaults).
    - No manual memory management!

> soup = BeautifulSoup("<html>a web page</html>", 'lxml')

**documentation**

[Ref] ()




### How to use th library?




