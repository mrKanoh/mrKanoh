# Progreso

## Trabajo actual: GHP-PERFIL-3 desfragmentador  (rama tarea/perfil-desfrag-3)
- Etapas: [x] 1 generador y SVG (commit e344802) · [x] 2 workflow, README y AGENTS.md (commit c8bafb4; corrección ronda 1: este) · [ ] 3 cierre
- Ciclo: etapas aprobadas 1, auditoría hecha (pasada 1), rondas 1
- Línea base de pruebas: el proyecto no tiene pruebas automáticas; verificación manual (AGENTS.md).
- Pendiente / bloqueos: revisión de la corrección de la etapa 2 (ronda 1: rebase antes del push, riesgo de GITHUB_TOKEN, errores sin datos en logs). Barra carbón pendiente de confirmación de Ariel. Protección de `main` no leída.
### Orden completa
```
Proyecto: profile-github — D:\Proyectos\profile-github
Id: GHP-PERFIL-3
Tamaño: grande — agrega un workflow de GitHub Actions con permiso de escritura que hace commits a main (infraestructura/permisos).
Etiqueta antes-de-*: sí (antes-de-perfil-3, en 2ebcc4c)
Tipo de solicitud: implementación
Autorizado: crear la rama tarea/perfil-desfrag-3 desde main actualizada, editar y verificar, un commit local por etapa verificada, la etiqueta local antes-de-perfil-3. Consultas de solo lectura a la API de GitHub con gh (gh api graphql para leer el calendario; gh api repos/mrKanoh/mrKanoh/actions/permissions y .../actions/permissions/workflow, solo GET).
No autorizado: push, PR, merge, ejecutar workflows en GitHub, cambiar ajustes del repo o de la cuenta (incluido el de «contribuciones privadas»), borrar ramas (tarea/perfil-readme-1 se queda: decisión de Ariel), textos visibles no aprobados.

Objetivo
El README muestra, debajo de las tres ventanas-enlace, una ventana SVG «DESFRAGMENTADOR» con un bloque por día del último año (marfil sin actividad, azul poca, naranja mucha), una leyenda «Sin actividad · Poca · Mucha» y una línea animada «Desfragmentando…», sin números. Un workflow diario regenera el SVG y hace commit solo si cambió.

Contexto (leer antes)
- DECISIONS.md, sección «GHP-PERFIL-3, solo registro»: textos, colores y alt exactos. Sección «Escritorio retro»: estilo de ventana (borde carbón, cuerpo marfil #f1ece8, barra de color con etiqueta IBM Plex Mono mayúsculas) y paleta (#2563eb azul, #b9370a naranja, #242625 carbón).
- LESSONS.md: el texto del SVG se dimensiona por el ancho mostrado (≈ 12–13 px a 343 px), no por px CSS; verificar con capturas a 343 y 830 px antes del commit.
- Los banners existentes convierten el texto a trazados (fontTools, fuentes .woff2 de @fontsource de D:\Proyectos\mrKanoh.github.io, solo lectura). Haz lo mismo con los textos fijos de esta ventana; el script de conversión queda fuera del repo (en tmp/, ignorado), como en GHP-PERFIL-1.
- Documentación oficial verificada por el orquestador (2026-10-28):
  * https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows — schedule: solo corre en la rama por defecto y si el archivo existe ahí; puede retrasarse con carga alta; «In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days.»
  * https://docs.github.com/en/actions/concepts/security/github_token — permisos limitados al repo del workflow; los eventos generados con GITHUB_TOKEN no disparan otros workflows (no hay bucle de push).
  * https://docs.github.com/en/graphql/reference/users — User.contributionsCollection (from/to; por defecto un año), contributionCalendar, ContributionCalendarDay.contributionCount/contributionLevel/date, enum ContributionLevel (NONE, FIRST..FOURTH_QUARTILE), restrictedContributionsCount «Only non-zero when the user has chosen to share their private contribution counts».
  * Conclusión: con GITHUB_TOKEN el calendario incluye las contribuciones privadas solo como conteo y solo si Ariel tiene activado «Private contributions» en su perfil; la documentación no lo confirma de forma explícita para GITHUB_TOKEN. No cambies ese ajuste.

Alcance
- Incluye: generador sin dependencias (Python 3 stdlib) que consulta GraphQL con el token de entorno y escribe assets/ventana-desfragmentador.svg; el SVG; el workflow .github/workflows/desfragmentador.yml; la línea en README.md; el cambio de la regla «Sin GitHub Actions» en AGENTS.md (y su sección «Cómo verificar»); DECISIONS.md con medidas reales, mapeo de niveles y riesgos; PROGRESS.md.
- No incluye: cambios a banners o ventanas existentes, versión oscura (un solo diseño para ambos temas, como las ventanas-enlace; **Estoy suponiendo** esto por coherencia con GHP-PERFIL-2), números o fechas visibles, dependencias de npm o pip, acciones de terceros salvo actions/checkout y actions/setup-python oficiales fijadas por SHA de commit.

Antes de empezar (preflight)
1. Lee AGENTS.md, DECISIONS.md, LESSONS.md, PROGRESS.md.
2. git status --short --branch; trata los cambios existentes como ajenos. git switch main && git pull --ff-only; crea antes-de-perfil-3 en main y la rama tarea/perfil-desfrag-3.
3. Resume objetivo, estado, restricciones y siguiente paso.

Tarea (al terminar y verificar cada etapa: commit local, actualiza PROGRESS.md, DETENTE e informa)

Etapa 1 — Generador y SVG
- Mapeo de niveles (Estoy suponiendo; regístralo en DECISIONS): NONE → marfil (sin actividad); FIRST y SECOND_QUARTILE → azul (poca); THIRD y FOURTH_QUARTILE → naranja (mucha). Usa contributionLevel, no los conteos, y no escribas conteos en el SVG.
- Rejilla de 53 columnas × 7 filas por semana como el calendario. Elige medidas por legibilidad: ventana mostrada al ancho del README (≈ 343–830 px); bloques distinguibles a 343 px. Barra «DESFRAGMENTADOR», leyenda y línea «Desfragmentando…» con texto como trazados. Animación CSS dentro del SVG solo en la línea «Desfragmentando…» (y, si quieres, un barrido sutil); con prefers-reduced-motion: reduce, sin animación.
- El SVG debe ser determinista (misma entrada → mismos bytes) para que el workflow no haga commits vacíos.
- Privacidad: el SVG que se commitea en esta etapa NO puede salir de tu token personal (tu token ve las privadas aunque Ariel las tenga ocultas). Commitea el SVG generado con un calendario sin actividad (todo NONE) como estado inicial; el primer run del workflow tras la fusión lo reemplaza. Para revisar el aspecto real, genera con datos reales solo en tmp/ (ignorado) y no lo commitees.
- El generador debe fallar con código distinto de 0 (sin escribir el SVG) si la consulta falla o la respuesta no trae ~365 días; así un error no publica un mapa vacío.
- Verificación: generador con datos reales a tmp/ y con todo NONE a assets/; parser XML, sin <script>, sin href externos, sin @import ni url(http; tamaño en bytes; determinismo (dos ejecuciones con la misma entrada, mismo hash); capturas a 343 y 830 px y con movimiento reducido.

Etapa 2 — Workflow, README y AGENTS.md
- .github/workflows/desfragmentador.yml: on schedule (una vez al día, hora fija fuera del minuto 0) y workflow_dispatch; permissions a nivel de workflow solo contents: write; concurrency para no solapar; checkout y setup-python fijados por SHA con el tag en comentario; ejecuta el generador con GITHUB_TOKEN; si git diff no muestra cambios, termina sin commit; si cambió, commit con autor github-actions[bot] y push a main. Sin otros secretos.
- Riesgo de 60 días: documenta en DECISIONS que la ventana del calendario avanza a diario, así que en la práctica habrá un commit casi cada día; la documentación no dice si los commits del bot cuentan como «repository activity»: déjalo como riesgo con su mitigación (si GitHub lo desactiva, Ariel lo reactiva en la pestaña Actions).
- Lee (solo GET) los permisos de Actions del repo y de GITHUB_TOKEN por defecto e informa si algo impide contents: write; no los cambies.
- README.md: la ventana debajo de las tres ventanas-enlace, sin enlace, con el alt aprobado exacto y width/height coherentes.
- AGENTS.md: reemplaza «Sin GitHub Actions» por la regla nueva (un solo workflow diario que regenera assets/ventana-desfragmentador.svg; no agregar otros sin decisión de Ariel) y agrega las verificaciones del workflow.
- Verificación: actionlint (si está instalado; si no, dilo), gh api markdown con el README y comprobar que la nueva <img> sobrevive, git diff --check.

Etapa 3 — Cierre
- DECISIONS.md con medidas reales, mapeo y riesgos; LESSONS.md solo si hubo retrabajo; PROGRESS.md con GHP-PERFIL-3 en «Terminados» (pendiente: push, PR y fusión con autorización de Ariel; primer run manual con workflow_dispatch tras la fusión) y «Trabajo actual: ninguno». git status --short vacío.

Restricciones
- Nunca commitees .env, tokens ni salidas con datos personales; no imprimas el token.
- Textos visibles: solo «DESFRAGMENTADOR», «Sin actividad», «Poca», «Mucha», «Desfragmentando…» y el alt aprobado.
- No hagas refactors ni mejoras fuera del alcance. No toques portafolio-v2 ni mrKanoh.github.io (solo lectura).

Verificación
Rápidas, en cada etapa (tú): las de AGENTS.md («Cómo verificar») que apliquen, más las de cada etapa.
Lenta al cierre (orquestador): revisión visual del README renderizado y de los SVG, gh api markdown, actionlint, gitleaks. El run real del workflow solo es posible tras la fusión (schedule y workflow_dispatch exigen el archivo en main): queda como verificación posterior.

Cierre
Informa: resultado, archivos modificados, verificaciones con su resultado real, problemas (separa los preexistentes) y siguiente paso.
```

