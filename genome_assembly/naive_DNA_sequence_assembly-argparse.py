#!/usr/bin/env python
# coding: utf-8

# In[9]:


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import argparse


# In[16]:


parser = argparse.ArgumentParser(prog='assembler', description='assembler', epilog='Start')
parser.add_argument('-i','--reads_input', required=True, type=str, metavar='fasta_name', help='fasta file with reads')
parser.add_argument('-k', default = 5, type=int, metavar='INT', help='lenght of k-mer')
parser.add_argument('-o','--output_contigs', default = 'out_assem.txt', type=str, metavar='txt_name', help='txt file ')


# In[ ]:


args = parser.parse_args()
args = args.__dict__


# In[ ]:


def receive_sequences(path):
    """
    
    path: a pathway to fasta file 
    
    return: a list of sequences from fasta file
    
    """
    sequences = list(SeqIO.parse(path, 'fasta'))
    
    return sequences


# In[1]:


def match(input_fasta, threshold = 6, output = 'out_seq.txt'):
    
    '''
    
    new_seqs: the list of input sequences
    ouput: name of output file 
    
    return : the list with alignment sequences 
    '''
    
    new_seqs = receive_sequences(input_fasta)
    threshold_iter = len(new_seqs)*10
    score = {0: 100}
    iteration = 0
    while (len(new_seqs) != 1) and (max(score.values()) >= threshold) and iteration < threshold_iter:
        iteration += 1
        score = {}
        a = new_seqs[0].seq
        for j in range(1, len(new_seqs)):
            b = new_seqs[j].seq
            aln = pairwise2.align.localms(a, b, 1, -1, -1, -1)
            if aln:
                aln = aln[0]
                score[j] = aln[2]
            else:
                score[j] = 0
                      
        for k in sorted(score, key=score.get, reverse=True):
            if score[k] >= threshold:
                pair_pos = k
                c = new_seqs[pair_pos].seq
                aln_true = pairwise2.align.localms(a, c, 1, -1, -1, -1)[0]
                fragment = aln_true[0][aln_true[3]:aln_true[4]]
                flag_len = aln_true[4] - aln_true[3]
                if (a.endswith(fragment) and c.startswith(fragment)):
                    new_seqs.pop(pair_pos)
                    new_seqs.pop(0)
                    new_seqs.append(SeqRecord(a + c[flag_len:]))
                    break
                elif (c.endswith(fragment) and a.startswith(fragment)):
                    new_seqs.pop(pair_pos)
                    new_seqs.pop(0)
                    new_seqs.append(SeqRecord(c + a[flag_len:]))
                    break
            else:
                temp = new_seqs[0]
                new_seqs.pop(0)
                new_seqs.append(temp)
    
    return new_seqs


# In[18]:


print(match(args['reads_input'], args['k']))


# In[ ]:




