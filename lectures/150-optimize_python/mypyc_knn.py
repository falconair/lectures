import math
from typing import List
import numpy as np
from numpy.typing import NDArray


def euclidean_distance_mypyc(
        p1: NDArray[np.float64]
        , p2: NDArray[np.float64]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))


def knn_python_mypyc(
    X_train: NDArray[np.float64],        # shape (n_samples, n_features)
    y_train: NDArray[np.int64],          # shape (n_samples,)
    X_test: NDArray[np.float64],         # shape (n_test, n_features)
    k: int
) -> List[int]:                          # returns list of predicted labels (ints)
    predictions: List[int] = []
    for test_point in X_test:
        distances: List[tuple[float, int]] = []
        for i, train_point in enumerate(X_train):
            dist = euclidean_distance_mypyc(test_point, train_point)
            distances.append((dist, int(y_train[i])))  # cast in case numpy type
        distances.sort(key=lambda x: x[0])

        nearest_labels: List[int] = [label for (_, label) in distances[:k]]

        # Majority vote, manual count
        best_label: int | None = None
        best_count = 0
        for label in set(nearest_labels):
            count = nearest_labels.count(label)
            if count > best_count:
                best_count = count
                best_label = label

        # best_label can’t be None here if k > 0
        predictions.append(best_label if best_label is not None else -1)
    return predictions
