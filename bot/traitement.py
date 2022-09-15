from ampalibe import Payload
from ampalibe.ui import QuickReply
from datetime import datetime

quick_rep_principal = [
    QuickReply(
        title="🥰BACC",
        payload="/bacc",
    ),
    QuickReply(
        title="😍LICENCE",
        payload="/licence",
    ),
    QuickReply(
        title="😱MASTER",
        payload="/master",
    ),
]

quick_rep_lieu = [
    QuickReply(
        title="🔴ANTANANARIVO",
        payload="/antananarivo",
    ),
    QuickReply(
        title="🟠ANTSIRANANA",
        payload="/antsiranana",
    ),
    QuickReply(
        title="🟡MAHAJANGA",
        payload="/mahajanga",
    ),
    QuickReply(
        title="🟢TOLIARA",
        payload="/toliara",
    ),
    QuickReply(
        title="🔵TOAMASINA",
        payload="/toamasina",
    ),
    QuickReply(
        title="🟣FIANARATSOA",
        payload="/fianaratsoa",
    ),
]

quick_rep_lieu_licence = [
    QuickReply(
        title="🟥VOTRE ECOLE",
        payload="/ecole",
    ),
    QuickReply(
        title="🟨MINISTERE",
        payload="/ministere",
    ),
]


def diplomelivre(data, niveau):
    return f"Votre diplome {niveau} est déjà obtenu et vous l'avez recuperé le {data.get('date_obtention')}"


def quick_oui_nom_back(numero):
    quick = [
        QuickReply(
            title="✅OUI",
            payload=Payload("/ouibacc", numero=numero),
        ),
        QuickReply(
            title="❌NOM",
            payload="/nom",
        ),
    ]
    return quick


def quick_oui_nom_licence(numero):
    quick = [
        QuickReply(
            title="✅OUI",
            payload=Payload("/ouilicence", numero=numero),
        ),
        QuickReply(
            title="❌NOM",
            payload="/nom",
        ),
    ]
    return quick


def traitement_info_bacc(data):
    information = data[0]
    print(information)
    return f"Lire attentivement les informations ci-dessous si vous concernez vraiment\n\n\
✅Nom : {information.get('nom')}\n✅prenom : {information.get('prenom')}\n✅Date de naissance : \
{information.get('date_naissance')}\n✅Lieu de naissance : {information.get('lieu_naissance')}\n\
✅Pays de naissance : {information.get('pays_de_naissance')}\n✅serie : {information.get('serie')}\n\
✅session : {information.get('session')}\n✅Mention : {information.get('mention')}"


def traitement_info_licence(data):
    information = data[0]
    print(information)
    return f"Lire attentivement les informations ci-dessous si vous concernez vraiment\n\n\
✅Nom : {information.get('nom')}\n✅prenom : {information.get('prenom')}\n✅Date de naissance : \
{information.get('date_naissance')}\n✅Lieu de naissance : {information.get('lieu_naissance')}\n\
✅Pays de naissance : {information.get('pays_de_naissance')}\n✅cin n° : {information.get('num_cin')}\n\
✅adresse : {information.get('adresse')}\n✅tel : {information.get('num_telephone')}"
