
import math
import re

def load_vocab():
    vocab = {}
    with open("vocab.txt", "r") as f:
        vocab_terms = f.readlines()
    with open("idf_values.txt", "r") as f:
        idf_values = f.readlines()

    for (term, idf_value) in zip(vocab_terms, idf_values):
        vocab[term.rstrip()] = int(idf_value.rstrip())

    return vocab

def load_document():
     with open("document.txt", "r") as f:
        documents = f.readlines()
        #print('Number of documents: ', len(documents))


     return documents

def load_inverted_index():
    inverted_index = {}
    with open('inverted_index.txt', 'r') as f:
        inverted_index_terms = f.readlines()

    for row_num in range(0,len(inverted_index_terms),2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num+1].strip().split()
        inverted_index[term] = documents

     #print('Size of inverted index: ', len(inverted_index))
    return inverted_index

def load_linkes_of_ques():
    
    with open("../Leetcode question scrapper/Qdata/Qindex.txt","r")as f:
        links=f.readlines()

    return links  


vocab=load_vocab()
document=load_document()
inverted_index=load_inverted_index()
Qlink=load_linkes_of_ques()



def get_tf_dictionary(term):
    tf_dictionary={}
    if term in inverted_index:
        for doc in inverted_index[term]:
            if doc not in tf_dictionary:
                tf_dictionary[doc]=1
            else:
                tf_dictionary[doc]+=1

    for doc in tf_dictionary:
        # dividing the freq of the word in doc with the total no of words in doc indexed document
        tf_dictionary[doc]/=len(document[int(doc)])            
                
    return tf_dictionary             


def get_idf_values(term):
    return math.log( (1+len(document) )/ (1+vocab[term]) )



def calculate_sorted_order_of_documents(query_terms):
    potential_docs={}

    for term in query_terms:
        if (term not in vocab):
            continue

        tf_values_by_docs=get_tf_dictionary(term)
        idf_values=get_idf_values(term)

        #print(term, tf_values_by_docs, idf_values)
        
        for doc in tf_values_by_docs:
            if doc not in potential_docs:
                potential_docs[doc]=tf_values_by_docs[doc]*idf_values
            else:
                potential_docs[doc]+=tf_values_by_docs[doc]*idf_values
        #print(potential_docs)
        #divide the scores of each doc with no of query terms

        for doc in potential_docs:
            potential_docs[doc]/=len(query_terms)

        # sort in dec order acc to values calculated
        potential_docs = dict(sorted(potential_docs.items(), key =lambda item : item[1], reverse = True))


        # if no doc found
        if(len(potential_docs)==0):
            print("no matching quetion is found ,please search with more releavent terms")

        else:
             print("The Question links in Decreasing Order of Relevance are: \n")  
             for doc_index in potential_docs:
               print("Question Link:", Qlink[int(doc_index) - 1], "\tScore:", potential_docs[doc_index])  

query = input('Enter your query: ')
query_terms = [term.lower() for term in query.strip().split()]
calculate_sorted_order_of_documents(query_terms)