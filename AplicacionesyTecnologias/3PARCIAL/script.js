// Agregar animaciones al hacer clic en los elementos de la lista
document.querySelectorAll('.list-group-item').forEach(item => {
    item.addEventListener('click', function() {
      this.classList.toggle('active');
    });
  });
  