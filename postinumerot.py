# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500

import json
from pickle import TRUE
import urllib.request

def get_postal_codes(district:str) -> str:
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        html = response.read()

        data = json.loads(html)
        resp = []


    for key in sorted (data):
        if data[key].replace(" ", "") == district.upper().replace(" ", ""):
            resp.append(key)

    if not resp:
        return "Tuntematon postitoimipaikka"
    else:
        return 'Postinumerot: ' + ', '.join(resp)

if __name__ == '__main__':
    district = input('Kirjoita postitoimipaikka: ').upper()
    postinumerot = get_postal_codes(district)

    if postinumerot:
        print(postinumerot)
    else:
        print("Tuntematon postitoimipaikka")

