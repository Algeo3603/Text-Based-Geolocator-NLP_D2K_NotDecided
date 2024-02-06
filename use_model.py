import spacy

nlp_ner = spacy.load("/content/model-last")


text = '''Bhargavi Lives in Ville Parle and Alan lives in Andheri'''
def get_place_list(text):
    doc = nlp_ner(text)
    loc_entities = [ent.text for ent in doc.ents]
    return loc_entities