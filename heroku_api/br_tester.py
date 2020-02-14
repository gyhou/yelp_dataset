import json
import requests

# if you want to test local
# url = "http://localhost:9000"

# if you want to test deployed
url = "http://br-yelp-predict-rating.herokuapp.com"

val = {"category": 'Shopping',
       "review": "Service is okay but the wait time is too long."}

# you'll get a 200 response if the keys align
# and something bad if the keys don't align.
if __name__ == '__main__':
    r_success = requests.post(url, data=json.dumps(val))
    print(
        f"Request responded: {r_success}.\nResponse was\n{r_success.json()}")

"""
Categories:
1. Active Life
2. Auto Repair
3. Automotive
4. Beauty Spas
5. Contractors
6. Doctors
7. Event Planning Services
8. Fashion
9. Fast Food
10. Hair Salons
11. Health Medical
12. Home Garden
13. Home Services
14. Local Services
15. Professional Services
16. Real Estate
17. Shopping
"""
