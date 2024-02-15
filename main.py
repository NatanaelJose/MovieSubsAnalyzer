import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import os
from tqdm import tqdm

def preprocess_text(text, stop_words):
    tokens = word_tokenize(text.lower())
    words = [word for word in tokens if word.isalpha() and word not in stop_words]
    return words

def process_subtitle_file(file_path, stop_words, word_counter, sentence_counter):
    with open(file_path, 'r', encoding='latin1') as subtitle_file:
        text = subtitle_file.read()
        words = preprocess_text(text, stop_words)
        word_counter.update(words)
        sentences = sent_tokenize(text.lower())
        sentence_counter.update(sentences)

def main():
    nltk.download('punkt')
    nltk.download('stopwords')

    subtitles_folder = "" 

    stop_words = set(stopwords.words('english'))
    word_counter = Counter()
    sentence_counter = Counter()

    subtitle_files = [file for file in os.listdir(subtitles_folder) if file.endswith(".srt")]
    total_files = len(subtitle_files)

    with tqdm(total=total_files, desc="Processing files") as pbar:
        for file in subtitle_files:
            file_path = os.path.join(subtitles_folder, file)
            process_subtitle_file(file_path, stop_words, word_counter, sentence_counter)
            pbar.update(1)

    print("Most common words:")
    for word, frequency in word_counter.most_common(40):
        print(f"{word}: {frequency}")

    print("\nMost common sentences:")
    for sentence, frequency in sentence_counter.most_common(40):
        print(f"{sentence}: {frequency}")

if __name__ == "__main__":
    main()
