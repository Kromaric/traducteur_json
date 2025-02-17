from translate import Translator
import json
import time

def traduire_valeurs_json(fichier_entree, fichier_sortie, lang='fr'):
    # Création d'un traducteur
    traducteur = Translator(to_lang=lang)

    # Chargement du fichier JSON
    with open(fichier_entree, 'r') as fichier:
        donnees = json.load(fichier)

    # Parcours récursif de la structure JSON pour traduire les valeurs
    def traduire_dictionnaire(d):
        dictionnaire_traduit = {}
        for cle, valeur in d.items():
            if isinstance(valeur, dict):
                cle_traduite = cle
                valeur_traduite = traduire_dictionnaire(valeur)
                dictionnaire_traduit[cle_traduite] = valeur_traduite
            elif isinstance(valeur, str):
                try:
                    valeur_traduite = traducteur.translate(valeur)
                    dictionnaire_traduit[cle] = valeur_traduite
                    # Introduire une pause pour éviter les limites de fréquence de l'API
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Erreur lors de la traduction de la valeur '{valeur}' : {e}")
            else:
                dictionnaire_traduit[cle] = valeur
        return dictionnaire_traduit

    # Traduction des valeurs
    donnees_traduites = traduire_dictionnaire(donnees)

    # Enregistrement du nouveau fichier JSON
    with open(fichier_sortie, 'w', encoding='utf-8') as fichier:
        json.dump(donnees_traduites, fichier, ensure_ascii=False, indent=4)

# Exemple d'utilisation
traduire_valeurs_json('lang/en.json', 'lang/fr.json', lang='fr')
