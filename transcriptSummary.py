from transformers import BartTokenizer, BartForConditionalGeneration

# Load the pre-trained model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Load the transcript file generated using genTranscript.py
transcript_file = 'transcript.txt'

with open(transcript_file, 'r', encoding='utf-8') as f:
    transcript = f.read()

# Tokenize and encode the transcript
inputs = tokenizer.encode("summarize: " + transcript, return_tensors="pt", max_length=1024, truncation=True)

# Generate the summary of max 150 words or 1 liner
summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print("One-line Summary:", summary)
