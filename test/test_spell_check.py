from vocably.spellcheck.checker import SpellCheck

def test_spellcheck():
    checker = SpellCheck()
    text = "christmas is celbrated on decembr 25 evry ear"
    assert (checker.correct(text) == "christmas is celebrated on december 25 every year")