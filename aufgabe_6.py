import math

alphabet = ['a', 'e', 'i', 'o', 'u']
probabilities = [0.25, 0.2, 0.1, 0.3, 0.15]
lengths = [2,2,3,2,3]

L = sum(p * l for p, l in zip(probabilities, lengths))

H = -sum(p * math.log2(p) for p in probabilities )

R = L - H

