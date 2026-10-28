# Progreso

## Trabajo actual: GHP-PERFIL-2 Escritorio retro  (rama tarea/perfil-retro-2)
- Etapas: [x] 1 rama, etiqueta antes-de-perfil-retro-2 y decisiones · [ ] 2 banners como ventana con barra «AMR» · [ ] 3 tres ventanas-enlace + README
- Ciclo: etapas aprobadas 0, auditoría pendiente, rondas sin dato
- Línea base de pruebas: sin pruebas automáticas; verificación manual (ver AGENTS.md)
- Pendiente / bloqueos: ninguno
- Siguiente: GHP-PERFIL-3 (desfragmentador de actividad; solo registrado en DECISIONS.md)
### Orden completa
Id: GHP-PERFIL-2. Objetivo: el README de perfil pasa a una estética de «escritorio retro» coherente con elari.work: el banner actual dentro de una ventana con barra de título, y debajo de la frase tres ventanas SVG que son los enlaces a Proyectos, Portafolio UX/UI y CV. Tamaño normal; etiqueta antes-de-perfil-retro-2; implementación. Autorizado: rama tarea/perfil-retro-2, editar, verificar, commits locales por etapa. No autorizado: push, PR, merge, borrar ramas, ajustes de la cuenta, workflows, editar portafolio-v2 o mrKanoh.github.io, textos no aprobados. Etapas: 1 rama + decisiones (DECISIONS/PROGRESS); 2 banners con ventana y barra azul «AMR» conservando disquete, animación 8 s, reduced-motion y trazados; 3 tres SVG ventana-enlace + README con `<a><img alt></a>`, legibles a 375 px, conservando `<picture>` y frase. Textos aprobados en DECISIONS.md (2026-10-28). Verificación rápida por etapa: git diff --check, git status, SVG con xml.etree y búsqueda de `<script|href=|@import|url(http`, tamaños, capturas a 1280 y 375 px con y sin movimiento reducido. Lenta (orquestador): gh api markdown + auditoría.
## Terminados
- 2026-10-27 GHP-PERFIL-1 — README de perfil con banner SVG animado de disquete AMR (claro y oscuro con `<picture>`), frase aprobada y enlaces a mrkanoh.github.io, elari.work y elari.work/cv/ · Ciclo: etapas aprobadas 3, auditoría hecha, rondas 0 · commits aab9e18 (main), 8d0aa61, 32e6ebc y el de cierre · publicación: PR pendiente de fusión por Ariel · observaciones bajas aceptadas: el fondo carbón no es el del tema oscuro de GitHub (decisión de marca); el alt menciona «AMR» (nombre del sitio ya aprobado).
