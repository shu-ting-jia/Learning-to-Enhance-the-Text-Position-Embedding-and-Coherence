i=0
listnew=[]
listindex=[]

with open("/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/examples/translation/iwslt14.tokenized.de-en/test.de", "r") as f:
    for line in f:
        list2 = line.split()
        #print(line,len(list2))
        if(len(list2)>40):
            listnew.append(line)
            listindex.append(i)
            #print(i)
        i=i+1
    
path = '/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/examples/translation/iwslt14.tokenized.de-en/outtest.de'
f = open(path, 'w')
f.writelines(listnew)
f.close()
print(len(listindex))        
listnewde=[]
listsave=[]
i=0
with open('/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/examples/translation/iwslt14.tokenized.de-en/test.en', 'r') as f:
    for line in f:
        listnewde.append(line)
        
print(len(listnewde))
for i in listindex:
    listsave.append(listnewde[i])

print(len(listsave))

path = '/root/Disentangled-Mask-Attention-in-Transformers/MT/Fairseq/examples/translation/iwslt14.tokenized.de-en/outtest.en'
f = open(path, 'w')
f.writelines(listsave)
f.close()