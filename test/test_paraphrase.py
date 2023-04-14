from vocably.paraphraser.paraphrase import Paraphraser

def test_paraphraser():
    checker = Paraphraser()
    text = """Hi LeetCoders! We have some exciting news! LeetCode launched a new problem category for JavaScript, please checkout this post to learn about the new problem category: JavaScript problems."""
    print(checker.paraphrase(text))
    #assert (checker.paraphrase(text) == """Salut, LeetCoders! We've got some thrilling news! Please read this post to find out more about the new problem category for JavaScript that LeetCode has launched: JavaScript difficulties.""")    

test_paraphraser()

