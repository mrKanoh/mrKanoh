# profile-github

- **Ruta real:** `D:\Proyectos\profile-github`.
- **Qué es:** el README de perfil público de la cuenta de GitHub `mrKanoh` (repo `mrKanoh/mrKanoh`). GitHub muestra el `README.md` de la raíz de la rama principal en https://github.com/mrKanoh, así que **fusionar a `main` publica en el perfil**.
- **Contenido:** `README.md`, los banners `assets/banner-claro.svg` y `assets/banner-oscuro.svg`, las ventanas `assets/ventana-*.svg` y el generador `scripts/desfragmentador.py` (Python 3, solo biblioteca estándar). Sin build ni dependencias.
- **GitHub Actions:** un solo workflow, `.github/workflows/desfragmentador.yml`, que una vez al día regenera `assets/ventana-desfragmentador.svg` y hace commit a `main` solo si cambió. No agregar otros workflows ni ampliar sus permisos sin decisión de Ariel. El SVG versionado sale del workflow (`GITHUB_TOKEN`); nunca commitear uno generado con un token personal, que ve las contribuciones privadas.

## Cómo verificar

El proyecto no tiene pruebas automáticas. La verificación es manual, con evidencia:

1. `git diff --check` y `git status --short --branch`.
2. SVG: bien formados con un parser XML (p. ej. `xml.etree` de Python), sin `<script>`, sin `href` externos, sin `@import` ni `url(http`; tamaño en bytes.
3. Revisión visual de ambos SVG en el navegador a 1280 px y 375 px de ancho, con y sin movimiento reducido (capturas en el informe).
4. README: `gh api markdown -f mode=gfm -f context=mrKanoh/mrKanoh -F text=@README.md` y comprobar que `<picture>`/`<source>` sobreviven al saneado.
5. Workflow: `actionlint .github/workflows/desfragmentador.yml` sin errores; `permissions` solo `contents: write`; acciones fijadas por SHA de commit con el tag en comentario; el paso de commit solo agrega `assets/ventana-desfragmentador.svg`.
6. Generador: `python scripts/desfragmentador.py --vacio --salida tmp/a.svg` dos veces con el mismo hash; con una respuesta inválida (`--entrada`) sale con código 1 sin escribir. Los datos reales solo se generan en `tmp/` (ignorado).
7. Tras fusionar un cambio del workflow: ejecutarlo a mano (workflow_dispatch) y revisar el run y el commit del bot.

## Qué no tocar

- `D:\Proyectos\portafolio-v2` y `D:\Proyectos\mrKanoh.github.io`: solo lectura (referencias de tokens, disquete y textos aprobados).
- Ajustes de la cuenta de GitHub.
- Textos visibles: solo los aprobados por Ariel (ver `DECISIONS.md`).
