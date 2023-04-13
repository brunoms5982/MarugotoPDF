import genanki
from pypdf import PdfReader
import regex
from open import get_text
my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])
jp,ro = get_text()
my_note = genanki.Note(model=my_model,fields=[jp[0], ro[0]])
my_deck = genanki.Deck(2059400110,'Marugoto x')
my_deck.add_note(my_note)
genanki.Package(my_deck).write_to_file('output.apkg')
