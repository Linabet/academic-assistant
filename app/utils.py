import re

def detecter_langue(texte):
    """
    Détecte automatiquement la langue d'une question
    Retourne : "fr", "ar", ou "darija"
    """
    texte = texte.lower().strip()
    
    # 1. Si contient des caractères arabes -> arabe classique
    if re.search('[\u0600-\u06FF]', texte):
        return "ar"
    
    # 2. Mots darija typiques
    mots_darija = [
        "wash", "ach", "kayn", "makanch", "had", "hadak", "hadchi",
        "dak", "f", "dial", "bach", "ula", "walo", "hna", "tnia",
        "chhal", "bhal", "gadi", "mazal", "daba", "bekri", "tn", "tlata",
        "rjel", "mra", "drari", "zyen", "bzzaf", "qrib", "b3id", "hada",
        "dik", "hadi", "fin", "mnin", "ash", "3la", "7ta", "bla", "m3a"
    ]
    
    mots_darija_set = set(mots_darija)
    mots_texte = texte.split()
    
    score_darija = sum(1 for mot in mots_texte if mot in mots_darija_set)
    
    # Si au moins 2 mots darija OU présence de mots-clés typiques
    if score_darija >= 2 or any(k in texte for k in ["kayn", "ach", "wash"]):
        return "darija"
    
    # 3. Par défaut : français
    return "fr"