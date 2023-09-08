def DNA_strand(dna):
    asdf = list(dna)
    for index, item in enumerate(asdf):
        if item =='A':
            asdf[index] = 'T'
        elif item =='T':
            asdf[index] = 'A'
        elif item =='C':
            asdf[index] = 'G'
        elif item =='G':
            asdf[index] = 'C'
        
    return "".join(asdf)
print(DNA_strand("ATTGC"))


#best
def DNA_strand(dna):
  return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])