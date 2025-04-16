import random
import math

def sample(num_candidates, width, height, samples):
    best_candidate = None
    best_distance = 0
    
    # Iterate through a number of candidate points
    for _ in range(num_candidates):
        # Generate a random candidate point within the given width and height
        c = [random.uniform(0, width), random.uniform(0, height)]
        
        # Find the closest sample point to the candidate and calculate the distance
        d = distance(find_closest(samples, c), c)
        
        # Update best candidate and best distance if this one is better
        if d > best_distance:
            best_distance = d
            best_candidate = c
    
    # Return the best candidate point found
    return best_candidate

# Finds the closest point in the list 'samples' to the point 'c'
def find_closest(samples, c):
    closest = None
    min_dist = float('inf')
    
    for sample in samples:
        dist = distance(sample, c)
        if dist < min_dist:
            min_dist = dist
            closest = sample
    
    return closest

# Calculates the Euclidean distance between two points 'a' and 'b'
def distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)

# Example usage
num_candidates = 10  # Number of candidate points to consider
width = 100  # Width of the area
height = 100  # Height of the area
samples = [[10, 20], [30, 40], [50, 60]]  # Existing sample points

new_sample = sample(num_candidates, width, height, samples)
print(new_sample)  # Prints the best candidate point

arr = ["asdb",1231, "Nome", "Casa", "Fruta", "Rapadura"]

for el in enumerate(arr):
    print(el)


def multi(nume):
    r = nume * nume
    print(r)

pessoa = {
    'nome': 'Diego',
    'sobrenome': 'Go',
    'idade': 37,
    'altura': 1.79,
    'endereco' : [
        {'rua': 'anibaldo', 'numero': 719 },
        {'rua': 'via plaermo', 'numero': 41}
    ]
}

print(pessoa, type(pessoa ))
