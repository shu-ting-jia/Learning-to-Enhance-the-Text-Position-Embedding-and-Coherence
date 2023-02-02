i=0
listour=[]
listsin=[]
listref=[]
listall=[]
with open("/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/checkpoints/wmt14_en_de/transformer/evaluate/evaluate.log.sys", "r") as f:
    for line in f:
        list2 = line.split()
        #print(line,len(list2))
        listour.append(line)
        i=i+1

with open("/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/checkpoints/wmt14_en_de_shortorig/transformer/evaluate/evaluate.log.ref", "r") as f:
    for line in f:
        list2 = line.split()
        #print(line,len(list2))
        listref.append(line) 
with open("/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/checkpoints/wmt14_en_de_shortorig/transformer/evaluate/evaluate.log.sys", "r") as f:
    for line in f:
        list2 = line.split()
        #print(line,len(list2))
        listsin.append(line)
print(len(listref),len(listour),len(listsin))
for c in range(len(listour)):
    listall.append(listref[c])
    listall.append(listour[c])
    listall.append(listsin[c])

path = '/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/examples/translation/cmp'
f = open(path, 'w')
f.writelines(listall)
f.close()
