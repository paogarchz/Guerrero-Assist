// script.js
document.addEventListener('DOMContentLoaded', function () {
    // Capturamos todas las imágenes con la clase "circle-image"
    const circleImages = document.querySelectorAll('.circle-image');
  
    // Recorremos las imágenes y agregamos los eventos
    circleImages.forEach(image => {
      // Obtenemos el texto adicional del atributo "data-text"
      const additionalText = image.dataset.text;
  
      // Creamos un párrafo para mostrar el texto adicional
      const paragraph = document.createElement('p');
      paragraph.textContent = additionalText;
  
      // Ocultamos el párrafo inicialmente
      paragraph.style.display = 'none';
  
      // Agregamos el párrafo después de la imagen
      image.parentNode.insertBefore(paragraph, image.nextSibling);
  
      // Agregamos eventos para mostrar y ocultar el párrafo al hacer clic en la imagen
      image.addEventListener('click', () => {
        paragraph.style.display = paragraph.style.display === 'none' ? 'block' : 'none';
      });
    });
  });
  