let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

const taskForm = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');
const countDisplay = document.getElementById('count');
const search = document.getElementById('search');

function saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(tasks));
  renderTasks();
}

function renderTasks(filter = '') {
  taskList.innerHTML = '';
  let filteredTasks = tasks.filter(t =>
    t.name.toLowerCase().includes(filter.toLowerCase()) ||
    t.course.toLowerCase().includes(filter.toLowerCase())
  );

  filteredTasks.forEach((task, index) => {
    const li = document.createElement('li');
    li.className = 'task' + (task.done ? ' done' : '');
    li.innerHTML = `
      <div>
        <strong>${task.name}</strong> <br>
        <small>${task.course} | Deadline: ${task.deadline}</small>
      </div>
      <div class="actions">
        <button onclick="toggleDone(${index})">${task.done ? 'Belum' : 'Selesai'}</button>
        <button onclick="editTask(${index})">Edit</button>
        <button onclick="deleteTask(${index})">Hapus</button>
      </div>
    `;
    taskList.appendChild(li);
  });

  countDisplay.textContent = tasks.filter(t => !t.done).length;
}

taskForm.addEventListener('submit', e => {
  e.preventDefault();
  const name = document.getElementById('taskName').value.trim();
  const course = document.getElementById('taskCourse').value.trim();
  const deadline = document.getElementById('taskDeadline').value;

  if (!name || !course || !deadline) {
    alert('Semua field harus diisi!');
    return;
  }

  const today = new Date().toISOString().split('T')[0];
  if (deadline < today) {
    alert('Deadline tidak boleh di masa lalu!');
    return;
  }

  tasks.push({ name, course, deadline, done: false });
  saveTasks();
  taskForm.reset();
});

function toggleDone(index) {
  tasks[index].done = !tasks[index].done;
  saveTasks();
}

function deleteTask(index) {
  if (confirm('Hapus tugas ini?')) {
    tasks.splice(index, 1);
    saveTasks();
  }
}

function editTask(index) {
  const newName = prompt('Edit Nama Tugas:', tasks[index].name);
  const newCourse = prompt('Edit Mata Kuliah:', tasks[index].course);
  const newDeadline = prompt('Edit Deadline (YYYY-MM-DD):', tasks[index].deadline);

  if (newName && newCourse && newDeadline) {
    tasks[index].name = newName.trim();
    tasks[index].course = newCourse.trim();
    tasks[index].deadline = newDeadline;
    saveTasks();
  } else {
    alert('Perubahan dibatalkan atau data tidak valid.');
  }
}

search.addEventListener('input', e => {
  renderTasks(e.target.value);
});

renderTasks();
