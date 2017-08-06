rna_map = {
        'G': 'C',
        'C': 'G',
        'A': 'U',
        'T': 'A'
}

def to_rna(dna):
    dnalist = list(dna)
    if set(dna) > set(rna_map.keys()):
        return ''
    return ''.join([rna_map.get(x, '') for x in dnalist])
