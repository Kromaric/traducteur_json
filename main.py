# traducteur de json
'''
ce code va servir de script de traduction des application en backend. En plus claire ce code va recuperer
les fichiers json de traduction backend des application et fait les traductions lui mêmes en fonctions du language spécifié
'''



from googletrans import Translator
import json


def translate_json_keys(file_path, lang='en'):
    """Traduit les clés d'un fichier JSON en un langage spécifié.

    Args:
        file_path (str): Le chemin du fichier JSON.
        lang (str, optional): Le code du langage en lequel les clés doivent être traduites. Defaults to 'en'.

    Returns:
        dict: Le dictionnaire JSON traduit.
    """
    translator = Translator()
    with open(file_path, 'r') as file:
        data = json.load(file)

    translated_data = {}
    for key, value in data.items():
        translated_key = translator.translate(key, dest=lang).text
        translated_data[translated_key] = value

    return translated_data

# Utilisation de la fonction
translated_data = translate_json_keys('en.json', lang='fr')

# Sauvegarde du fichier JSON traduit
with open('translated_json_file.json', 'w') as file:
    json.dump(translated_data, file, ensure_ascii=False, indent=4)