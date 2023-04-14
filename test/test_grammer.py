from vocably.grammercheck.Grammer_checker import GrammerCheck

def test_grammer_check():
    checker=GrammerCheck()
    text="This sentences has has bads grammar."
    print(checker.correct(text))
    assert (checker.correct(text) == "This sentence has bad grammar.")