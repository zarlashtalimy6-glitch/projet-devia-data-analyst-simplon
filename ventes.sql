SELECT SUM(prix * qte) AS Chiffre_Affaires_Total
FROM ventes;

SELECT produit, SUM(prix * qte) AS Ventes
FROM ventes
GROUP BY produit;

SELECT region, SUM(prix * qte) AS Ventes
FROM ventes
GROUP BY region;