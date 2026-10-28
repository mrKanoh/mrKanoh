# Progreso

## Trabajo actual: GHP-PERFIL-6 panel de control y barra de tareas  (rama tarea/perfil-panel-6)
- Etapas: [x] 1 dos SVG nuevos (commit en esta rama) · [ ] 2 README, DECISIONS y cierre
- Ciclo: etapas aprobadas 0, auditoría pendiente, rondas 0
- Línea base de pruebas: el proyecto no tiene pruebas automáticas; verificación manual.
- Pendiente / bloqueos: ninguno. Etapa 1: `assets/ventana-panel-de-control.svg` (830 × 510, 4 × 3 iconos, 34 768 bytes) y `assets/barra-de-tareas.svg` (830 × 72, 5 345 bytes), generados con un script fuera del repo (`tmp/panel.py`).
### Orden completa
Proyecto: profile-github — D:\Proyectos\profile-github
Id: GHP-PERFIL-6
Tamaño: normal — 2 SVG nuevos + README + DECISIONS + PROGRESS, sin lógica ni workflow
Etiqueta antes-de-*: sí (antes-de-perfil-panel-6)
Tipo de solicitud: implementación
Autorizado: actualizar main local con `git pull --ff-only`, crear la rama tarea/perfil-panel-6 y la etiqueta local antes-de-perfil-panel-6, editar los archivos del alcance y hacer un commit local por etapa verificada.
No autorizado: push, PR, merge, tocar el workflow, scripts/, los banners ni las ventanas existentes, ajustes de la cuenta de GitHub, editar D:\Proyectos\portafolio-v2 o D:\Proyectos\mrKanoh.github.io (solo lectura).

Objetivo
El README muestra, después del desfragmentador, una ventana «PANEL DE CONTROL» con las herramientas de Ariel como iconos retro y, al final, una barra de tareas estilo Windows 95 con «Inicio» y «2026», ambas coherentes con las ventanas existentes y legibles a 375 px.

Contexto
Textos visibles aprobados por Ariel (2026-10-28), sin agregar otros:
- Título de ventana: «PANEL DE CONTROL».
- Herramientas, una etiqueta por icono, en este orden: HTML, CSS, JavaScript, TypeScript, React, Astro, Node.js, Tailwind, Git, Python, Figma, FigJam (lista del CV aprobado en elari.work, «código + diseño»).
- Barra de tareas: botón «Inicio» a la izquierda y «2026» fijo a la derecha.
Estoy suponiendo estos alt (texto no visible, accesible): «Panel de control con las herramientas que uso: HTML, CSS, JavaScript, TypeScript, React, Astro, Node.js, Tailwind, Git, Python, Figma y FigJam» y «Barra de tareas retro con el botón Inicio y el año 2026». Regístralos en DECISIONS.md como suposición del orquestador.

Alcance
- Incluye:
  R1. `assets/ventana-panel-de-control.svg`: misma construcción que `assets/ventana-cv.svg` y `assets/ventana-desfragmentador.svg` (paleta, borde, barra de título oscura, texto convertido a trazados como ellas, sin fuentes externas). Ancho 830 como el desfragmentador; alto el que pida una cuadrícula de 12 iconos (p. ej. 6 × 2) legible al escalar a 343 px. Iconos dibujados originales y genéricos estilo Windows 95 (carpeta, documento, engranaje, etc.), con la etiqueta de texto debajo: no copies logos oficiales de marcas.
  R2. `assets/barra-de-tareas.svg`: franja de 830 de ancho, botón «Inicio» con un icono pequeño original (p. ej. el disquete AMR simplificado si ya existe en los banners, o un cuadrado genérico) y «2026» en un recuadro hundido a la derecha. Sin animación; si agregas alguna, debe respetar `prefers-reduced-motion`.
  R3. README: agregar las dos imágenes después del desfragmentador, con `width`/`height` reales y los alt del Contexto; sin enlaces. No cambies nada más del README.
  R4. DECISIONS.md: entrada «2026-10-28 — Panel de control y barra de tareas (GHP-PERFIL-6; textos aprobados por Ariel)» con textos, medidas, alt y la regla de iconos originales. PROGRESS.md: trabajo actual y, al cerrar, la entrada en Terminados.
- No incluye: datos en vivo, cambios al workflow o al generador, enlaces nuevos, otros textos.

Tarea (detente e informa al cerrar cada etapa; espera «Aprobado» del orquestador)
Etapa 1: rama tarea/perfil-panel-6 desde main actualizada, etiqueta antes-de-perfil-panel-6, R1 y R2 (solo los dos SVG). Verifica y haz commit.
Etapa 2: R3 y R4, revisión visual del README completo, verifica y haz commit de cierre con PROGRESS.md cerrado.

