import app.models.boutique_model as boutique_model


def calculer_prix_ht(prix_ttc, taux_tva):
    return round(prix_ttc / (1 + taux_tva), 2)


def calculer_prix_ttc(prix_ht, taux_tva):
    return round(prix_ht * (1 + taux_tva), 2)


def traiter_commande(quantité_commande):
    if quantité_commande > boutique_model.quantité_stock:
        print("pas assez de chaussette en stock")
        return None

    print("commande realise")
    prix_hors_taxe = calculer_prix_ht(boutique_model.prix_unitaire, boutique_model.tva)
    prix_ttc = calculer_prix_ttc(prix_hors_taxe, boutique_model.tva)
    montant_achat_ht = prix_hors_taxe * quantité_commande
    montant_achat_ttc = prix_ttc * quantité_commande
    stock_restant = boutique_model.quantité_stock - quantité_commande
    boutique_model.quantité_stock = stock_restant
    boutique_model.compte_client -= montant_achat_ttc
    boutique_model.compte_boutique += montant_achat_ht

    return {
        "montant_achat_ht": montant_achat_ht,
        "montant_achat_ttc": montant_achat_ttc,
        "stock_restant": stock_restant,
        "compte_client": boutique_model.compte_client,
        "compte_boutique": boutique_model.compte_boutique,
    }

def verif_stock():
    stock = boutique_model.quantité_stock
    prix = boutique_model.prix_unitaire
    if stock < 10:
        print("!! Stock bientôt épuisé !!")
    elif 10 < stock < 15 and prix > 5:
        print("!! Attention produit presque en ruptures")

