# ChatBotSimple
First project - first week internship in [FPT QAI](https://quynhon.ai).
<br>
However, this project **has not finished** yet.
# Run
simply clone then <br>
``` python run.py ```
# Frontend
Using HTML/ CSS/ Js. <br> Luckily, I got a template from [ScottWindon - CodePen](https://codepen.io/ScottWindon/pen/yLVgZjp)
# Backend
Data used: [QA Dataset - Kaggle](https://www.kaggle.com/datasets/rtatman/questionanswer-dataset)
<br>
Using pretrain model [paraphrase-albert-small-v2](https://huggingface.co/sentence-transformers/paraphrase-albert-small-v2) along with [Sentences Transformer](https://www.sbert.net)
<br>
Method: Encode given data and input question with **paraphrase-albert-small-v2**, then using **cosine similarity** to findout the most similarity question. Then give back the corresponding answer.
