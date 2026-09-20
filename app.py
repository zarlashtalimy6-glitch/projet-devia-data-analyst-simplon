import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

données["chiffre_affaires"] = données["prix"] * données["qte"]

# Graphique 1 : ventes par produit
ventes_produit = données.groupby("produit")["qte"].sum().reset_index()

figure1 = px.bar(
    ventes_produit,
    x="produit",
    y="qte",
    title="Ventes par produit",
    labels={"qte": "Quantité vendue", "produit": "Produit"}
)

figure1.write_html("ventes-par-produit.html")


# Graphique 2 : chiffre d'affaires par produit
ca_produit = données.groupby("produit")["chiffre_affaires"].sum().reset_index()

figure2 = px.bar(
    ca_produit,
    x="produit",
    y="chiffre_affaires",
    title="Chiffre d'affaires par produit",
    labels={"chiffre_affaires": "Chiffre d'affaires", "produit": "Produit"}
)

figure2.write_html("chiffre-affaires-par-produit.html")

print("Les deux graphiques ont été générés avec succès !")
