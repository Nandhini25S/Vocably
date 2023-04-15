from vocably.grammercheck.grammerchecker import GrammerCheck

def test_grammer_check():
    checker=GrammerCheck()
    text="This sentences has has bads grammar."
    checker.correct(text)
