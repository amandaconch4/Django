

const slider = document.querySelector('.slider');
const slides = document.querySelectorAll('.slider__section');
const btnLeft = document.getElementById('btn-left');
const btnRight = document.getElementById('btn-right');

let index = 1;
let width = slides[0].clientWidth;

// Clonamos primero y último
const firstClone = slides[0].cloneNode(true);
const lastClone = slides[slides.length - 1].cloneNode(true);
firstClone.classList.add('clone');
lastClone.classList.add('clone');

slider.appendChild(firstClone);
slider.insertBefore(lastClone, slides[0]);

let allSlides = document.querySelectorAll('.slider__section');

// Posición inicial
slider.style.transform = `translateX(-${width * index}px)`;

// Función para mover
function moveToSlide(i) {
  index = i;
  slider.style.transition = 'transform 0.5s ease-in-out';
  slider.style.transform = `translateX(-${width * index}px)`;
}

// Eventos botones
btnRight.addEventListener('click', () => moveToSlide(index + 1));
btnLeft.addEventListener('click', () => moveToSlide(index - 1));

// Evento al terminar transición
slider.addEventListener('transitionend', () => {
  if (allSlides[index].classList.contains('clone')) {
    slider.style.transition = 'none';
    if (index === allSlides.length - 1) {
      index = 1;
    } else if (index === 0) {
      index = allSlides.length - 2;
    }
    slider.style.transform = `translateX(-${width * index}px)`;
  }
});

// Auto-slide
let interval = setInterval(() => moveToSlide(index + 1), 7000);

// Ajuste en resize
window.addEventListener('resize', () => {
  width = document.querySelector('.slider__section').clientWidth;
  slider.style.transform = `translateX(-${width * index}px)`;
});
