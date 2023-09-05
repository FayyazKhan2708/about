import re
from collections import Counter

def tokenize_text(text):
    sentences = re.split(r"\s+", text)
    return sentences
    
def calculate_sentence_scores(sentences, stopwords):
    word_frequencies = Counter()
    sentence_scores = {}

    for sentence in sentences:
        words = re.findall(r'\w+', sentence)
        for word in words:
            if word.lower() not in stopwords:
                word_frequencies[word] += 1
        # print(word_frequencies)

    max_frequency = max(word_frequencies.values())

    for sentence in sentences:
        words = re.findall(r'\w+', sentence)
        for word in words:
            if word.lower() not in stopwords:
                sentence_scores[sentence] = word_frequencies[word] / max_frequency

    return sentence_scores

def generate_summary(text, num_sentences=10):
    stopwords = set(["the", "in", "and", "of", "a", "to", "for", "an", "is", "on", "with", "as", "by"])

    sentences = tokenize_text(text)
    sentence_scores = calculate_sentence_scores(sentences, stopwords)
    # print(sentence_scores)

    ranked_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    selected_sentences = ranked_sentences[:num_sentences]
    # print(selected_sentences)

    summary = [sentence for sentence, score in selected_sentences]
    summary = ' '.join(summary)
    return summary

# Input text to be summarized
input_text = "The action or process of defining. The act of defining; determination of the limits. A product of defining. The action or power of describing, explaining, or making definite and clear."


# Summarize the input text
summary = generate_summary(input_text)

# Print the summary
print(summary)
