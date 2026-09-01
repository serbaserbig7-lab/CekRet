import streamlit as st
import streamlit.components.v1 as components

# Konfigurasi Halaman
st.set_page_config(page_title="Cek Retribusi", page_icon="🧾", layout="centered")

st.title("🧾 Cek Retribusi Bank Nagari")
st.write("Masukkan kode ID untuk pengecekan retribusi.")

# Menggunakan form agar rapi
with st.form("form_cek"):
    id_retribusi = st.text_input("Kode ID (contoh: 0001)")
    submit = st.form_submit_button("Cek Sekarang")

if submit:
    if not id_retribusi.strip():
        st.warning("Silakan masukkan kode ID terlebih dahulu!")
    else:
        # Membuat link sesuai format
        url = f"https://retribusi.banknagari.co.id/RetribusiPadang/nav2?m=cT&i={id_retribusi.strip()}"
        
        st.success("Tautan berhasil dibuat!")
        
        # Tombol untuk buka di tab baru (solusi jika bank memblokir iframe)
        st.link_button("Buka Hasil di Tab Baru", url, type="primary")
        
        st.divider()
        
        # Menampilkan website langsung di dalam aplikasi (iFrame)
        st.write("### Pratinjau Halaman Bank Nagari:")
        components.iframe(url, height=600, scrolling=True)
