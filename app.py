import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Kalkulator Interaktif SPLDV Kelas 10",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Kalkulator Pembelajaran Interaktif SPLDV (Kelas 10 SMA)")
st.markdown("""
Aplikasi ini dirancang untuk membantu kamu memahami materi **Sistem Persamaan Linier Dua Variabel (SPLDV)**, 
khususnya menggunakan **Metode Grafik** dan **Metode Analitik (Eliminasi-Substitusi)** sesuai dengan modul pembelajaranmu!
""")

st.sidebar.header("⚙️ Masukkan Persamaan SPLDV")
st.sidebar.markdown("Bentuk Umum: $ax + by = c$")

st.sidebar.subheader("Persamaan 1")
a1 = st.sidebar.number_input("Koefisien $x$ ($a_1$)", value=2, step=1, format="%d")
b1 = st.sidebar.number_input("Koefisien $y$ ($b_1$)", value=-1, step=1, format="%d")
c1 = st.sidebar.number_input("Konstanta ($c_1$)", value=1, step=1, format="%d")

st.sidebar.subheader("Persamaan 2")
a2 = st.sidebar.number_input("Koefisien $x$ ($a_2$)", value=1, step=1, format="%d")
b2 = st.sidebar.number_input("Koefisien $y$ ($b_2$)", value=1, step=1, format="%d")
c2 = st.sidebar.number_input("Konstanta ($c_2$)", value=5, step=1, format="%d")

st.markdown("---")
col_eq1, col_eq2 = st.columns(2)
with col_eq1:
    st.info(f"**Persamaan 1:** ${int(a1)}x + ({int(b1)})y = {int(c1)}$")
