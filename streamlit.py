import streamlit as st
from transformers import pipeline


def app():
    st.title("Yelp Food Review Generator")
    
    text = """
    In this app, you can generate synthetic review for restaurants using transfer learning from OpenAI GPT-2 model.
    
    Notebook for detailed code: [Notebook](https://calendar.google.com/calendar/u/0/r/week)
    """
    st.markdown(text)
    generate_review = pipeline('text-generation', 
                        model = './gpt2', 
                        tokenizer = 'gpt2', 
                        config = {'max_length': 100})
    
    with st.form("user_input"):
        user_input = st.text_input("Please input your text snippet for the review.")
        length = st.number_input("Please input the maximum length of review you want to generate (max 100 words).", min_value = 1, max_value = 300, step = 1)
        submitted = st.form_submit_button("Generate Review")
        if submitted:
            result_1 = generate_review(user_input)[0]['generated_text']
            result_2 = generate_review(user_input)[0]['generated_text']
            result_3 = generate_review(user_input)[0]['generated_text']
            
            st.markdown("__You're 1st synthetic review:__")
            st.write(result_1)
            st.markdown("__You're 2nd synthetic review:__")
            st.write(result_2)
            st.markdown("__You're 3rd synthetic review:__")
            st.write(result_3)
    

if __name__ == '__main__':
    app()