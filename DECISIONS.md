# Decisiones

## 2026-10-27 — README de perfil de mrKanoh (Ariel)

- **Motivo del banner:** disquete AMR animado (la chapa del obturador se desliza y vuelve), en el estilo de elari.work: marfil, carbón, naranja y azul; Inter e IBM Plex Mono.
- **Texto:** solo los textos ya aprobados para https://mrkanoh.github.io (`D:\Proyectos\mrKanoh.github.io\DECISIONS.md` y `src\data\site.ts`); nada nuevo.
  - Nombre: «Ariel Mesina Ramírez».
  - Cargo: «Full Stack Developer con foco en Frontend».
  - Frase: «Aquí están mis proyectos de código en GitHub. Los casos UX/UI y el CV están en elari.work.»
- **Temas:** versión clara y oscura del banner, elegidas con `<picture>` según el tema de GitHub.
  - Fuente del patrón: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax (sección «The Picture element»: solo dice que `<picture>` está soportado) y el ejemplo oficial en https://github.blog/changelog/2022-08-15-specify-theme-context-for-images-in-markdown-ga.
- **Repo:** `mrKanoh/mrKanoh` (público, mismo nombre que el usuario, como exige GitHub para el README de perfil). Lo crea el trabajador con `gh` al cierre de GHP-PERFIL-1.

## 2026-10-27 — Diseño del banner (GHP-PERFIL-1, etapa 2; propuesta del trabajador, aceptada por el orquestador)

- **Disquete:** forma de `FloppyDisk.astro` de elari.work (280 × 280, esquina cortada, chapa metálica #c7c6c2, etiqueta marfil con franja azul de módulos). Carcasa naranja #d9430e en ambos temas, para que el disquete sea el mismo sobre marfil y sobre carbón. La etiqueta no lleva texto.
- **Movimiento:** la chapa se desliza 36 unidades a la izquierda (≈ 12,9 % del ancho, como el recorrido de `DisqueteAnimado.astro`), deja ver la ventana del disco y vuelve; ciclo de 8 s. Con `prefers-reduced-motion: reduce` no hay animación y la chapa queda cerrada.
- **Texto:** nombre en Inter 600 (76 px) y cargo en IBM Plex Mono 400 (46 px) en dos líneas («Full Stack Developer» / «con foco en Frontend»), sin cambiar el texto aprobado. Dos líneas para que el cargo mida ≈ 13 px cuando el banner se ve a 375 px.
- **Trazados:** el texto se convirtió a trazados con fontTools (kerning por pares de GPOS) desde los `.woff2` de `@fontsource` de `mrKanoh.github.io`. El script quedó fuera del repo: no se versionan dependencias ni herramientas.

## 2026-10-28 — Escritorio retro (GHP-PERFIL-2; aprobado por Ariel)

- **Composición:** el banner actual dentro de una ventana con barra de título azul «AMR»; debajo de la frase, tres ventanas SVG que son los enlaces a Proyectos, Portafolio UX/UI y CV. Estética coherente con elari.work: ventana con borde carbón, cuerpo marfil #f1ece8, barra con etiqueta en IBM Plex Mono mayúsculas.
- **Escala:** las medidas se fijan por legibilidad al ancho en que GitHub muestra la imagen (≈ 343–830 px), no en px de elari.work (borde 1 px, barra 32 px, etiqueta 12 px), que dentro de un SVG escalado no se conservan. Banner (viewBox 1280 × 404; corrección ab804af): barra de 84 unidades con etiqueta de 46 (≈ 13 px a 343 px) y borde de 3. Ventanas-enlace (270 × 124, mostradas a 270 px): barra de 36, etiqueta de 13, cuerpo en Inter 600 de 19, borde de 1.
- **Textos aprobados (exactos):**
  - Barra del banner: «AMR» (de `site.ts` de mrkanoh.github.io). Banner, nombre y cargo sin cambios; frase sin cambios.
  - Ventana 1: barra azul #2563eb «ARCHIVOS»; cuerpo «Proyectos de código ↗»; enlace https://mrkanoh.github.io.
  - Ventana 2: barra naranja #b9370a «AMR / ESPACIO DE TRABAJO»; cuerpo «Portafolio UX/UI ↗»; enlace https://elari.work.
  - Ventana 3: barra carbón #242625 «MI PERFIL / CV»; cuerpo «Abrir CV ↗»; enlace https://elari.work/cv/.
  - «ARCHIVOS», «AMR / ESPACIO DE TRABAJO», «MI PERFIL / CV» y «Abrir CV» vienen de elari.work.
- **Ventanas-enlace:** un solo diseño para ambos temas (cuerpo marfil, borde carbón, barra de color); no hay versión oscura.
- **Alt:** banner «Ventana retro con el disquete naranja de la marca AMR junto al nombre Ariel Mesina Ramírez y el cargo Full Stack Developer con foco en Frontend»; ventanas «Proyectos de código», «Portafolio UX/UI» y «CV».

## 2026-10-28 — GHP-PERFIL-3, solo registro (aprobado por Ariel; no implementado)

- **Actividad del año como «desfragmentador de disco»:** ventana con barra «DESFRAGMENTADOR», un bloque por día (marfil sin actividad, azul poca, naranja mucha), leyenda «Sin actividad · Poca · Mucha», línea animada «Desfragmentando…», sin números. Alt: «Actividad del último año en GitHub, mostrada como el mapa de bloques de un desfragmentador de disco».
- **Actualización diaria:** Ariel autoriza que el repo se actualice solo una vez al día con GitHub Actions. La regla «Sin GitHub Actions» de `AGENTS.md` se cambia en GHP-PERFIL-3, no antes.
