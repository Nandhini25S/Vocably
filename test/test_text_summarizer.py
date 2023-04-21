from vocably.summarizer.summarizer import Summarizer


def test_summarize():
    checker = Summarizer()
    text = """Hi LeetCoders! We have some exciting news! LeetCode launched a new problem category for JavaScript, please checkout this post to learn about the new problem category: JavaScript problems."""
    print(checker.summarizer(text))
    
test_summarize()