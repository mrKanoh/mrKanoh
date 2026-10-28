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
