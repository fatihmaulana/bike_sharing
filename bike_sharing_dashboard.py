import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'bike_sharing_data/day.csv'
df = pd.read_csv(file_path)

st.title("Dashboard Analisis Bike Sharing")


st.subheader("Rata-rata Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")
df['dteday'] = pd.to_datetime(df['dteday'])
df['weekday'] = df['dteday'].dt.day_name()
weekday_usage = df.groupby('weekday')['cnt'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

fig, ax = plt.subplots()
sns.barplot(x=weekday_usage.index, y=weekday_usage.values, ax=ax)
ax.set_title('Rata-rata Penggunaan Sepeda Berdasarkan Hari dalam Seminggu')
ax.set_xlabel('Hari dalam Seminggu')
ax.set_ylabel('Rata-rata Jumlah Sepeda yang Disewa')
st.pyplot(fig)


st.subheader("Korelasi Faktor Cuaca dengan Penyewaan Sepeda")
weather_factors = ['temp', 'atemp', 'hum', 'windspeed']
correlations = df[weather_factors + ['cnt']].corr()

fig, ax = plt.subplots()
sns.heatmap(correlations, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
ax.set_title('Korelasi Faktor Cuaca dengan Penyewaan Sepeda')
st.pyplot(fig)


st.subheader("RFM Analysis untuk Penggunaan Sepeda")


df['Recency'] = (df['dteday'].max() - df['dteday']).dt.days

df['Frequency'] = df.groupby('weekday')['cnt'].transform('count')


df['Monetary'] = df.groupby('weekday')['cnt'].transform('sum')


st.write("Rata-rata Recency per Hari:")
st.bar_chart(df.groupby('weekday')['Recency'].mean())

st.write("Rata-rata Frequency per Hari:")
st.bar_chart(df.groupby('weekday')['Frequency'].mean())

st.write("Rata-rata Monetary per Hari:")
st.bar_chart(df.groupby('weekday')['Monetary'].mean())
