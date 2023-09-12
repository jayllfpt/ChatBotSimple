from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

def load_data(n_samples = 1000):
    df1 = pd.read_csv("Data/S08_question_answer_pairs.txt", sep = '\t')
    df2 = pd.read_csv("Data/S09_question_answer_pairs.txt", sep = '\t')
    df3 = pd.read_csv('Data/S10_question_answer_pairs.txt', sep = '\t', encoding = 'ISO-8859-1')
    data = pd.concat([df1, df2, df3], ignore_index= True)
    data = data.dropna()
    data = data.sample(n_samples, ignore_index= True)
    data = data[['Question', 'Answer']]
    print('data loaded')
    return data

def load_model(model_name = 'paraphrase-albert-small-v2'):
    model = SentenceTransformer(model_name)
    print('model loaded')
    return model

def embeddings_data(data: pd.DataFrame, model):
    questionsData = data.Question.to_list()
    data_embeddings = model.encode(questionsData)
    # data_embeddings = np.load("embedded-qa.npy")
    print('data embedded')
    return data_embeddings

def getAnswer(questionList, data, data_embeddings, model):
    similarityQuestion = []
    answerList = []
    scoreList = []
    for question in questionList:
        question_embedding = model.encode(question)

        similarity_score = cosine_similarity(
            [question_embedding],
            data_embeddings
        ).flatten()

        max_score_index = np.argmax(similarity_score)

        scoreList.append(similarity_score[max_score_index])

        answerList.append(data.at[max_score_index, 'Answer'])
        
        similarityQuestion.append(data.at[max_score_index, 'Question'])

    _resultdata = {'Question': questionList, 'Simiarity Q': similarityQuestion, 'Score': scoreList, 'Answer': answerList}
    return _resultdata
    # answer_df = pd.DataFrame(_resultdata)
    # return answer_df

data = load_data()
model = load_model()
data_embeddings = embeddings_data(data, model)
print(getAnswer(["What serves as the capital of Indonesia?"], data, data_embeddings, model))