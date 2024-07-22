def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The DNA sequences must be of equal length.")
    
    mismatches = sum(1 for a, b in zip(list1, list2) if a != b)
    return mismatches / len(list1)

def get_p_distance_matrix(dna_sequences):
    n = len(dna_sequences)
    p_distance_matrix = [[0.0] * n for _ in range(n)]  # Initialize matrix with zeros

    for i in range(n):
        for j in range(i + 1, n):  # Avoid redundant calculations (matrix is symmetric)
            distance = get_p_distance(dna_sequences[i], dna_sequences[j])
            p_distance_matrix[i][j] = distance
            p_distance_matrix[j][i] = distance  # Fill in the symmetric part
    
    return p_distance_matrix

dna_sequences = [
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
    ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],
    ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],
    ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
]

result_matrix = get_p_distance_matrix(dna_sequences)

for row in result_matrix:
    print(" ".join(f"{val:.5f}" for val in row))
