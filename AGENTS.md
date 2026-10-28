# profile-github

- **Ruta real:** `D:\Proyectos\profile-github`.
- **Qué es:** el README de perfil público de la cuenta de GitHub `mrKanoh` (repo `mrKanoh/mrKanoh`). GitHub muestra el `README.md` de la raíz de la rama principal en https://github.com/mrKanoh, así que **fusionar a `main` publica en el perfil**.
- **Contenido:** `README.md` y los banners `assets/banner-claro.svg` y `assets/banner-oscuro.svg`. Sin build, sin dependencias, sin GitHub Actions.

## Cómo verificar

El proyecto no tiene pruebas automáticas. La verificación es manual, con evidencia:

1. `git diff --check` y `git status --short --branch`.
2. SVG: bien formados con un parser XML (p. ej. `xml.etree` de Python), sin `<script>`, sin `href` externos, sin `@import` ni `url(http`; tamaño en bytes.
3. Revisión visual de ambos SVG en el navegador a 1280 px y 375 px de ancho, con y sin movimiento reducido (capturas en el informe).
4. README: `gh api markdown -f mode=gfm -f context=mrKanoh/mrKanoh -F text=@README.md` y comprobar que `<picture>`/`<source>` sobreviven al saneado.

## Qué no tocar

- `D:\Proyectos\portafolio-v2` y `D:\Proyectos\mrKanoh.github.io`: solo lectura (referencias de tokens, disquete y textos aprobados).
- Ajustes de la cuenta de GitHub.
- Textos visibles: solo los aprobados por Ariel (ver `DECISIONS.md`).
