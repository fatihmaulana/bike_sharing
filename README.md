# Bike Sharing Analysis and Dashboard

Proyek ini menganalisis data penyewaan sepeda dan menyediakan dashboard interaktif menggunakan Streamlit.

## Struktur Proyek

- `Proyek_Analisis_Data.ipynb`: Notebook Jupyter untuk analisis data.
- `bike_sharing_dashboard.py`: Script Streamlit untuk dashboard interaktif.
- `bike_sharing_data/`: Direktori yang berisi file data (`day.csv` dan `hour.csv`).
- `requirements.txt`: Daftar pustaka Python yang diperlukan.

## Cara Menjalankan Dashboard

1. **Clone atau download** repositori ini ke komputer Anda.

2. **Instal pustaka yang diperlukan**:

   pip install -r requirements.txt

3. **Jalankan dashboard Streamlit**:

   streamlit run bike_sharing_dashboard.py

4. **Buka browser** dan akses `http://localhost:8501/` untuk melihat dashboard.

## Data

Data yang digunakan dalam proyek ini berasal dari direktori `bike_sharing_data`, yang berisi:

- `day.csv`: Data penyewaan sepeda harian.
- `hour.csv`: Data penyewaan sepeda per jam.
