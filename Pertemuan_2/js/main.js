// main.js
import StorageManager from './app.js';

const storage = new StorageManager('dashboard_pribadi');
let data = { tugas: [], catatan: [] };

// Fungsi async untuk memuat data awal
const muatData = async () => {
  data = await storage.load();
  renderTugas();
  renderCatatan();
};

// Arrow function untuk memperbarui waktu setiap detik
const updateWaktu = () => {
  const waktuEl = document.getElementById('waktu');
  waktuEl.textContent = new Date().toLocaleString('id-ID');
};
setInterval(updateWaktu, 1000);

// Render daftar tugas menggunakan template literals
const renderTugas = () => {
  const list = document.getElementById('daftarTugas');
  list.innerHTML = data.tugas.map((t, i) => `
    <li>
      <span>${t}</span>
      <div>
        <button onclick="editTugas(${i})">Edit</button>
        <button onclick="hapusTugas(${i})">Hapus</button>
      </div>
    </li>
  `).join('');
};

// Render daftar catatan menggunakan template literals
const renderCatatan = () => {
  const list = document.getElementById('daftarCatatan');
  list.innerHTML = data.catatan.map((c, i) => `
    <li>
      <span>${c}</span>
      <div>
        <button onclick="editCatatan(${i})">Edit</button>
        <button onclick="hapusCatatan(${i})">Hapus</button>
      </div>
    </li>
  `).join('');
};

// Tambah tugas
document.getElementById('tambahTugas').addEventListener('click', async () => {
  const input = document.getElementById('judulTugas');
  if (!input.value.trim()) return alert('Masukkan nama tugas!');
  data.tugas.push(input.value.trim());
  input.value = '';
  await storage.save(data);
  renderTugas();
});

// Tambah catatan
document.getElementById('tambahCatatan').addEventListener('click', async () => {
  const input = document.getElementById('isiCatatan');
  if (!input.value.trim()) return alert('Tulis catatan!');
  data.catatan.push(input.value.trim());
  input.value = '';
  await storage.save(data);
  renderCatatan();
});

// Fungsi global agar bisa dipanggil di onclick HTML
window.hapusTugas = async (index) => {
  data.tugas.splice(index, 1);
  await storage.save(data);
  renderTugas();
};

window.hapusCatatan = async (index) => {
  data.catatan.splice(index, 1);
  await storage.save(data);
  renderCatatan();
};

window.editTugas = async (index) => {
  const baru = prompt('Edit nama tugas:', data.tugas[index]);
  if (baru !== null && baru.trim()) {
    data.tugas[index] = baru.trim();
    await storage.save(data);
    renderTugas();
  }
};

window.editCatatan = async (index) => {
  const baru = prompt('Edit catatan:', data.catatan[index]);
  if (baru !== null && baru.trim()) {
    data.catatan[index] = baru.trim();
    await storage.save(data);
    renderCatatan();
  }
};

// Jalankan
muatData();
updateWaktu();
