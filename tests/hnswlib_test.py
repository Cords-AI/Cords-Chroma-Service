import hnswlib
import os
import json
from typing import Optional, Sequence, Dict, Set, List, cast

index = hnswlib.Index('l2', 1536)

folder = os.path.abspath('data-2024-06-16/text-embedding-ada-002/60bec353-834c-491b-83b4-52bb38b1e225')

index.load_index(
    folder,
    is_persistent_index=True,
    max_elements=262090,
)

index.set_ef(16)
index.set_num_threads(12)

k = 100

json_file = os.path.abspath('tests/query_vectors.json')
with open(json_file, 'r') as file:
    query_vectors = json.load(file)

json_file = os.path.abspath('tests/labels-crash.json')
with open(json_file, 'r') as file:
    labels: Set[int] = set(json.load(file))

filtered = []
def filter_function(label: int) -> bool:
    if label in labels:
        filtered.append(label)
    return label in labels

if k > len(labels):
    k = len(labels)

result_labels, distances = index.knn_query(
    query_vectors, k=k, filter=filter_function
)
