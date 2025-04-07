

const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slider__section');
const btnLeft = document.getElementById('btn-left');
const btnRight = document.getElementById('btn-right');

let index = 1;
let width = slides[0].clientWidth;

// Clonar slides para efecto infinito
const firstClone = slides[0].cloneNode(true);
const lastClone = slides[slides.length - 1].cloneNode(true);
slider.appendChild(firstClone);
slider.insertBefore(lastClone, slides[0]);

const allSlides = document.querySelectorAll('.slider__section');
slider.style.transform = `translateX(-${width * index}px)`;

function moveToSlide(i) {
  index = i;
  slider.style.transition = 'transform 0.5s ease-in-out';
  slider.style.transform = `translateX(-${width * index}px)`;
}

btnRight.addEventListener('click', () => {
  if (index >= allSlides.length - 1) return;
  moveToSlide(index + 1);
});

btnLeft.addEventListener('click', () => {
  if (index <= 0) return;
  moveToSlide(index - 1);
});

slider.addEventListener('transitionend', () => {
  if (allSlides[index].isEqualNode(firstClone)) {
    slider.style.transition = 'none';
    index = 1;
    slider.style.transform = `translateX(-${width * index}px)`;
  }
  if (allSlides[index].isEqualNode(lastClone)) {
    slider.style.transition = 'none';
    index = allSlides.length - 2;
    slider.style.transform = `translateX(-${width * index}px)`;
  }
});

setInterval(() => {
  moveToSlide(index + 1);
}, 7000);

// Para que funcione bien en cambios de tamaño de pantalla
window.addEventListener('resize', () => {
  width = slides[0].clientWidth;
  slider.style.transform = `translateX(-${width * index}px)`;
});