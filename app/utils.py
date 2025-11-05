from app.models.boutique_model import (
    nom_boutique,
    produit,
    prix_unitaire,
    quantité_stock,
    tva,
    compte_client,
    compte_boutique,
)


def afficher_informations_boutique():
    print(
        f"la boutique {nom_boutique} vend des {produit} au prix de {prix_unitaire}. "
        f"il y a {quantité_stock} en stock. la tva est de {tva}. "
        f"le compte client est de {compte_client}€ et le compte boutique est de {compte_boutique}€."
    )


def afficher_recapitulatif(recapitulatif):
    print(
        f"recap commande:\n"
        f"- montant ht: {recapitulatif['montant_achat_ht']}€\n"
        f"- montant ttc: {recapitulatif['montant_achat_ttc']}€\n"
        f"- stock restant: {recapitulatif['stock_restant']}\n"
        f"- compte client: {recapitulatif['compte_client']}€\n"
        f"- compte boutique: {recapitulatif['compte_boutique']}€\n"
        f"- merci pour votre achat ! c'est cool :)"
    )


def afficher_facture(recapitulatif, quantité_commande):
    montant_tva = recapitulatif["montant_achat_ttc"] - recapitulatif["montant_achat_ht"]

    ligne_separation = "-" * 40

    print(ligne_separation)
    print(f"{nom_boutique}")
    print(ligne_separation)
    print("Produit qté ht")

    produit_formaté = produit.capitalize()
    prix_ht_arrondi = round(recapitulatif["montant_achat_ht"], 2)
    total_ht_arrondi = round(recapitulatif["montant_achat_ht"], 2)
    tva_arrondie = round(montant_tva, 2)
    total_ttc_arrondi = round(recapitulatif["montant_achat_ttc"], 2)

    print(f"{produit_formaté} {'.' * 45} {quantité_commande} {prix_ht_arrondi}")
    print(f" total ht : {total_ht_arrondi}")
    print(f" tva : {tva_arrondie}")
    print(f" total ttc : {total_ttc_arrondi}")
    print(ligne_separation)


def afficher_types_variables():
    print("\nTypes des variables:")
    print(f"nom_boutique: {type(nom_boutique)}")
    print(f"produit: {type(produit)}")
    print(f"prix_unitaire: {type(prix_unitaire)}")
    print(f"quantite_stock: {type(quantité_stock)}")
    print(f"tva: {type(tva)}")
    print(f"compte_client: {type(compte_client)}")
    print(f"compte_boutique: {type(compte_boutique)}")
