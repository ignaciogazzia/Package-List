import requests
import json


def search_packages(packages: list):
    headers = {
        "Content-Type": "application/json",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTY0NDIxLCJqdGkiOiJjNjE0YTBmYmEyY2U0NTc2YmFmNWE4OGYyYzIwOWQyMiIsInVzZXJfaWQiOjI1NDJ9.q83zbZxIuy1gTkXIOS_Q5rV6M9Kd_tPBHOI5sKrjtgs"
    }
    sesion = requests.session()

    for pack in packages:
        url = 'https://ppointapi.clicoh.com/api/v1/pickup_points/packages/?order_by=-id&section=list_packages&search=' + \
            pack + '&page=1&size=100'
        # url = 'http://ppointapi.clicoh.com/api/v1/pickup_points/packages/?search=' + \
        #    pack + '&section=list_packages'
        response = sesion.get(url=url, headers=headers)
        diccionario = json.loads(response.text)
        print("Paquete: " + pack + " ---> " + estaEnElSoft(diccionario))


def estaEnElSoft(respuesta: str):
    if respuesta["count"] == 1:
        return 'está en el soft'
    return 'no está en el soft/devolvió 2 o más paquetes'


if __name__ == '__main__':
    # fill the ids array with id packages (meli/clicoh)
    # format ids = ["id1", "id2", ....]
    packages = [
        "41921947748",
        "41921863603",
        "41921849406",
        "41921798050",
        "41921760206",
        "41921742453",
        "41921719596",
        "41921697775",
        "41921665473",
        "41921626599",
        "41921622684",
        "41921587785",
        "41921515496",
        "41921506188",
        "41921482997",
        "41921450577",
        "41921407075",
        "41921391585",
        "41921378651",
        "41921339036",
        "41921333787",
        "41921299883",
        "41921241716",
        "41921233012",
        "41921218251",
        "41921203801",
        "41921172400",
        "41921165732",
        "41921142292",
        "41921119000",
        "41921111635",
    ]

    search_packages(packages)
