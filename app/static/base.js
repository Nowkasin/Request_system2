export function openModal() {
  document.getElementById('profileModal')?.classList.remove('hidden');
}

export function closeModal() {
  document.getElementById('profileModal')?.classList.add('hidden');
}
