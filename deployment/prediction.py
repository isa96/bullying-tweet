# Library Streamlit
import streamlit as st

# Library Load Model
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

# Library Pre-Processing
from nltk.stem import WordNetLemmatizer
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('popular')

def run() :
    # Load Model
    model_lstm = load_model('best_model')

    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Cyberbullying Tweet Prediction</h1>", unsafe_allow_html=True)

    # Menambahkan Deskripsi Form
    st.write('Page ini berisi model untuk memprediksi jenis Cyberbullying pada tweet')

    with st.form(key= 'form_tweet'):
        st.markdown('### **Tweet**')
        tweet_text = st.text_input('',value= '')
        submitted = st.form_submit_button('Predict')

    # Additional Stopwords
    additional_stopwords = ['rt', 'mkr', 'didn', 'bc', 'n', 'm', 
                    'im', 'll', 'y', 've', 'u', 'ur', 'don', 
                    'p', 't', 's', 'aren', 'kp', 'o', 'kat',
                    'de', 're', 'amp', 'will', 'wa', 'e', 'like', 'andre', 'na', 're', 'lil', 'd', 'na', 'pete', 'annie', 'nikki', 'lmao', 'miley', 'wan', 'gon']

    # Setting stopwords english
    stpwds_eng = list(set(stopwords.words('english')))
    for i in additional_stopwords:
        stpwds_eng.append(i)
    # Membuat Fungsi Pre-Processing Text

    cleaning_pattern = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
    lemmatizer = WordNetLemmatizer()

    def text_proses(teks):

        # Mengubah Teks ke Lowercase
        teks = teks.lower()

        # Menghilangkan Link
        teks = re.sub(cleaning_pattern, ' ', teks)

        # Menghilangkan Mention
        teks = re.sub("@[A-Za-z0-9_]+", " ", teks)
    
        # Menghilangkan Hashtag
        teks = re.sub("#[A-Za-z0-9_]+", " ", teks)

        # Menghilangkan \n
        teks = re.sub(r"\\n", " ",teks)

        # Menghilangkan kata dibawah 3 char
        teks = re.sub(r'\b\w{1,3}\b', " ",teks)
    
        # Menghilangkan Whitespace
        teks = teks.strip()

        # Menghilangkan yang Bukan Huruf seperti Emoji, Gamma dll
        teks = re.sub("[^A-Za-z\s']", " ", teks)

        # Menghilangkan double space
        teks = re.sub("\s\s+" , " ", teks)
            
        # Melakukan Tokenisasi
        tokens = word_tokenize(teks)

        # Menghilangkan Stopwords
        teks = ' '.join([word for word in tokens if word not in stpwds_eng])

        # Melakukan Lemmatizer
        teks = lemmatizer.lemmatize(teks)
    
        return teks

    # Membuat Dataframe
    data_inf = {
    'tweet_text' : tweet_text                               
    }
    data_inf = pd.DataFrame([data_inf])

    if submitted :
        # Preprocessing Data Inference
        data_inf['tweet_processed'] = data_inf['tweet_text'].apply(lambda x: text_proses(x))

        # Prediksi jenis tweet
        y_inf_pred = np.argmax(model_lstm.predict(data_inf['tweet_processed']), axis=-1)

        # Membuat fungsi untuk return result prediksi
        if y_inf_pred[0] == 0:
            result = 'age'
        elif y_inf_pred[0] == 1:
            result = 'ethnicity'
        elif y_inf_pred[0] == 2:
            result = 'gender'
        elif y_inf_pred[0] == 3:
            result = 'not_cyberbullying'
        elif y_inf_pred[0] == 4:
            result = 'other_cyberbullying'
        else:
            result = 'religion'
        st.write('# Cyberbullying Prediction : ', result)
        
if __name__ == '__main__':
    run()