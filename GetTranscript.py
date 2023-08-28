from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline


outls = []

strTranscript = """"""

# tx = YouTubeTranscriptApi.get_transcript('q6fwHkoSMsE')
tx = YouTubeTranscriptApi.get_transcript('89-iRCL4i4Y')
for i in tx:
    outtxt = (i['text']) #picks out the text, if not used we get, a json dictionary
    outls.append(outtxt) 

    with open("op.txt", 'a') as opf:
        opf.write(outtxt + "\n")

summarizer = pipeline('summarization')

# Reading the file into strTranscript
with open("op.txt", "r") as opf:
    strTranscript = opf.read()

# print(strTranscript)

#dividing the text into chunks of 1000 for summarization
num_iters = int(len(strTranscript)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
    # start = 0
    start = i*1000
    end = (i + 1) * 1000
    out = summarizer(strTranscript[start:end], min_length = 3, max_length = 8)
    out = out[0]
    out = out['summary_text']
    summarized_text.append(out)

for line in summarized_text:
    print("\n",line)