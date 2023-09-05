import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import json
from glob import glob
from models import *
from pprint import pprint


def create_word_cloud(texts):
    # Combine all the texts into one string
    combined_text = " ".join(texts)

    # Tokenize the combined text into words (you can use more advanced tokenization methods if needed)
    words = re.findall(r'\b\w+\b', combined_text.lower())  # Using regex for basic tokenization

    # Define a regular expression pattern to match English words
    english_word_pattern = re.compile(r'^[a-zA-Z]+$')

    # Filter out non-English words
    english_words = [word for word in words if english_word_pattern.match(word)]

    # Join the English words into a single string for word cloud generation
    text_for_wordcloud = " ".join(english_words)

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_for_wordcloud)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    # Save the word cloud to a file
    plt.savefig("light_output.png", bbox_inches='tight', dpi=300)
    plt.close()

    wordcloud = WordCloud(width=800, height=400, background_color='black', colormap='viridis', contour_color='white').generate(text_for_wordcloud)
    # Display the word cloud using matplotlib
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

    # Save the word cloud to a file
    plt.savefig("dark_output.png", bbox_inches='tight', dpi=300)
    plt.close()




user = ""
msgs = []

for message_json in glob(f"data/messages/inbox/{user}/message_*.json"):
    with open(message_json) as f:
        data = json.load(f)
    msgs.extend(data["messages"])

parsed = parse_messages(msgs)


# Example usage:
texts = [im.text for im in parsed if im.text is not None]

create_word_cloud(texts)
