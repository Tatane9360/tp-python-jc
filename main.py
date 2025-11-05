from app.utils import afficher_informations_boutique, afficher_facture, afficher_types_variables
from app.services.boutique_service import traiter_commande


def main():
    afficher_informations_boutique()
    quantité_commande = int(input("Combien de chaussettes voulez-vous acheter ? "))
    recapitulatif = traiter_commande(quantité_commande)
    if recapitulatif:
        afficher_facture(recapitulatif, quantité_commande)
    afficher_types_variables()


if __name__ == "__main__":
    main()    