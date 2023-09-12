# ChatBotSimple
First project - first week internship in [FPT QAI](https://quynhon.ai).
<br>
However, this project **has not finished** yet.
# Run
simply clone then <br>
``` python run.py ```
# ScreenShot
![screen shot](https://github.com/jayllfpt/ChatBotSimple/blob/main/chatapp/screenshot.png)
# Data
Full data at ```chatapp/chatbot/Data``` <br>
I have also generated some testing data (paraphrase using ChatGPT) [here](https://github.com/jayllfpt/ChatBotSimple/blob/main/chatapp/test_data.xlsx)
# Frontend
Using HTML/ CSS/ Js. <br> Luckily, I got a template from [ScottWindon - CodePen](https://codepen.io/ScottWindon/pen/yLVgZjp)
# Backend
Data used: [QA Dataset - Kaggle](https://www.kaggle.com/datasets/rtatman/questionanswer-dataset)
<br>
Using pretrain model [paraphrase-albert-small-v2](https://huggingface.co/sentence-transformers/paraphrase-albert-small-v2) along with [Sentences Transformer](https://www.sbert.net)
<br>
Deploy model and create web app using Flask and SocketIO. (I followed the tutorial [here](https://youtu.be/AMp6hlA8xKA?si=xjD4v0etZFLrTz_J) )
<br>
Method: Encode given data and input question with **paraphrase-albert-small-v2**, then using **cosine similarity** to findout the most similarity question. Then give back the corresponding answer.
# Future work
Apply more and more models for comparison - learning purpose :)
<br>
Apply [Qdrant](https://qdrant.tech) instead of read from numpy.ndarray
<br>
Packaging using [Docker](https://www.docker.com)
<br>
