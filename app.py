import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Titanic Data Exploration')

@st.cache_data
def load_data():
    url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
    data = pd.read_csv(url)
    return data

data = load_data()

st.sidebar.title("Einstellungen")
view = st.sidebar.radio("Wähle die Ansicht", ('Tabelle', 'Grafik'))

if view == 'Tabelle':
    st.write("Daten als Tabelle")
    num_rows = st.sidebar.slider("Anzahl der Zeilen", min_value=1, max_value=len(data), value=10)
    st.dataframe(data.head(num_rows))
elif view == 'Grafik':
    st.write("Daten als Grafik")
    chart_type = st.sidebar.selectbox("Wähle den Grafiktyp", ["Histogramm", "Korrelation", "Überlebende nach Klasse"])

    if chart_type == "Histogramm":
        st.write("Histogramm der Altersverteilung")
        fig, ax = plt.subplots()
        sns.histplot(data['Age'].dropna(), kde=True, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Korrelation":
        st.write("Korrelationsmatrix")
        numeric_data = data.select_dtypes(include=['float64', 'int64'])
        fig, ax = plt.subplots()
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Überlebende nach Klasse":
        st.write("Überlebende nach Klasse")
        fig, ax = plt.subplots()
        sns.countplot(x='Pclass', hue='Survived', data=data, ax=ax)
        st.pyplot(fig)
