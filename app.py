import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Pengaturan Halaman Streamlit
st.set_page_config(
    page_title="Kalkulator Interaktif SPLDV Kelas 10",
    page_icon="📊",
    layout="wide"
)

# Judul dan Pengantar
st.title("📊 Kalkulator Pembelajaran Interaktif SPLDV (Kelas 10 SMA)")
st.markdown("""
Aplikasi ini dirancang untuk membantu kamu memahami materi **Sistem Persamaan Linier Dua Variabel (SPLDV)**, 
khususnya menggunakan **Metode Grafik** dan **Metode Analitik (Eliminasi-Substitusi)** sesuai dengan modul pembelajaranmu!
""")

st.sidebar.header("⚙️ Masukkan Persamaan SPLDV")
st.sidebar.markdown("Bentuk Umum: $ax + by = c$")

st.sidebar.subheader("Persamaan 1")
a1 = st.sidebar.number_input("Koefisien $x$ ($a_1$)", value=2.0, step=1.0)
b1 = st.sidebar.number_input("Koefisien $y$ ($b_1$)", value=-1.0, step=1.0)
c1 = st.sidebar.number_input("Konstanta ($c_1$)", value=1.0, step=1.0)

st.sidebar.subheader("Persamaan 2")
a2 = st.sidebar.number_input("Koefisien $x$ ($a_2$)", value=1.0, step=1.0)
b2 = st.sidebar.number_input("Koefisien $y$ ($b_2$)", value=1.0, step=1.0)
c2 = st.sidebar.number_input("Konstanta ($c_2$)", value=5.0, step=1.0)

# Menampilkan Persamaan Saat Ini
st.markdown("---")
col_eq1, col_eq2 = st.columns(2)
with col_eq1:
    st.info(f"**Persamaan 1:** ${int(a1) if a1.is_integer() else a1}x + ({int(b1) if b1.is_integer() else b1})y = {int(c1) if c1.is_integer() else c1}$")
with col_eq2:
    st.info(f"**Persamaan 2:** ${int(a2) if a2.is_integer() else a2}x + ({int(b2) if b2.is_integer() else b2})y = {int(c2) if c2.is_integer() else c2}$")

# Hitung Determinan Matriks / Kondisi Garis
det = (a1 * b2) - (a2 * b1)

# Tab Menu Pembelajaran
tab1, tab2, tab3 = st.tabs(["📈 Visualisasi & Metode Grafik", "📝 Langkah Analitis (Langkah-demi-Langkah)", "💡 Analisis Khusus & Konsep Penting"])

