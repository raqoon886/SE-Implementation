import os
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import WordNetError

def load_txt(path, dataset="train"):
    if dataset not in ['train', 'valid', 'test']:
        raise AssertionError('invalid dataset type. select : [train, valid, test]')

    filename = f"wordnet-mlj12-{dataset}.txt"
    with open(os.path.join(path, filename), 'r') as f:
        data = f.read()

    data = data.split('\n')[:-1]
    data = [i.split('\t') for i in data]

    return data


def entities_decifer(data):

    '''
    wordnet synset id to synset object
    :param data: list of triplets
    :return: list of triplets(decifered)
    '''

    decifered_data = []
    for i, a in enumerate(data):
        tmp = []
        try:
            tmp.append(wn.synset_from_pos_and_offset("n", int(a[0])))
            tmp.append(a[1])
            tmp.append(wn.synset_from_pos_and_offset("n", int(a[2])))
            decifered_data.append(tmp)
        except:
            continue

    return decifered_data


class Triplets():
    def __init__(self, data):
        self.data = data
        self.heads = [i[0] for i in self.data]
        self.rels = [i[1] for i in self.data]
        self.tails = [i[2] for i in self.data]

        entities = []
        entities.extend(self.heads)
        entities.extend(self.tails)
        self.entities = list(set(entities))

    def __len__(self):
        return len(self.data)
