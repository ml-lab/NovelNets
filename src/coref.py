import spacy
from text_io import get_section
from ner import match_people

section = get_section(1, remove_endnote_tags=True)
nlp = spacy.load('en_coref_md')
doc = nlp(section)

match_entities = []
matcher, matches = match_people(doc)
print(matcher)

print("MATCHES:")
for m in matches:
    string = matcher.vocab.strings[m[0]]
    print(string)
    match_entities.append(string)


print("CLUSTERS")
print(len(doc._.coref_clusters))
print(doc._.coref_clusters)

print("\n\nMentions")
print(doc._.coref_clusters[1].mentions)
print(doc._.coref_clusters[1].mentions[-1])
print(doc._.coref_clusters[1].mentions[-1]._.coref_cluster.main)

print("\n\nTOKEN")
token = doc[-1]
print(token._.in_coref)
print(token._.coref_clusters)

print("\n\nSPAN")
span = doc[-1:]
print(span._.is_coref)
print(span._.coref_cluster.main)
print(span._.coref_cluster.main._.coref_cluster)