Restricciones
- Español neutro con «tú» en documentación.
- No refactorices ni reformatees archivos existentes.
- Nada de `<script>`, `href` externos, `@import` ni `url(http` en los SVG.

Verificación (rápidas, en cada etapa)
- `git diff --check`, `git status --short --branch`, `git show --stat HEAD`.
- SVG bien formados con `python -c "import xml.etree.ElementTree as E,sys;[E.parse(f) for f in sys.argv[1:]]" assets/*.svg`; grep sin `<script`, `href="http`, `@import`, `url(http`; tamaño en bytes de cada SVG nuevo.
- Revisión visual en el navegador a 1280 px y 375 px de ancho (etapa 1: los dos SVG; etapa 2: el README renderizado), con capturas en el informe.
- Etapa 2: `gh api markdown -f mode=gfm -f context=mrKanoh/mrKanoh -F text=@README.md` y confirmar que las `<img>` nuevas sobreviven con su alt.
Lenta: no hay (sin pruebas automáticas).

Cierre
Informa: resultado, archivos modificados, verificaciones con su salida real, capturas, problemas (separa los preexistentes) y siguiente paso.

## Terminados
- 2026-10-28 GHP-PERFIL-5 — PROGRESS.md al día tras la fusión de GHP-PERFIL-4 · Ciclo: etapas aprobadas 1, auditoría no aplica (tarea chica), rondas 0 · commit el de esta tarea (rama tarea/perfil-progress-5) · pendiente: PR y fusión por Ariel.
- 2026-10-28 GHP-PERFIL-4 — la ventana «DESFRAGMENTADOR» muestra «<N> contribuciones en el último año» (N = `totalContributions` de GraphQL, entero 0–9 999 999 o el generador sale con código 1 sin escribir; singular si N = 1), sin leyenda, con «Compilando ideas…» junto a la barra; viewBox sin cambios (830 × 312), medidas en `DECISIONS.md` · Ciclo: etapas aprobadas 2, auditoría hecha, rondas 0 · commits ad305bf, 8c77481 y el de cierre (rama tarea/perfil-contrib-4) · pendiente: nada de GHP-PERFIL-4 (fusionado por PR #4 en 092e246; run manual 40760056536, éxito, 2026-10-28; commit del bot 2dd580b con 1069 contribuciones, igual al total de GraphQL).
- 2026-10-28 GHP-PERFIL-3 — ventana «DESFRAGMENTADOR» con la actividad del último año (53 × 7 bloques por `contributionLevel`, leyenda y línea animada, sin números) en el README, generada por `scripts/desfragmentador.py` (Python stdlib) y regenerada a diario por `.github/workflows/desfragmentador.yml` (solo `contents: write`, checkout fijado por SHA, commit solo si cambió); SVG versionado sin actividad hasta el primer run · Ciclo: etapas aprobadas 3, auditoría hecha, rondas 1 · commits e344802, c8bafb4, 42d619d y el de cierre (rama tarea/perfil-desfrag-3) · pendiente: nada de GHP-PERFIL-3 (fusionado por PR #3; primer run manual con workflow_dispatch hecho, runs 40741639404 y 40742296945, éxito, 2026-10-28).
- 2026-10-28 GHP-PERFIL-2 — escritorio retro: banners claro y oscuro como ventana con barra azul «AMR» (escala legible a 343 px) y tres ventanas-enlace SVG (Proyectos, Portafolio UX/UI, CV) en el README · Ciclo: etapas aprobadas 3, auditoría hecha, rondas 0 · commits fa64e08, 31bab8f, ab804af, f5012df y el de cierre (rama tarea/perfil-retro-2, sin push) · `gh api markdown` ya corrido: `<picture>`, `<source>`, `<a>` e `<img alt>` sobreviven · pendiente: PR y fusión por Ariel · siguiente: GHP-PERFIL-3 (desfragmentador, solo registrado en DECISIONS.md).
- 2026-10-27 GHP-PERFIL-1 — README de perfil con banner SVG animado de disquete AMR (claro y oscuro con `<picture>`), frase aprobada y enlaces a mrkanoh.github.io, elari.work y elari.work/cv/ · Ciclo: etapas aprobadas 3, auditoría hecha, rondas 0 · commits aab9e18 (main), 8d0aa61, 32e6ebc y el de cierre · publicación: PR pendiente de fusión por Ariel · observaciones bajas aceptadas: el fondo carbón no es el del tema oscuro de GitHub (decisión de marca); el alt menciona «AMR» (nombre del sitio ya aprobado).
