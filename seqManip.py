#! /usr/bin/env python

#module containing home made sequence object
import sequenceObj

#Jeremy's sequence
jSequence="aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
#create sequenceObject from imported module
jSequenceObject = sequenceObj.sequenceObject(jSequence)

#print various values required by the assignment
print("The length of the provided sequence is:")
print(str(len(jSequenceObject.sequence))+"\n")

print("The RNA equivalent is:")
print(jSequenceObject.RNA + "\n")

print("The Reverse Compliment is:")
print(jSequenceObject.reverse + "\n")

print("The 13th and 14th codons from the sequence are:")
print(jSequenceObject.sequence[38:44] +"\n")

translation=jSequenceObject.translateSequence(jSequenceObject.sequence,1)
print("The amino acid translation from the first reading frame is:")
print(translation +"\n")
