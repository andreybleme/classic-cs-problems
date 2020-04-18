from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def str_to_gene(gene_str: str):
  gene: Gene = []
  for i in range(0, len(gene_str), 3):
    if (i + 2) >= len(gene_str):
      return gene
    codon: Codon = (Nucleotide[gene_str[i]], Nucleotide[gene_str[i + 1]], Nucleotide[gene_str[i + 2]])
    gene.append(codon)
  return gene

my_gene: Gene = str_to_gene(gene_str)

def linear_contains(gene: Gene, key_codon: Codon):
  for codon in gene:
    if codon == key_codon:
      return True
  return False

# Linear search
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
aaa: Codon = (Nucleotide.A, Nucleotide.A, Nucleotide.A)
print('Contains acg {}'.format(linear_contains(my_gene, acg)))
print('Contains aaa {}'.format(linear_contains(my_gene, aaa)))

def binary_contains(gene: Gene, key_codon: Codon):
  low: int = 0
  top: int = len(gene) - 1
  while low <= top:
    mid: int = (low + top) // 2
    if (gene[mid] > key_codon):
      top = mid - 1
    elif (gene[mid] < key_codon):
      low = mid + 1
    else:
      return True
  return False

# Binary search
my_sorted_gene: Gene = sorted(my_gene)
print('Contains acg {}'.format(binary_contains(my_sorted_gene, acg)))
print('Contains aaa {}'.format(binary_contains(my_sorted_gene, aaa)))
