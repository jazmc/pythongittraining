# Kirjoita postinumerot-moduulin testit tähän tiedostoon
from postinumerot import get_postal_codes

def test_find_only_one_postalcode():
    # Korvatunturi = 99999
    assert get_postal_codes('Korvatunturi') == 'Postinumerot: 99999'

def test_find_many_postalcodes():
    # Klaukkala = 01800, 01801, 01820, 01840
    assert get_postal_codes('Klaukkala') != 'Tuntematon postitoimipaikka'

def test_find_zero_postalcodes():
    # Tyhjälä = ei osumia
    assert get_postal_codes('Tyhjälä') == 'Tuntematon postitoimipaikka'

def test_ignore_spaces():
    assert get_postal_codes('smartpost') == get_postal_codes('smart post')