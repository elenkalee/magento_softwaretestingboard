# https://softwaretestingboard.com/practice-api-testing-using-magento-2/
import pytest
import requests

#Consumer Key: u5gkmvsnxvc5w6qxoy2iwx98mkc1j30d
#Consumer Secret: brpz2fvopf9fcdlkqh6dlbh8ui5lqow6
#Access Token: cdxf96vcah8pbivc3zzrshd8t15ikua5
#Access Token Secret: lkqssgly3qw0eel6pcaug1s9203v2pwn


#DRAFTS

class TestApi:

    def test_create_customer_account(self):
        #To create a customer account, admin permissions are required.
        endpoint = "https://magento.softwaretestingboard.com/rest/default/V1/customers"
        headers = {
                    'Content-Type': 'application/json',
                    'Authorization Bearer': 'cdxf96vcah8pbivc3zzrshd8t15ikua5'
                   }
        """You should substitute the value
         of the email parameter with a real email address. 
         As if you do that, you can receive all notifications.
        """
        payload = {
            "customer": {
                "email": "elena.lipukhina@gmail.com",
                "firstname": "Jane",
                "lastname": "Doe",
                "addresses": [{
                    "defaultShipping": 'true',
                    "defaultBilling": 'true',
                    "firstname": "Jane",
                    "lastname": "Doe",
                    "region": {
                        "regionCode": "NY",
                        "region": "New York",
                        "regionId": 43
                    },
                    "postcode": "10755",
                    "street": ["123 Oak Ave"],
                    "city": "Purchase",
                    "telephone": "512-555-1111",
                    "countryId": "US"
                }]
            },
            "password": "Password1"
        }
        result = requests.post(endpoint, headers=headers, params=payload)

        print(result.json())


    def test_create_customer_token(self):
        # TODO: work
        headers = {'Content-Type': 'application/json'}
        payload = {
            "username": "elena.42rus@yandex.ru",
            "password": "Qwerty123)"}
        base_url = 'https://magento.softwaretestingboard.com/rest/default/V1/integration/customer/token/'
        result = requests.post(base_url, headers=headers, params=payload)
        print(f"Token is {result.json()}")


    def test_get_info_about_customer(self):
        # TODO: doesn't work
        base_url = 'https://magento.softwaretestingboard.com/rest/default/V1/customers/me'
        headers = {
            'Content-Type': 'application/json',
            'Authorization Bearer': '9el8858674hx5fh075nf4ljtrvo5ayb9'
                   }

        result = requests.get(base_url, headers=headers)
        print(result.json())
