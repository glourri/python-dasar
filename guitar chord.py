#mengimport streamlit as st dan modul os untuk beirnteraksi dengan sistem file
import streamlit as st
import os


#mendefinisikan sebagai tempat menyimpan gambar kunci gitar
PENYIMPANAN_CHORD = "gambar_kunci"

def nama_kunci_gitar(kunci_gitar):
  
    # Konversi nama chord menjadi format file (misal G -> G.jpg)
    ekstensi = ['.jpg', '.jpeg', '.png', '.gif']
    
    for ext in ekstensi:
        kunci_path = os.path.join(PENYIMPANAN_CHORD, kunci_gitar.upper() + ext)
        if os.path.exists(kunci_path):
            return kunci_path
    #os.path join menggabungkan direktori dan nama file
    #kunci gitat upper untuk mengubah nama kunci menjadi huruf kapital
    #os.path.exist memeriksa apakah file tersebut tersedia dan jika ditemukan akan kembali ke path file tersebut
    return None

def main():
    st.title("Hello there!")
    st.write("Temukan gambar chord gitar dengan mudah!")
    
    # Input chord dari user
    chord_input = st.text_input("Masukkan Nama Chord (contoh: G, C, Am)", placeholder="Ketik chord di sini")
    
    if chord_input:
        # Cari gambar kunci
        gambar_kunci = nama_kunci_gitar(chord_input)
        
        
        if gambar_kunci:
            st.image(gambar_kunci, caption=f"Chord {chord_input.upper()}", use_column_width=True)
            #jika kunci ditemukan tampilkan dengan st.iamage
            #berikan caption nama kunci
            #use_column_width=true untuk menyesuaikan lebar
        else:
            #tampilkan pesan peringatan menggunakan st.warning
            st.warning(f"Maaf, chord {chord_input.upper()} tidak ditemukan. Cek kembali nama chord.")
    
    # Tambahkan informasi tambahan
    st.sidebar.header("Petunjuk")
    st.sidebar.info(
    #menambahkan sidebar dengan petunjuk penggunaan
    #st.sidebar.header membuat header di sidebar
    #st.sidebar.info menamplikan infrmasi petunjuk dengan format mulitline
    """
    Cara Penggunaan:
    1. Ketik nama chord (huruf besar/kecil)
    2. Tekan Enter
    3. Gambar chord akan ditampilkan
    
    Contoh: G, C, Am, Dm
    """)

if __name__ == "__main__":
    main()
