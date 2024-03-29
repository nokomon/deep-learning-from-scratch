import sys
sys.path.append('..')

import pickle
from common.util import *

pkl_file = 'skipgram_params_W_in_W_out.pkl'
with open(pkl_file, 'rb') as f:
    params = pickle.load(f)   # keys: word_vecs, word_to_id, id_to_word
    word_vecs = params['word_vecs']
    word_to_id = params['word_to_id']
    id_to_word = params['id_to_word']

querys = ['you', 'year', 'car', 'hotel', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)

# 유추(analogy) 작업
print('-'*50)
analogy('king', 'man', 'queen',  word_to_id, id_to_word, word_vecs)
analogy('take', 'took', 'go',  word_to_id, id_to_word, word_vecs)
analogy('car', 'cars', 'child',  word_to_id, id_to_word, word_vecs)
analogy('good', 'better', 'bad',  word_to_id, id_to_word, word_vecs)
# analogy('nice', 'bad', 'happy',  word_to_id, id_to_word, word_vecs)