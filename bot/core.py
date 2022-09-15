import ampalibe
import service as serv
import traitement as trt
import constantes as const
from conf import Configuration

bot = ampalibe.init(Configuration())
chat = bot.chat
query = bot.query
# create a get started option to get permission of user.
# bot.chat.get_started(payload="/get_started")


@ampalibe.command("/get_started")
def get_started(sender_id, **extends):
    chat.send_message(sender_id, const.salutation_information)
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )


@ampalibe.command("/")
def main(sender_id, **extends):
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )


@ampalibe.command("/bacc")
def bacc(sender_id, **extends):
    chat.send_message(sender_id, const.demande_num_bacc)
    query.set_action(sender_id, "attente_num_bacc")


@ampalibe.command("/licence")
def bacc(sender_id, **extends):
    chat.send_message(sender_id, const.demande_lmd)
    query.set_action(sender_id, "attente_num_licence")


@ampalibe.command("/master")
def bacc(sender_id, **extends):
    chat.send_message(sender_id, const.demande_lmd)
    query.set_action(sender_id, "attente_num_master")


@ampalibe.action("attente_num_bacc")
def informationBacc(sender_id, cmd, **extends):
    numero = cmd.strip()

    if numero.isdigit():
        get_info = serv.get_information_bacc(numero)
        print(get_info[0].get("Diplome_obtenu"))

        # if get_info[0].get("Diplome_obtenu"):
        #     chat.send_message(sender_id, trt.diplomelivre(get_info[0], "BACCALAUREAT"))
        #     return True

        if get_info:
            chat.send_message(sender_id, trt.traitement_info_bacc(get_info))
            chat.send_quick_reply(
                sender_id,
                trt.quick_oui_nom_back(get_info[0].get("numero_iscription")),
                const.oui_nom,
            )
            query.set_action(sender_id, None)

        else:
            chat.send_message(sender_id, const.num_fake_bacc)
            query.set_action(sender_id, None)
            chat.send_quick_reply(
                sender_id, trt.quick_rep_principal, const.text_quick_principal
            )
    else:
        chat.send_message(sender_id, const.const_num_not_digit)
        query.set_action(sender_id, None)
        chat.send_quick_reply(
            sender_id, trt.quick_rep_principal, const.text_quick_principal
        )


@ampalibe.action("attente_num_licence")
def informationLicence(sender_id, cmd, **extends):
    numero = cmd.strip()

    if numero.isdigit():
        # verification = serv.verifDiplome(numero)[0]
        # if verification.get("obtenu"):
        #     chat.send_message(sender_id, trt.diplomelivre(get_info[0], "LICENCE"))
        #     return True

        get_info = serv.get_information_licence(numero)

        if get_info:
            chat.send_message(sender_id, trt.traitement_info_licence(get_info))
            chat.send_quick_reply(
                sender_id,
                trt.quick_oui_nom_licence(get_info[0].get("numero_iscription")),
                const.oui_nom,
            )
            query.set_action(sender_id, None)

        else:
            chat.send_message(sender_id, const.num_fake_bacc)
            query.set_action(sender_id, None)
            chat.send_quick_reply(
                sender_id, trt.quick_rep_principal, const.text_quick_principal
            )
    else:
        chat.send_message(sender_id, const.const_num_not_digit)
        query.set_action(sender_id, None)
        chat.send_quick_reply(
            sender_id, trt.quick_rep_principal, const.text_quick_principal
        )


@ampalibe.command("/ouibacc")
def paymentBancaire(sender_id, numero, **extends):
    query.set_temp(sender_id, "num_inscription", numero)
    chat.send_quick_reply(sender_id, trt.quick_rep_lieu, const.lieu)


@ampalibe.command("/antananarivo")
def paymentBancaire(sender_id, **extends):
    query.set_temp(sender_id, "lieu", "ANTANANARIVO")
    chat.send_message(sender_id, const.payment)
    query.set_action(sender_id, "attente_payment")


@ampalibe.command("/antsiranana")
def paymentBancaire(sender_id, **extends):
    query.set_temp(sender_id, "lieu", "ANTSIRANANA")
    chat.send_message(sender_id, const.payment)
    query.set_action(sender_id, "attente_payment")


@ampalibe.command("/mahajanga")
def paymentBancaire(sender_id, **extends):
    query.set_temp(sender_id, "lieu", "MAHAJANGA")
    chat.send_message(sender_id, const.payment)
    query.set_action(sender_id, "attente_payment")


@ampalibe.command("/toliara")
def paymentBancaire(sender_id, **extends):
    query.set_temp(sender_id, "lieu", "TOLIARA")
    chat.send_message(sender_id, const.payment)
    query.set_action(sender_id, "attente_payment")


@ampalibe.command("/toamasina")
def paymentBancaire(sender_id, **extends):
    query.set_temp(sender_id, "lieu", "TOAMASINA")
    chat.send_message(sender_id, const.payment)
    query.set_action(sender_id, "attente_payment")


@ampalibe.command("/antananarivo")
def paymentBancaire(sender_id, **extends):
    query.set_temp(sender_id, "lieu", "FIANARATSOA")
    chat.send_message(sender_id, const.payment)
    query.set_action(sender_id, "attente_payment")


@ampalibe.action("attente_payment")
def demandeDiplomeBacc(sender_id, cmd, **extends):
    num = cmd.strip()
    query.set_temp(sender_id, "virement", num)
    chat.send_message(
        sender_id,
        f"✳️✳️✳️Votre demande a été bien réçu, Veuillez le recuperer  le Lundi 04 juillet 2022 auprer de votre lieu de recuperation✳️✳️✳️",
    )
    query.set_action(sender_id, None)
    # data ⁼ {
    #     "" :
    # }
    # post


@ampalibe.command("/ouilicence")
def lieuRecuperation(sender_id, numero, **extends):
    query.set_temp(sender_id, "num_unique", numero)
    chat.send_quick_reply(sender_id, trt.quick_rep_lieu_licence, const.lieu)
    query.set_action(sender_id, None)


@ampalibe.command("/ecole")
def ecole(sender_id, **extends):
    data = {"num_unique": "sdf", "lieu": "ECOLE"}
    ##post
    f"✳️✳️✳️Votre demande a été bien réçu, Veuillez le recuperer le Lundi 04 juillet 2022 auprer de votre lieu de recuperation✳️✳️✳️",
    query.set_action(sender_id, None)


@ampalibe.command("/ministere")
def ministere(sender_id, **extends):
    data = {"num_unique": "sdf", "lieu": "MINISTER"}
    # post
    f"✳️✳️✳️Votre demande a été bien réçu, Veuillez le recuperer le Lundi 04 juillet 2022 auprer de votre lieu de recuperation✳️✳️✳️",
    query.set_action(sender_id, None)


@ampalibe.command("/non")
def non(sender_id, **extends):
    chat.send_message(
        sender_id,
        "Alors veuillez bien verifier votre numero d'inscription et recommencer votre demande",
    )
    chat.send_quick_reply(
        sender_id, trt.quick_rep_principal, const.text_quick_principal
    )