## Terminados
- 2026-10-28 GHP-PERFIL-2 — escritorio retro: banners claro y oscuro como ventana con barra azul «AMR» (escala legible a 343 px) y tres ventanas-enlace SVG (Proyectos, Portafolio UX/UI, CV) en el README · Ciclo: etapas aprobadas 3, auditoría hecha, rondas 0 · commits fa64e08, 31bab8f, ab804af, f5012df y el de cierre (rama tarea/perfil-retro-2, sin push) · `gh api markdown` ya corrido: `<picture>`, `<source>`, `<a>` e `<img alt>` sobreviven · pendiente: PR y fusión por Ariel · siguiente: GHP-PERFIL-3 (desfragmentador, solo registrado en DECISIONS.md).
- 2026-10-27 GHP-PERFIL-1 — README de perfil con banner SVG animado de disquete AMR (claro y oscuro con `<picture>`), frase aprobada y enlaces a mrkanoh.github.io, elari.work y elari.work/cv/ · Ciclo: etapas aprobadas 3, auditoría hecha, rondas 0 · commits aab9e18 (main), 8d0aa61, 32e6ebc y el de cierre · publicación: PR pendiente de fusión por Ariel · observaciones bajas aceptadas: el fondo carbón no es el del tema oscuro de GitHub (decisión de marca); el alt menciona «AMR» (nombre del sitio ya aprobado).
