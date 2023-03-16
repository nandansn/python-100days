import requests as req



url_path = "https://api.kanye.rest/"

def get_quote():
    res = req.get(url_path)
    print("Status:{} Message:".format(res.status_code, res.json("quote")))
    
get_quote()