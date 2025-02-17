from translate import Translator
import json
import time

def translate_json_keys(input_file, lang='fr'):
    # Création d'un traducteur
    translator = Translator(to_lang=lang)

    # Chargement du fichier JSON
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Création d'un dictionnaire vide pour stocker les données traduites
    translated_data = {}

    # Parcours récursif de la structure JSON pour traduire les clés
    def translate_dict(d):
        for key, value in d.items():
            if isinstance(value, dict):
                d[key] = translate_dict(value)
            else:
                try:
                    translated_key = translator.translate(key).text
                    d[translated_key] = value
                    del d[key]
                    # Introduce a delay to avoid API rate limits
                    time.sleep(0.5)
                except Exception as e:
                    print(f"Error translating key '{key}': {e}")
        return d

    # Traduction des clés et des valeurs
    translated_data = translate_dict(data)

    return translated_data

# Exemple d'utilisation
translated_data = translate_json_keys('en.json', lang='fr')
