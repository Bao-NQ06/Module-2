import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vi_data_df = pd . read_csv ("Module-2\\week4\\vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]

tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
# print(context_embedded.toarray()[7][0])


def tfidf_search ( question , tfidf_vectorizer , top_d=5) :
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(context_embedded,query_embedded)

    results = []
    for idx in cosine_scores.argsort()[-top_d:][:: -1]:
        doc_score = {
        'id': idx ,
        'cosine_score': cosine_scores [ idx ]
        }
        results . append ( doc_score )
    return results

# Example 1:
# question = vi_data_df.iloc[0]['question']
# results = tfidf_search( question , tfidf_vectorizer , top_d =5)
# print(results[0]['cosine_score'])
# for result in results:
#     print("Id: ", result['id'])
#     print("Score: ", result['cosine_score'])
#     print(vi_data_df.iloc[result['id'], 2])
#     print("=======")
    
    
    
    
def corr_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    corr_scores = np.corrcoef(
        query_embedded.toarray()[0],
        context_embedded.toarray()
    )
    corr_scores = corr_scores[0][1:]
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score':corr_scores[idx]
        }
        results.append(doc)
    return results

# Example 2:
# question = vi_data_df.iloc[5]['question']
# print("Question: ", question)
# results = corr_search(question, tfidf_vectorizer)
# for result in results:
#     print("Id: ", result['id'])
#     print("Score: ", result['corr_score'])
#     print(vi_data_df.iloc[result['id'], 2])
#     print("=======")