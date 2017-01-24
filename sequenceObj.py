#! /usr/bin/env python

#codon/amino acid dictionary
#key = RNA codon, value = amino acid abbreviation
#disclaimer: I totally stole this from the internet so I didn't have to type it all
#it might not match the one given in class exactly
aaDict = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


#sequence object class, contains a sequence and related information
class sequenceObject:
    #transform a sequence into its RNA equivalent by replacing t with u
    def DNAtoRNA(self,sequence):
        """
            -input DNA sequence and replaces the thymine with uracil (T -> U)
            -assumes sequence is upper case; sequence passed to sequence object will already be upper
        """
        RNAsequence=sequence.replace("T","U")
        return RNAsequence
    
    #return the reverse compliment for a sequence
    #handles ambiguous characters and missing characters
    def reverseCompliment(self,sequence):
        """
            -input DNA/RNA sequence and returns the reverse compliment
            -handles missing/ambiguous characters
        """
        reverseComp=""
        for character in sequence[::-1]:
            if character == "A":
                newCharacter="T"
            elif character == "C":
                newCharacter="G"
            elif character == "G":
                newCharacter="C"
            elif character == "T":
                newCharacter="A"
            elif character == "N":
                newCharacter="N"
            elif character == "?":
                newCharacter="?"
            else:
                #throw an error about not being DNA sequence
                #pass for now until throw/catch set up
                pass
            #one way to add more information to a preexisting variable
            reverseComp=reverseComp + newCharacter
        return reverseComp
            
    #takes RNA sequence and then translates it into AA
    #want to check for DNA or RNA here? Or put in protection elsewhere?
    def translateSequence(self,sequence,frame):
        """
            -input DNA sequence and reading frame, returns amino acid sequence
            -amino acid dictionary doesn't currently support missing/ambiguous characters, so neither does this function
        """
        #initialize the string that will become the amino acid sequence
        aaString=""
        #use the sequence if reading frame is 1-3
        if frame == 1 or frame == 2 or frame== 3:
            #convert sequence to RNA
            RNA=self.DNAtoRNA(sequence)
            #shift to make 0 indexed
            newFrame = frame - 1
            #loop over sequence, grab codons, translate via amino acid dictionary
            for i in range(newFrame,len(RNA))[::3]:
                #needs to handle what happens when there's not an even multiple of 3
                #the try/except will handle any index errors that pop up
                try:
                    codon=RNA[i:i+3]
                    aaString+=aaDict[codon]
                except:
                    pass
            return aaString
        #need reverse compliment for reading frames in the other direction
        elif frame == 4 or frame == 5 or frame == 6:
            #get reverse compliment and change to RNA
            reverse = self.reverseCompliment(sequence)
            RNA= self.DNAtoRNA(reverse)
            #0 index
            newFrame= frame-4
            
            for i in range(newFrame,len(RNA))[::3]:
                try:
                    codon=RNA[i:i+3]
                    aaString+=aaDict[codon]
                except:
                    pass
            return aaString
        
        #deal with any incorrectly input reading frames (i.e. not 1-6)
        else:
            return "error"
    
    #initialize method
    def __init__(self, originalSequence):
        """
            initialize method; stores sequence variable, as well as generating the RNA and reverse sequences automatically
        """
        self.sequence=originalSequence.upper()
        self.RNA= self.DNAtoRNA(self.sequence)
        self.reverse= self.reverseCompliment(self.sequence)