with tab1:
    st.subheader("Visualisasi Grafik Perpotongan Dua Garis")
    st.markdown("Metode grafik dilakukan dengan mencari titik potong sumbu $x$ ($y=0$) dan sumbu $y$ ($x=0$) dari masing-masing persamaan.")

    # Membuat plot matplotlib
    fig, ax = plt.subplots(figsize=(8, 6))

    # Range sumbu x
    x_vals = np.linspace(-10, 10, 400)

    # Plot Persamaan 1: b1*y = c1 - a1*x => y = (c1 - a1*x)/b1
    if b1 != 0:
        y_vals1 = (c1 - a1 * x_vals) / b1
        ax.plot(x_vals, y_vals1, label=f'{a1}x + {b1}y = {c1}', color='blue', linewidth=2)
    else:
        # Garis vertikal x = c1/a1
        x_vert1 = c1 / a1
        ax.axvline(x=x_vert1, color='blue', label=f'x = {x_vert1}')

    # Plot Persamaan 2: b2*y = c2 - a2*x => y = (c2 - a2*x)/b2
    if b2 != 0:
        y_vals2 = (c2 - a2 * x_vals) / b2
        ax.plot(x_vals, y_vals2, label=f'{a2}x + {b2}y = {c2}', color='orange', linewidth=2)
    else:
        x_vert2 = c2 / a2
        ax.axvline(x=x_vert2, color='orange', label=f'x = {x_vert2}')

    # Cari solusi titik potong jika ada (det != 0)
    if det != 0:
        # Aturan Cramer
        x_sol = ((c1 * b2) - (c2 * b1)) / det
        y_sol = ((a1 * c2) - (a2 * c1)) / det

        # Tandai titik potong
        ax.scatter([x_sol], [y_sol], color='red', s=100, zorder=5, label=f'Titik Potong ({x_sol:.2f}, {y_sol:.2f})')
        ax.annotate(f'({x_sol:.1f}, {y_sol:.1f})', (x_sol, y_sol), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold', color='red')

    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.legend(loc='best')
    ax.set_title("Grafik SPLDV")

    st.pyplot(fig)

    # Menampilkan Analisis Titik Potong Sumbu seperti di Modul
    st.markdown("---")
    st.subheader("🔍 Panduan Mencari Titik Potong Sumbu (Seperti di Buku)")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(f"**Analisis Persamaan 1:** ${a1}x + {b1}y = {c1}$")
        # Titik potong sumbu x (y=0)
        if a1 != 0:
            tp_x1 = c1 / a1
            st.write(f"- Titik potong sumbu $x$ (syarat $y=0$): $x = {c1}/{a1} = {tp_x1}$ $\rightarrow$ Koordinat: $({tp_x1}, 0)$")
        # Titik potong sumbu y (x=0)
        if b1 != 0:
            tp_y1 = c1 / b1
            st.write(f"- Titik potong sumbu $y$ (syarat $x=0$): $y = {c1}/{b1} = {tp_y1}$ $\rightarrow$ Koordinat: $(0, {tp_y1})$")

    with col_p2:
        st.markdown(f"**Analisis Persamaan 2:** ${a2}x + {b2}y = {c2}$")
        if a2 != 0:
            tp_x2 = c2 / a2
            st.write(f"- Titik potong sumbu $x$ (syarat $y=0$): $x = {c2}/{a2} = {tp_x2}$ $\rightarrow$ Koordinat: $({tp_x2}, 0)$")
        if b2 != 0:
            tp_y2 = c2 / b2
            st.write(f"- Titik potong sumbu $y$ (syarat $x=0$): $y = {c2}/{b2} = {tp_y2}$ $\rightarrow$ Koordinat: $(0, {tp_y2})$")

with tab2:
    st.subheader("📝 Langkah Penyelesaian Analitis (Eliminasi & Substitusi)")
    
    if det != 0:
        x_sol = ((c1 * b2) - (c2 * b1)) / det
        y_sol = ((a1 * c2) - (a2 * c1)) / det
        
        st.success(f"**Himpunan Penyelesaian ditemukan!** Nilai $x = {x_sol:.2f}$ dan $y = {y_sol:.2f}$")
        
        st.markdown("#### **Langkah 1: Metode Eliminasi**")
        st.write(f"Kita eliminasi variabel $y$ terlebih dahulu dengan menyamakan koefisiennya.")
        st.write(f"- Persamaan 1 dikali dengan koefisien $y$ persamaan 2 ($|{b2}|$) $\rightarrow$ Menghasilkan persamaan baru.")
        st.write(f"- Persamaan 2 dikali dengan koefisien $y$ persamaan 1 ($|{b1}|$) $\rightarrow$ Menghasilkan persamaan baru.")
        
        st.markdown("#### **Langkah 2: Metode Substitusi**")
        st.write(f"Masukkan nilai $x = {x_sol:.2f}$ ke salah satu persamaan awal untuk mendapatkan nilai $y$.")
        st.write(f"Hasil akhir perhitungan menunjukkan titik potong keduaya berada pada koordinat:")
        st.markdown(f"### HP = $\\left\\{{({x_sol:.2f}, {y_sol:.2f})\\}}\\right$")
    else:
        st.warning("Determinannya bernilai 0. Artinya garis-garis tersebut bisa sejajar atau berhimpit (tidak memiliki solusi unik atau memiliki solusi tak hingga).")

with tab3:
    st.subheader("💡 Konsep Penting Berdasarkan Modul Pembelajaran")
    st.markdown("""
    Perhatikan kedudukan dua garis pada bidang cartesius:
    1. **Tepat Satu Penyelesaian:** Kedua garis berpotongan di satu titik (seperti contoh di atas).
    2. **Himpunan Penyelesaian Kosong ($\varnothing$):** 
       Kedua garis **sejajar** (tidak pernah berpotongan). 
       $$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} \\neq \\frac{c_1}{c_2}$$
    3. **Himpunan Penyelesaian Tak Hingga Banyaknya:** 
       Kedua garis **berhimpit** (menjadi garis yang sama persis).
       $$\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2}$$
    """)
    
    # Cek kondisi rasio untuk siswa
    if a2 != 0 and b2 != 0:
        r_a = a1 / a2
        r_b = b1 / b2
        r_c = c1 / c2
        
        st.markdown("#### **Status Sistem Persamaan Saat Ini:**")
        if r_a == r_b and r_b != r_c:
            st.error("⚠️ **Kedua garis sejajar!** Himpunan penyelesaian adalah **himpunan kosong ($\varnothing$)**.")
        elif r_a == r_b and r_b == r_c:
            st.warning("⚠️ **Kedua garis berhimpit!** Himpunan penyelesaian **tak hingga banyaknya**.")
        else:
            st.success("✅ **Kedua garis berpotongan di satu titik!** Memiliki tepat satu penyelesaian.")
