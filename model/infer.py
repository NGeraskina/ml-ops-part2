import json

import numpy as np
import tensorflow as tf


def predict(text, next_words, model, max_sequence_len):
    for _ in range(next_words):
        with open("tokenizer.json") as f:
            data = json.load(f)
            tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)
        token_list = tokenizer.texts_to_sequences([text])[0]
        token_list = tf.keras.preprocessing.sequence.pad_sequences(
            [token_list], maxlen=max_sequence_len - 1, padding="pre"
        )
        predicted = np.argmax(model.predict(token_list), axis=1)
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                text += word + " "
    return text