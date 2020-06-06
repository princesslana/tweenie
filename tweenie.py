import logging
import json
import csv
import numpy as np
from emoji import emojis
from smalld import Intent, SmallD

from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis
from torchmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH

THRESHOLD = 0.10

logging.basicConfig(level=logging.INFO)

def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]

logging.info('Tokenizing using dictionary from %s', VOCAB_PATH)
with open(VOCAB_PATH, 'r') as f:
    vocabulary = json.load(f)

st = SentenceTokenizer(vocabulary, 2000)

logging.info('Loading model from %s.', PRETRAINED_PATH)
model = torchmoji_emojis(PRETRAINED_PATH)
logging.debug(model)

smalld = SmallD(intents=Intent.GUILD_MESSAGES)

@smalld.on_message_create()
def on_message(msg):
    if not msg.content:
        return

    tokenized, _, _ = st.tokenize_sentences([msg.content])
    prediction = model(tokenized)[0]

    top = top_elements(prediction, 5)

    logging.info("Message: %s, Reacts: %s", msg.content, "".join(str((emojis[t], prediction[t])) for t in top))

    for t in top:
        if prediction[t] > THRESHOLD:
            react_with = emojis[t]
            smalld.put(f"/channels/{msg.channel_id}/messages/{msg.id}/reactions/{react_with}/@me")

smalld.run()
