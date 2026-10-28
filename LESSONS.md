# Lecciones

## Medidas en px CSS copiadas a un SVG que GitHub escala (GHP-PERFIL-2)

- **Qué salió mal:** la barra de 32 unidades y la etiqueta de 12 px de elari.work se copiaron a un viewBox de 1280 de ancho. GitHub muestra el banner a 343–830 px, así que la etiqueta quedó en ≈ 2–5 px y era ilegible. Se detectó en la revisión de la etapa 2.
- **Causa raíz:** los px CSS de una web no se conservan dentro de un SVG que se escala al ancho del contenedor.
- **Prevención:** dimensionar el texto del SVG según el ancho en que se mostrará (tamaño renderizado ≈ 12–13 px a 343 px) y verificar con una captura a 343 px y a 830 px antes del commit, no al tamaño natural del SVG.
