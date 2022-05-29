"""Creates bar chart from sentence after translating it to another lang"""

from googletrans import Translator, constants
from pprint import pprint
from collections import defaultdict

text = "Hail and well met fellow traveler, can I interest you in any of my \
wares today?"

translator = Translator()

text_span = translator.translate(text, dest="es").text.lower()
print(text_span)

bar = defaultdict(list)
for letter in text_span:
    if letter != " ":
        bar[letter].append(letter)

pprint(bar)