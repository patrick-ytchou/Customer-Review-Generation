## Yelp Restaurant Review Generation

### Background
Text Generation is a popular subfield for Natural Language Processing that aims to generate text based on some seed text. This text can be done via RNN / LSTM to deal with sequence text data. However, this task cannot be easily done on normal computer given the humongous amount of data the model has to train on.

Fortunately, new model training technologies have saved our lives. Transfer Learning is a learning technique in machine learning that focuses on transferring knowledge gained from training one problem to another similar task. For instance, we can use the neural network that are trained to classify cars to classify birds by changing later part of the model structure.

Another wonderful news is that there are some research labs dedicating to open-sourced machine learning models. In this notebook, we will utilize the GPT-2 model trained by OpenAI. GPT-2, Generative pretrained transformer 2, is a language model released in 2019 that are trained on 8 million web pages. It is a pretrained model with 1.5 billion parameters.

Thanks to the open-sourced model, we can download the parameters directly through Huggingface API and fine-tuned via yelp review data. By doing this we can make use of the pretrained parameters in GPT-2 to best suit our review data.

---
### Project Structure

- `Yelp Review Generation with Transfer Learning` shows the detailed model traninig process for the fined-tuned text generation model.
  
- `app.py` is the streamlit app for user's interaction to the model.
