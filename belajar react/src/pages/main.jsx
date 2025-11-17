import React from "react";

const HomePage = () => {
    return (
        <div>
            <header>
                <h1>Aplikasi Manajemen Buku Pribadi</h1>
                <p>Selamat datang di aplikasi manajemen buku pribadi !</p>
            </header>
        
            <main>
                <section>
                    <h2>Tambahkan Buku Anda</h2>
                    <input type="text" placeholder="Judul Buku" />
                    <input type="text" placeholder="Pengarang" />
                    <input type="text" placeholder="Tahun Terbit" /> 
                    <br />
                    <button>Tambah Buku</button>
                </section>
                <section>
                    <h2>Daftar List Buku</h2>
                </section>
            </main>
        </div>
    );
}
export default HomePage;