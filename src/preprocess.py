from src.prepro.data_loader import load_txt, entities_decifer, Triplets

def preprocess(path, dataset='train'):

    data = load_txt(path, dataset="train")
    data = entities_decifer(data)
    triplets = Triplets(data)

    return triplets