import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run() :
    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    st.write('Berikut adalah EDA dan Workcloud dari Setiap Kategori Tweet')

    # Import DF
    df_eda = pd.read_csv('eda_preprocessing.csv')


    # Membuat Sub Header
    st.subheader('**Persebaran Kategori Tweet**')

    # Membuat visualisasi Distribusi Tweet
    fig, ax =plt.subplots(1,2,figsize=(15,6))

    sns.countplot(x='cyberbullying_type', data=df_eda, palette="winter", ax=ax[0])
    ax[0].set_xlabel("cyberbullying_type", fontsize= 12)
    ax[0].set_ylabel("# of Tweet", fontsize= 12)
    fig.suptitle('Tweet Type Distribution', fontsize=18, fontweight='bold')
    ax[0].set_ylim(0,10000)
    ax[0].tick_params(axis='x', rotation=90)
    plt.xlabel("cyberbullying_type", fontsize= 12)
    plt.ylabel("# of Tweet", fontsize= 12)

    for p in ax[0].patches:
        ax[0].annotate("%.0f"%(p.get_height()), (p.get_x() + p.get_width() / 2,
                        p.get_height()+205), ha='center', va='center',fontsize = 11) 

    df_eda['cyberbullying_type'].value_counts().plot(kind='pie',autopct='%1.1f%%', textprops = {"fontsize":12})
    ax[1].set_ylabel("% of Tweet", fontsize= 12)
    st.pyplot(fig)


    # Membuat Sub Header
    st.subheader('**All Tweet**')

    # Membuat Sub Header
    st.subheader('**Age Tweet**')

    # Membuat Sub Header
    st.subheader('**Gender Tweet**')

    # Membuat Sub Header
    st.subheader('**Religion Tweet**')

    # Membuat Sub Header
    st.subheader('**Other Cyberbullying Tweet**')

    # Membuat Sub Header
    st.subheader('**Not Cyberbullying Tweet**')
    
    
if __name__ == '__main__':
    run()