with col_eq2:
    st.info(f"**Persamaan 2:** ${int(a2)}x + ({int(b2)})y = {int(c2)}$")

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

    # Plot Persamaan 1
    if b1 != 0:
        y_vals1 = (c1 - a1 * x_vals) / b1
        ax.plot(x_vals, y_vals1, label=f'{int(a1)}x + {int(b1)}y = {int(c1)}', color='blue', linewidth=2)
    else:
        x_vert1 = c1 / a1
        ax.axvline(x=x_vert1, color='blue', label=f'x = {int(x_vert1)}')

    # Plot Persamaan 2
    if b2 != 0:
        y_vals2 = (c2 - a2 * x_vals) / b2
        ax.plot(x_vals, y_vals2, label=f'{int(a2)}x + {int(b2)}y = {int(c2)}', color='orange', linewidth=2)
    else:
        x_vert2 = c2 / a2
        ax.axvline(x=x_vert2, color='orange', label=f'x = {int(x_vert2)}')

    # Cari solusi titik potong jika ada (det != 0)
    if det != 0:
        x_sol = ((c1 * b2) - (c2 * b1)) / det
        y_sol = ((a1 * c2) - (a2 * c1)) / det

        # Cek apakah nilai bulat untuk ditampilkan rapi
        is_int_sol = (x_sol.is_integer() and y_sol.is_integer())
        lbl_x = int(x_sol) if is_int_sol else round(x_sol, 2)
        lbl_y = int(y_sol) if is_int_sol else round(y_sol, 2)

        ax.scatter([x_sol], [y_sol], color='red', s=100, zorder=5, label=f'Titik Potong ({lbl_x}, {lbl_y})')
        ax.annotate(f'({lbl_x}, {lbl_y})', (x_sol, y_sol), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold', color='red')

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

    st.markdown("---")
    st.subheader("🔍 Panduan Mencari Titik Potong Sumbu (Seperti di Buku)")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(f"**Analisis Persamaan 1:** ${int(a1)}x + {int(b1)}y = {int(c1)}$")
        if a1 != 0:
            tp_x1 = c1 / a1
            disp_x1 = int(tp_x1) if tp_x1.is_integer() else f"{tp_x1:.1f}"
            st.write(f"- Titik potong sumbu $x$ (syarat $y=0$): $x = {int(c1)}/{int(a1)} = {disp_x1}$ $\rightarrow$ Koordinat: $({disp_x1}, 0)$")
        if b1 != 0:
            tp_y1 = c1 / b1
            disp_y1 = int(tp_y1) if tp_y1.is_integer() else f"{tp_y1:.1f}"
            st.write(f"- Titik potong sumbu $y$ (syarat $x=0$): $y = {int(c1)}/{int(b1)} = {disp_y1}$ $\rightarrow$ Koordinat: $(0, {disp_y1})$")

    with col_p2:
        st.markdown(f"**Analisis Persamaan 2:** ${int(a2)}x + {int(b2)}y = {int(c2)}$")
        if a2 != 0:
            tp_x2 = c2 / a2
            disp_x2 = int(tp_x2) if tp_x2.is_integer() else f"{tp_x2:.1f}"
            st.write(f"- Titik potong sumbu $x$ (syarat $y=0$): $x = {int(c2)}/{int(a2)} = {disp_x2}$ $\rightarrow$ Koordinat: $({disp_x2}, 0)$")
        if b2 != 0:
            tp_y2 = c2 / b2
            disp_y2 = int(tp_y2) if tp_y2.is_integer() else f"{tp_y2:.1f}"
            st.write(f"- Titik potong sumbu $y$ (syarat $x=0$): $y = {int(c2)}/{int(b2)} = {disp_y2}$ $\rightarrow$ Koordinat: $(0, {disp_y2})$")

with tab2:
    st.subheader("📝 Langkah Penyelesaian Analitis (Eliminasi & Substitusi)")
    
    if det != 0:
        x_sol = ((c1 * b2) - (c2 * b1)) / det
        y_sol = ((a1 * c2) - (a2 * c1)) / det
        
        # Format angka bulat jika memungkinkan agar bersih
        x_display = int(x_sol) if x_sol.is_integer() else f"{x_sol:.2f}"
        y_display = int(y_sol) if y_sol.is_integer() else f"{y_sol:.2f}"
        
        st.success(f"**Himpunan Penyelesaian ditemukan!** Nilai $x = {x_display}$ dan $y = {y_display}$")
        
        st.markdown("#### **Langkah 1: Metode Eliminasi**")
        st.write("Kita eliminasi salah satu variabel (misalnya $y$) terlebih dahulu dengan menyamakan koefisiennya.")
        st.markdown(f"- Persamaan 1 dikalikan dengan koefisien $y$ persamaan 2 ($|{int(b2)}|$) $\\rightarrow$ Menghasilkan persamaan baru.")
        st.markdown(f"- Persamaan 2 dikalikan dengan koefisien $y$ persamaan 1 ($|{int(b1)}|$) $\\rightarrow$ Menghasilkan persamaan baru.")
        
        st.markdown("#### **Langkah 2: Metode Substitusi**")
        st.markdown(f"Masukkan nilai $x = {x_display}$ ke salah satu persamaan awal untuk mendapatkan nilai $y$.")
        st.markdown("Hasil akhir perhitungan menunjukkan titik potong kedua garis berada pada koordinat:")
        
        # Penulisan LaTeX yang bersih tanpa error / escape syntax yang rusak
        st.markdown(f"### $\\text{{HP}} = \\{{({x_display}, {y_display})\\}}$")
    else:
        st.warning("Determinannya bernilai 0. Artinya garis-garis tersebut bisa sejajar atau berhimpit (tidak memiliki solusi unik atau memiliki solusi tak hingga).")

with tab3:
    st.subheader("💡 Konsep Penting Berdasarkan Modul Pembelajaran")
    st.markdown("""
    Perhatikan kedudukan dua garis pada bidang Kartesius:
    1. **Tepat Satu Penyelesaian:** Kedua garis berpotongan di satu titik (seperti contoh di atas).
    2. **Himpunan Penyelesaian Kosong ($\\varnothing$):** 
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
            st.error("⚠️ **Kedua garis sejajar!** Himpunan penyelesaian adalah **himpunan kosong ($\\varnothing$)**.")
        elif r_a == r_b and r_b == r_c:
            st.warning("⚠️ **Kedua garis berhimpit!** Himpunan penyelesaian **tak hingga banyaknya**.")
        else:
            st.success("✅ **Kedua garis berpotongan di satu titik!** Memiliki tepat satu penyelesaian.")
