import requests
import json


def search_packages(packages: list):
    headers = {
        "Content-Type": "application/json",
        "authorization": "introduzca su token aquí (bearer)"
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
    packages = ['41926587293', '41926571209', '41926491245', '41926476691', '41926452874', '41926444493', '41926433257', '41926408927', '41926377672', '41926353847', '41926330496', '41926310546', '41926304804', '41926288065', '41926278612', '41926274201', '41926252243', '41926234417', '41926224997', '41926196479', '41926179275', '41926153136', '41926124296', '41926004373', '41925987736',
                '41925919700', '41925881495', '41925867368', '41925735784', '41925670539', '41925663838', '41925660966', '41925629898', '41925616533', '41925567431', '41925558592', '41925450386', '41925407147', '41925366800', '41925346954', '41925237161', '41925169495', '41925121591', '41925024386', '41925073311', '41925070483', '41925046575', '41924940257', '41924897239', '41924884795']

    search_packages(packages)
