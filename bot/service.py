import requests


def get_information_bacc(numero):
    data = requests.get(f"http://127.0.0.1:8000/api/bacc/?numero={numero}")
    return data.json()


def get_information_licence(numero):
    data = requests.get(f"http://127.0.0.1:8000/api/etudiant/?numero={numero}")
    return data.json()


def postDemande(data):
    return requests.post(f"http://127.0.0.1:8000/api/demande/", data=data)


def verifDiplome(numero):
    data = requests.get(f"http://127.0.0.1:8000/api/diplomeLMD/?numero={numero}")
    return data.json()
