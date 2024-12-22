from flair.nn import Classifier
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.tokenization import Tokenizer
from segtok.segmenter import split_single
from collections import Counter
import pandas as pd
import os


ner_tagger = SequenceTagger.load("flair/ner-english-ontonotes")
pos_tagger = Classifier.load("pos")


def get_named_entities(text: str, tagger=ner_tagger):
    sentence = [Sentence(sent, use_tokenizer=True) for sent in split_single(text)]
    tagger.predict(sentence)

    entities = []

    for token in sentence:
        for entity in token.get_spans("ner"):
            entity = str(entity)
            entities.append(entity)

    return entities


def get_most_frequent_words(dataset: str, k=10):

    split_str = dataset.split()

    counter = Counter(split_str)

    most_frequent = counter.most_common(k)

    return most_frequent


# POS categories https://huggingface.co/flair/pos-english


def get_parts_of_sentence(text: str, tagger=pos_tagger):

    sentence = Sentence(text)

    tagger.predict(sentence)

    return sentence


# path_stem = os.path.join("datasets")

# file_name = "ch3_colour_data_viz_suggestions_set_2"

# ner_output_path = os.path.join(path_stem, f"{file_name}_ner.csv")

# df = pd.read_csv(ner_output_path)

# df = df.head(3)


# ner_dataset = df["alma_metadata"].to_list()
# ner_dataset = " ".join(ner_dataset)

# tokenizer = Tokenizer()

# tokens = Tokenizer.tokenize(Tokenizer, ner_dataset)

# print(tokens)
# # most_common = get_most_frequent_words(ner_dataset)

# print(most_common)
