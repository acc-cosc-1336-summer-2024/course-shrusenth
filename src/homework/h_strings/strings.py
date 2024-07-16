def get_hamming_distance(dna1, dna2):
   
    if len(dna1) != len(dna2):
        raise ValueError("Strings must be of the same length")
    
    distance = sum(1 for a, b in zip(dna1, dna2) if a != b)
    return distance

def get_dna_complement(dna):
   
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_complement = ''.join(complement[base] for base in reversed(dna))
    return reverse_complement
