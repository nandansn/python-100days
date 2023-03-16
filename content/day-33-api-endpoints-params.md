### API end points
- how to call the rest api?
    - using the library, **requests**

### Requests
    - url
       - protocol
       - host name
       - port
       - resources
    - api method
    - headers
        - content
        - auth
        - etc..
    

### response

- status code
- response body

### status codes

 -   Informational responses (100–199)
 -   Successful responses (200–299)
 -   Redirection messages (300–399)
 -   Client error responses (400–499)
 -   Server error responses (500–599)

 [Ref] (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)


### How to handle if there is an error in the response?

- **request** module has the built in methods to raise the exceptions
- like,
> reaponse.raise_for_status(), will create one, if there is an error.


### References:

[Ref] (https://www.geeksforgeeks.org/python-requests-tutorial/)



