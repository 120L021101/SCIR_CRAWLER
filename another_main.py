# with open(file='all_chengyu.txt', mode='r', encoding='utf-8') as fr:
#     with open(file='chengyu.txt', mode='r', encoding='utf-8') as fr2:
#         with open(file='save.txt', mode='w', encoding='utf-8') as fw:
#             set1 = set()
#             for line in fr.readlines():
#                 word = line.strip()
#                 set1.add(word)
#             for line in fr2.readlines():
#                 word = line.strip()
#                 if word not in set1:
#                     fw.write(word + '\n')

seq = '''
CTTAGCGATACTCTGTTTTCCCTGGATCGGTATCTCCCTACGGAGGTCGAGTACTCGGAAGCAGCTTGCTTTAATTCTGCTACAAGCAGCCAGTGGGAGCGAATCATGAGCTACTGTACGAATATTCTACGAATGGTTTCGACGCACTCCTGTCTGCCATTAGTCTTAGTGGTGTGCCACGGCCGGACTCACGCAAACGGTCCCAAGCCGGCGGAAAAGAGCTAGCCGTTATCCTACGAGGGAGACCAGAGACTATTATCAGCGCCTCAAAAAAAAAAAAAAAAACACCAGACTCGGGGGTTCGTGGAGGGAGGGCGATAGGCTAGGGAAAGACTTGCACGGAAGCTTGAGTCGAGCCTCTCCAGACAGAGCGGCATCCCCGCAAAAGATTAGAGATAGTTACATCGTGTGACAAATAGGTTTTTGCACACAGCAGCCTCACCTGCTAGGGCCGGGCTTCATCCAAAGTCAAGGTCCAAACAAAGCCTAGCTGAATTCCTATGGTCTGGCGTTGACGATGGTCATATTCTAGACTCTTACTCAAATGGCCAT'''.replace('\n', '')
print(len(seq))

seq = """43705950	43706487"""
print(int(seq.split('\t')[1]) - int(seq.split('\t')[0]))