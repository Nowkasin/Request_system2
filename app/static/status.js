export function saveRow(taskCode) {
  const inputs = document.querySelectorAll(`[data-task="${taskCode}"]`);
  const updatedData = {};
  inputs.forEach(input => {
    updatedData[input.dataset.field] = input.value;
  });

  fetch(`/update/${taskCode}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(updatedData)
  })
  .then(res => res.json())
  .then(data => {
    alert(data.message || '✅ บันทึกสำเร็จ');
  })
  .catch(err => {
    alert('❌ เกิดข้อผิดพลาด');
    console.error(err);
  });
}
