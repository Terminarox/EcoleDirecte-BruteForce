import requests as rqs
DV = False
APIVERSION = "4.19.0"
username = str(input("username : "))
password = str(input("password : "))

class login:
    def __init__(self, user, password, version="4.18.3"):
        try:
            assert type(user) == str and user != ''
            assert type(password) == str and password != ''
        except:
            raise ValueError("Bad args !!!")
        v = version
        user = user
        password = password
        token = ""
        header = {
                'authority': 'api.ecoledirecte.com',
                'accept': 'application/json, text/plain, */*',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'content-type': 'application/x-www-form-urlencoded',
                'sec-gpc': '1',
                'origin': 'https://www.ecoledirecte.com',
                'sec-fetch-site': 'same-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.ecoledirecte.com/',
                'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        #try a password
        data = 'data={\n\t\"uuid\": \"\",\n\t\"identifiant\": \"' + user + '\",\n\t\"motdepasse\": \"' + password + '\"\n}'
        url = "https://api.ecoledirecte.com/v3/login.awp?v=" + v
        response = rqs.post(url=url, data=data, headers=header).json()
        if response['code'] == 200:
                token = response['token']
                header['x-token'] = token
                id = response['data']['accounts'][0]['id']
                email = response['data']['accounts'][0]['email']
                header['origin'] = "https://www.ecoledirecte.com"
                print("Succeful auhtentification for " + user + " with this password : " + password)
                exit()
        elif response['code'] == 505:
            print("Bad password or username")
        else:
            raise RequestError('Error {}: {}'.format(response['code'], response['message']))


inst = login(username, password, APIVERSION)

