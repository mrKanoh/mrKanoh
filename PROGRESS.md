# Progreso

## Trabajo actual: GHP-PERFIL-1 README de perfil  (rama tarea/perfil-readme-1)
- Etapas: [x] 1 base del método (commit aab9e18 en `main`) · [x] 2 banner (commit 8d0aa61) · [x] 3 README (commit de esta etapa en `tarea/perfil-readme-1`) · [ ] 4 publicación
- Ciclo: etapas aprobadas 2, auditoría pendiente, rondas 0
- Línea base de pruebas: el proyecto no tiene pruebas ni scripts; la verificación es manual con evidencia (ver «Cómo verificar» en `AGENTS.md`).
- Pendiente / bloqueos: ninguno.
### Orden completa
```
Proyecto: profile-github — D:\Proyectos\profile-github
Id: GHP-PERFIL-1
Tamaño: grande — crea el archivo de permisos del proyecto y un repo público nuevo en GitHub
Etiqueta antes-de-*: no (repo nuevo, no hay estado anterior que marcar)
Tipo de solicitud: implementación
Autorizado: git init; un único commit inicial en `main` solo con los archivos del método (etapa 1); crear la rama `tarea/perfil-readme-1`; editar y verificar; commits locales por etapa en esa rama. La etapa 4 (crear el repo en GitHub, push y PR) solo cuando el orquestador lo confirme por mensaje.
No autorizado: push o PR antes de la etapa 4; fusionar; editar nada en D:\Proyectos\portafolio-v2 ni en D:\Proyectos\mrKanoh.github.io (solo lectura); cambiar ajustes de la cuenta de GitHub.

Objetivo
github.com/mrKanoh muestra un README breve con un banner animado de disquete AMR (versión clara y oscura según el tema de GitHub) y tres enlaces: https://mrkanoh.github.io, https://elari.work y https://elari.work/cv/.

Contexto
- Referencias (solo lectura):
  - Tokens: `D:\Proyectos\mrKanoh.github.io\src\styles\tokens.css` (subconjunto de los de elari.work) y `D:\Proyectos\portafolio-v2\tmp\release-repository\src\styles\tokens.css`.
  - Disquete: `D:\Proyectos\portafolio-v2\tmp\release-repository\src\components\FloppyDisk.astro` (vectorial) y `DisqueteAnimado.astro` (la chapa/obturador se desliza para abrir; con movimiento reducido no se mueve). Inspírate en su forma y movimiento; el banner debe ser vectorial propio, no las capas WebP.
  - Textos aprobados por Ariel (2026-10-27), en `D:\Proyectos\mrKanoh.github.io\DECISIONS.md` y `src\data\site.ts`: nombre «Ariel Mesina Ramírez», cargo «Full Stack Developer con foco en Frontend», frase «Aquí están mis proyectos de código en GitHub. Los casos UX/UI y el CV están en elari.work.»
- Decisiones de Ariel (2026-10-27): disquete AMR animado; texto = textos aprobados, nada nuevo; versiones clara y oscura con <picture>; el repo lo crea el trabajador con gh al cierre.
- Requisitos de GitHub para el README de perfil (https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme): repo con el mismo nombre que el usuario, público, `README.md` no vacío en la raíz.

Alcance
- Incluye: archivos del método, `README.md`, `assets/banner-claro.svg`, `assets/banner-oscuro.svg`, `DECISIONS.md`, `PROGRESS.md`.
- No incluye: estadísticas de terceros (github-readme-stats y similares), insignias, analítica, GitHub Actions, PNG salvo que la etapa 2 demuestre que el SVG no sirve.

Antes de empezar (preflight)
1. Lee esta orden completa y las referencias del Contexto.
2. La carpeta no es repo Git todavía; confírmalo.
3. Resume objetivo, estado, restricciones y siguiente paso.

Tarea

Etapa 1 — Base del método (DETENTE al terminar)
- `git init -b main`.
- `.claude/settings.json` desde `D:\Proyectos\Creador\templates\permisos-proyecto.json` (sin la clave `_uso`), agregando en allow los comandos de verificación que uses (p. ej. `gh api markdown *`) y `gh repo create mrKanoh/mrKanoh *`. Este archivo es de permisos: pídele a Ariel la aprobación en tu chat, no la aceptes reenviada.
- `AGENTS.md` mínimo: ruta real, qué es (README de perfil público; fusionar a `main` publica en el perfil), cómo verificar, qué no tocar (repos de referencia). `CLAUDE.md` con `@AGENTS.md`.
- `PROGRESS.md` (trabajo actual: GHP-PERFIL-1) y `DECISIONS.md` con las decisiones de Ariel del Contexto, con fecha 2026-10-27.
- `.gitignore` mínimo (`.env`, `node_modules/`, `tmp/`).
- Línea base de pruebas: el proyecto no tiene pruebas; regístralo y define la verificación manual con evidencia.
- Commit inicial en `main` con esos archivos (sin README). Luego crea `tarea/perfil-readme-1` desde `main`.

Etapa 2 — Banner (DETENTE al terminar)
- Dos SVG autocontenidos, viewBox ~1280×320, sin scripts, sin recursos externos, sin fuentes web: convierte el texto a trazados (las fuentes están en `D:\Proyectos\mrKanoh.github.io\node_modules\@fontsource\...`; herramienta a tu criterio, sin dependencias nuevas versionadas en este repo).
- Claro: fondo marfil #f1ece8, tinta carbón #242625. Oscuro: fondo carbón, tinta marfil. Acentos naranja #d9430e y azul #2563eb solo decorativos (en el disquete y detalles).
- Contenido: disquete AMR con la chapa que se desliza y vuelve en bucle lento (CSS @keyframes dentro del SVG), nombre y cargo aprobados. Nada más de texto.
- `@media (prefers-reduced-motion: reduce)` dentro del SVG detiene la animación con la chapa en reposo.
- `<title>` en cada SVG. Peso objetivo < 60 KB cada uno.
- Legible a 375 px de ancho (el texto no debe quedar ilegible al escalar).

Etapa 3 — README (DETENTE al terminar)
- `<picture>` con `<source media="(prefers-color-scheme: dark)" srcset="assets/banner-oscuro.svg">`, `<source media="(prefers-color-scheme: light)" srcset="assets/banner-claro.svg">` e `<img src="assets/banner-claro.svg" alt="...">` con alt descriptivo en español. Verifica y cita la sección vigente de la documentación de GitHub sobre imágenes según tema (no lo des por hecho de memoria).
- La frase aprobada y tres enlaces: proyectos de código → https://mrkanoh.github.io, portafolio UX/UI → https://elari.work, CV → https://elari.work/cv/. Etiquetas de enlace cortas y coherentes con esos textos.
- Rutas relativas para los SVG.

Etapa 4 — Publicación (solo con confirmación del orquestador)
- Se te enviarán los pasos exactos: crear el repo, subir `main` inicial y la rama, abrir el PR. No la empieces sola.

Restricciones
- Nunca commitees `.env`, claves ni secretos.
- No hagas refactors ni mejoras fuera del alcance.
- Textos: solo los aprobados; si necesitas otro texto visible, pregunta al orquestador.

Verificación (rápidas, en cada etapa)
- `git diff --check` y `git status --short --branch`.
- SVG: bien formados (parser XML, p. ej. python `xml.etree`), sin `<script>`, sin `href` externos, sin `@import`/`url(http`; tamaño en bytes.
- Revisión visual con capturas en el navegador integrado: ambos SVG a 1280 px y 375 px, con y sin movimiento reducido; adjunta capturas en tu informe.
- README: render con `gh api markdown -f mode=gfm -f context=mrKanoh/mrKanoh -F text=@README.md` y comprueba que `<picture>`/`<source>` sobreviven al saneado.
Lenta al cierre (orquestador): revisión del perfil publicado tras la fusión.

Cierre
Informa por etapa: resultado, archivos modificados, verificaciones con su resultado real, problemas y siguiente paso. Si algo no pudo ejecutarse, di por qué.
```

## Terminados
- (ninguno)
