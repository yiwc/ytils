print("ytils: set of useful functions for data science")

import numpy as np

def get_hash(unique_string,length=20)->str:
    import hashlib
    hash_object = hashlib.sha256(unique_string.encode())
    hex_dig = hash_object.hexdigest()[:length]
    return hex_dig


def cosine_dist(a,b):
    assert len(a.shape)==2
    assert len(b.shape)==2
    return 1-(a*b).sum(1)/np.sqrt(np.sum(a*a,1)*np.sum(b*b,1))


def watch_distribution(data:np.array):
    assert len(data.shape)==1
    for k in [1,2,3,4,5,10,20,30,40,50,60,70,80,90]:
        print(str({k:np.percentile(data,k)}))