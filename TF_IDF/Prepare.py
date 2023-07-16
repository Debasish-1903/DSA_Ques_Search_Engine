'''
    1. Read lines from the document 
    2. Preprocess the lines(document) and store it in documents[] list
    3. Create "vocab" as dictionary and store it in file
    4. Store preprocessed documents in file
    5. Store IDF(here term frequency) values of vocab terms in files
    6. Store Inverted-Index (in which document that term is present + term's frequency in that document)
'''
import sys
import os
import re


Qdata_folder="Leetcode question scrapper/Qdata"
target_str="Example 1:"

all_lines=[]

for i in range(1,2201):
    #adding body of the ith problem
    file_path=os.path.join(Qdata_folder,"{}/{}.txt".format(i,i))

    doc=""
    with open(file_path,"r",encoding="utf-8",errors="ignore")as f:
     lines=f.readlines()


    for line in lines:
         if target_str in line:
             break
         else: doc+=line

    all_lines.append(doc)     



    # adding heading of the ith question

head_path=os.path.join(Qdata_folder,"index.txt")

with open(head_path,"r",encoding="utf-8",errors="ignore") as f:
     headings=f.readlines()


for (i,heading) in enumerate(headings,0):
    if i<len(all_lines) :


      # removing the  ques No from the heading
       words=heading.split()

     # removing the Q No from the heading
       heading=' '.join(words[1:])
       # Now adding the remainging words in heading to the respective ques's body
       all_lines[i]+=heading




# read lines from index file
#with open("Leetcode question scrapper/Qdata/index.txt", "r", encoding="utf8",errors="ignore") as f:
 #  lines = f.readlines()
   

def preprocess(doc_txt):# remove problem no, and return a list of lowercase words
    #print(doc_txt)
      doc_txt = re.sub(r'[^a-zA-Z0-9\s-]', '', doc_txt)  # removing non alphanumeric chars
     #remove the leading numbers from string and remove all non alpha numeric characters,  make all characters lowercase
      terms=[term.lower()for term in doc_txt.strip().split()[1:]]
   # print (terms)
      return terms

vocab={} #it is dictionary    # word : no of docs that word is present in
documents=[]  #list            # all lists, with each list containing words of a document

for (index,line) in enumerate(all_lines):
    try:
       # print(index,line)
       tokens=preprocess(line)
       documents.append(tokens)
       
       tokens = set(tokens) # every thing is just counted 1 time
       for token in tokens:
            if token not in vocab:
                vocab[token]=1
            else: vocab[token]+=1     
       
    except UnicodeEncodeError: 
            print(line.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))


#print(documents[:5])    

vocab = dict( sorted(vocab.items(), key = lambda item : item[1], reverse = True) )



print('Number of documents:', len(documents))
print('Size of vocab:', len(vocab))
print('Sample document:', documents[0])

# Print the vocab dictionary using error handling for encoding issues
for key, value in vocab.items():
    try:
        print(key, value)
    except UnicodeEncodeError:
        print(key.encode(sys.stdout.encoding, errors='ignore').decode(sys.stdout.encoding), value)


# keys of vocab thus is a set of distinct words across all docs
#save them in vocab file
with open("TF_IDF/vocab.txt","w",encoding="utf-8",errors="ignore")as f:
    for key in vocab.keys():
        f.write("%s\n"%key)




#save the idf valuse
with open("TF_IDF/idf_values.txt","w",encoding="utf-8",errors="ignore")as f:
    for key in vocab.keys():
        f.write("%s\n"%vocab[key])


#save the documents(lists of words for each doc) 
with open("TF_IDF/documents.txt", "w", encoding = 'utf-8', errors = "ignore") as f:
    for doc in documents:
             f.write("%s\n" % doc)

inverted_index={}    # word : list of index of docs the word is present in.
                    # inserting word multiple times from same doc too, so that we even get the term freq from here itself
for (index,doc)in enumerate(documents,start=1):
     
     for token in doc:
         # print(index)
          if token not in inverted_index:
               inverted_index[token]=[index]
          else : inverted_index[token].append(index)  


#save the inverted index in a file 
with open("TF_IDF/inverted_index.txt","w",encoding="utf-8",errors="ignore")as f:
     for key in inverted_index.keys():
          f.write("%s\n"%key) 

          doc_indexes=" ".join([str(term)for term in inverted_index[key]])
          f.write("%s\n"%doc_indexes)            


