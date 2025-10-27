/* app.js - Dasbor Pribadi (Bahasa Indonesia)
   ✅ ES6+: let/const, arrow function ≥3, template literals, async/await, class
   ✅ Fitur: tambah/edit/hapus Tugas & Catatan
   ✅ Penyimpanan lokal: localStorage
*/

class Penyimpanan {
  constructor(kunci = 'dasbor_pribadi_v1') {
    this.kunci = kunci;
  }

  async simpan(data) {
    return new Promise((resolve) => {
      localStorage.setItem(this.kunci, JSON.stringify(data));
      resolve(true);
    });
  }

  async muat() {
    return new Promise((resolve) => {
      const data = localStorage.getItem(this.kunci);
      if (!data) return resolve({ tugas: [], catatan: [] });
      try {
        resolve(JSON.parse(data));
      } catch {
        resolve({ tugas: [], catatan: [] });
      }
    });
  }
}

// helper arrow functions
const buatID = () => Date.now().toString(36) + Math.random().toString(36).slice(2, 7);
const formatTanggal = (ts) => new Date(ts).toLocaleString('id-ID');

// elemen
const elTugas = document.getElementById('tasksList');
const elCatatan = document.getElementById('notesList');
const formTugas = document.getElementById('taskForm');
const formCatatan = document.getElementById('noteForm');
const jamEl = document.getElementById('clock');

let data = { tugas: [], catatan: [] };
const simpanan = new Penyimpanan();

// render fungsi
const tampilkanTugas = () => {
  elTugas.innerHTML = '';
  if (data.tugas.length === 0) return elTugas.innerHTML = `<p class="small">Belum ada tugas.</p>`;
  
  data.tugas.forEach(t => {
    const div = document.createElement('div');
    div.className = 'item';
    div.dataset.id = t.id;
    div.innerHTML = `
      <div class="left">
        <div class="title" style="text-decoration:${t.selesai ? 'line-through' : 'none'}">${t.judul}</div>
        <div class="meta">${t.deskripsi || ''} · ${formatTanggal(t.dibuat)}</div>
      </div>
      <div class="actions">
        <button data-action="toggle">${t.selesai ? 'Batal' : 'Selesai'}</button>
        <button data-action="edit">Edit</button>
        <button data-action="hapus">Hapus</button>
      </div>
    `;
    elTugas.appendChild(div);
  });
};

const tampilkanCatatan = () => {
  elCatatan.innerHTML = '';
  if (data.catatan.length === 0) return elCatatan.innerHTML = `<p class="small">Belum ada catatan.</p>`;

  data.catatan.forEach(c => {
    const div = document.createElement('div');
    div.className = 'item';
    div.dataset.id = c.id;
    div.innerHTML = `
      <div class="left">
        <div class="title">${c.judul}</div>
        <div class="meta">${c.isi || ''} · ${formatTanggal(c.dibuat)}</div>
      </div>
      <div class="actions">
        <button data-action="edit">Edit</button>
        <button data-action="hapus">Hapus</button>
      </div>
    `;
    elCatatan.appendChild(div);
  });
};

const renderSemua = () => {
  tampilkanTugas();
  tampilkanCatatan();
};

// operasi data
const simpan = async () => await simpanan.simpan(data);

const muat = async () => {
  data = await simpanan.muat();
  renderSemua();
};

// event form
formTugas.addEventListener('submit', async (e) => {
  e.preventDefault();
  const judul = document.getElementById('taskTitle').value.trim();
  const deskripsi = document.getElementById('taskDesc').value.trim();
  if (!judul) return alert('Judul tugas wajib diisi.');

  const baru = { id: buatID(), judul, deskripsi, selesai: false, dibuat: Date.now() };
  data.tugas.unshift(baru);
  await simpan();
  renderSemua();
  formTugas.reset();
});

formCatatan.addEventListener('submit', async (e) => {
  e.preventDefault();
  const judul = document.getElementById('noteTitle').value.trim();
  const isi = document.getElementById('noteBody').value.trim();
  if (!judul) return alert('Judul catatan wajib diisi.');

  const baru = { id: buatID(), judul, isi, dibuat: Date.now() };
  data.catatan.unshift(baru);
  await simpan();
  renderSemua();
  formCatatan.reset();
});

// aksi tugas
elTugas.addEventListener('click', async (e) => {
  const btn = e.target.closest('button');
  if (!btn) return;
  const id = e.target.closest('.item').dataset.id;
  const tugas = data.tugas.find(t => t.id === id);
  if (!tugas) return;

  const aksi = btn.dataset.action;
  if (aksi === 'toggle') {
    tugas.selesai = !tugas.selesai;
  } else if (aksi === 'edit') {
    const j = prompt('Ubah judul tugas:', tugas.judul);
    if (j === null) return;
    const d = prompt('Ubah deskripsi:', tugas.deskripsi);
    if (d === null) return;
    tugas.judul = j.trim(); tugas.deskripsi = d.trim();
  } else if (aksi === 'hapus') {
    if (confirm('Hapus tugas ini?')) {
      data.tugas = data.tugas.filter(t => t.id !== id);
    }
  }
  await simpan();
  renderSemua();
});

// aksi catatan
elCatatan.addEventListener('click', async (e) => {
  const btn = e.target.closest('button');
  if (!btn) return;
  const id = e.target.closest('.item').dataset.id;
  const catatan = data.catatan.find(c => c.id === id);
  if (!catatan) return;

  const aksi = btn.dataset.action;
  if (aksi === 'edit') {
    const j = prompt('Ubah judul catatan:', catatan.judul);
    if (j === null) return;
    const i = prompt('Ubah isi catatan:', catatan.isi);
    if (i === null) return;
    catatan.judul = j.trim(); catatan.isi = i.trim();
  } else if (aksi === 'hapus') {
    if (confirm('Hapus catatan ini?')) {
      data.catatan = data.catatan.filter(c => c.id !== id);
    }
  }
  await simpan();
  renderSemua();
});

// jam real-time
setInterval(() => jamEl.textContent = new Date().toLocaleString('id-ID'), 1000);

// muat pertama kali
muat();
