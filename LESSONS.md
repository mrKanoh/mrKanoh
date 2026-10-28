# Lecciones

## Medidas en px CSS copiadas a un SVG que GitHub escala (GHP-PERFIL-2)

- **Qué salió mal:** la barra de 32 unidades y la etiqueta de 12 px de elari.work se copiaron a un viewBox de 1280 de ancho. GitHub muestra el banner a 343–830 px, así que la etiqueta quedó en ≈ 2–5 px y era ilegible. Se detectó en la revisión de la etapa 2.
- **Causa raíz:** los px CSS de una web no se conservan dentro de un SVG que se escala al ancho del contenedor.
- **Prevención:** dimensionar el texto del SVG según el ancho en que se mostrará (tamaño renderizado ≈ 12–13 px a 343 px) y verificar con una captura a 343 px y a 830 px antes del commit, no al tamaño natural del SVG.

## Workflow que hace push a `main` con logs públicos (GHP-PERFIL-3)

- **Qué salió mal:** la primera versión del workflow hacía `git push origin HEAD:main` sin integrar `main`, y los errores del generador volcaban el día completo (fecha y nivel) y la lista de errores de GraphQL. Lo detectó la auditoría de la etapa 2 (ronda 1).
- **Causa raíz:** se diseñó como un script local, donde la rama no avanza durante la ejecución y la salida de error solo la ve quien lo corre.
- **Prevención:** en todo workflow que haga commit, `git pull --rebase` antes del push y sin forzar nada. Los logs de Actions de un repo público son públicos: los mensajes de error nombran índices o conteos, nunca datos del usuario ni respuestas de la API completas.
