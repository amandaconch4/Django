

let currentIndex = 0;
const slides = document.querySelectorAll('.slider__section'); // Seleccionamos todas las imágenes del slider
const totalSlides = slides.length;
const btnLeft = document.getElementById('btn-left');
const btnRight = document.getElementById('btn-right');

function moveToSlide(index) {
  // Evitar que el índice esté fuera del rango
  if (index < 0) {
    currentIndex = totalSlides - 1;
  } else if (index >= totalSlides) {
    currentIndex = 0;
  } else {
    currentIndex = index;
  }

  // Cambiar la posición del slider
  slider.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Detectamos cuando se ha completado la transición
slider.addEventListener('transitionend', () => {
  // Reiniciar el índice si llegamos al último slide
  if (currentIndex === totalSlides) {
    currentIndex = 0;
    slider.style.transition = 'none'; // Evita transición al reiniciar
    slider.style.transform = `translateX(-${currentIndex * 100}%)`;
    setTimeout(() => {
      slider.style.transition = 'transform 3s ease-in-out'; // Restaura la transición después de reiniciar
    }, 20);
  }
});

// Botones de navegación
btnLeft.addEventListener('click', () => moveToSlide(currentIndex - 1));
btnRight.addEventListener('click', () => moveToSlide(currentIndex + 1));

// Movimiento automático cada 7 segundos
setInterval(() => {
  moveToSlide(currentIndex + 1);
}, 7000);