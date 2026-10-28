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

## 2026-10-28 — Ventana «DESFRAGMENTADOR» (GHP-PERFIL-3, etapa 1; propuesta del trabajador, aceptada por el orquestador)

- **Mapeo de niveles** (supuesto de la orden): se usa `contributionLevel`, nunca los conteos. `NONE` → marfil #f1ece8 (sin actividad); `FIRST_QUARTILE` y `SECOND_QUARTILE` → azul #2563eb (poca); `THIRD_QUARTILE` y `FOURTH_QUARTILE` → naranja #b9370a (mucha). La consulta solo pide `date`, `weekday` y `contributionLevel`.
- **Medidas** (viewBox 830 × 312, mostrado a ≈ 343–830 px): borde carbón de 2; barra carbón de 54 con «DESFRAGMENTADOR» en IBM Plex Mono 500 de 30 (≈ 12,4 px a 343 px); rejilla de 53 columnas × 7 filas, bloques de 11 con paso 14,5 (≈ 4,5 px con separación de 1,5 px a 343 px) sobre un panel carbón, que también queda visible donde no hay día (inicio y fin del año); leyenda y «Desfragmentando…» en IBM Plex Mono 400 de 30.
- **Barra carbón** (aprobada por Ariel, 2026-10-28): el carbón deja que el azul y el naranja de los bloques sean los únicos colores.
- **Animación:** solo la barra de 16 segmentos junto a «Desfragmentando…»: se llena por pasos en 7,2 s y queda llena hasta los 9 s. Con `prefers-reduced-motion: reduce` no hay animación y la barra queda a la mitad. Sin barrido en la rejilla.
- **Generador:** `scripts/desfragmentador.py` (Python 3, solo biblioteca estándar) consulta GraphQL con `GITHUB_TOKEN` o `GH_TOKEN`; sale con código 1 sin escribir si la consulta falla, hay errores o no llegan 364–371 días consecutivos (el calendario trae el año completado hasta el domingo inicial: 368 días el 2026-10-28). Dibuja las últimas 53 semanas. Determinista: misma entrada → mismos bytes.
- **Textos como trazados:** los trazados de los cinco textos fijos están en `scripts/desfragmentador_textos.json`, generado con fontTools desde los `.woff2` de `@fontsource` de `mrKanoh.github.io`; el script de conversión queda fuera del repo (`tmp/`), como en GHP-PERFIL-1. Así el generador no depende de fontTools en Actions.
- **Estado inicial:** el SVG versionado es el calendario sin actividad (`--vacio`, 53 semanas en `NONE`); nunca sale del token personal, que ve las contribuciones privadas aunque Ariel las tenga ocultas. El primer run del workflow tras la fusión lo reemplaza.

## 2026-10-28 — Workflow diario y README (GHP-PERFIL-3, etapa 2; propuesta del trabajador, aceptada por el orquestador)

- **Workflow** `.github/workflows/desfragmentador.yml`: `schedule` a las 06:17 UTC (fuera del minuto 0) y `workflow_dispatch`; `permissions` a nivel de workflow solo `contents: write`; `concurrency` `desfragmentador` sin cancelar el run en curso; el job solo corre en `refs/heads/main` (un `workflow_dispatch` desde otra rama no hace nada); `timeout-minutes: 5`.
- **Pasos:** `actions/checkout` fijado por SHA (`fbc6f3992d24b796d5a048ff273f7fcc4a7b6c09`, v5.1.0, leído con `git ls-remote`); `python3` del runner, sin `setup-python`; el generador con `GITHUB_TOKEN`; si `git diff --quiet` sobre el SVG no ve cambios, termina sin commit; si cambió, `git add` solo de `assets/ventana-desfragmentador.svg`, commit con autor `github-actions[bot]`, `git pull --rebase origin main` (por si `main` avanzó desde el checkout; si otro commit tocó el mismo SVG, el rebase falla y no se fuerza nada) y `git push origin HEAD:main`. Sin otros secretos. Si el generador falla, el job falla y no hay commit. Los logs de Actions son públicos: los errores del generador nombran el índice del día o el número de errores de GraphQL, nunca fechas, niveles ni el token.
- **Permisos leídos (GET, 2026-10-28):** `actions/permissions` → `enabled: true`, `allowed_actions: all`, `sha_pinning_required: false`; `actions/permissions/workflow` → `default_workflow_permissions: read`. El `contents: write` del workflow eleva ese permiso solo para este workflow; nada de lo leído lo impide. Protección de `main` (leída por el orquestador, 2026-10-28): `protected: false`, sin rulesets; el push directo del bot no está bloqueado (riesgo resuelto). Si Ariel agrega protección o reglas a `main`, el push del bot fallará y habrá que revisar el workflow.
- **README:** la ventana va debajo de las tres ventanas-enlace, sin enlace, con el alt aprobado y `width="830" height="312"` (la proporción del viewBox). El saneado de GitHub (`gh api markdown`) agrega `style="max-width: 100%; height: auto; max-height: 312px;"` cuando hay `height`, así que a 343 px no se deforma. GitHub envuelve toda imagen sin enlace en un `<a target="_blank">` a la propia imagen; eso es del renderizado de GitHub, no un enlace del README.
- **Riesgo: desactivación a los 60 días.** GitHub desactiva los workflows programados de un repo público sin actividad en 60 días. La ventana del calendario avanza a diario, así que habrá un commit del bot casi cada día; la documentación no dice si esos commits cuentan como «repository activity». Mitigación: si GitHub lo desactiva, Ariel lo reactiva en la pestaña Actions.
- **Riesgo: lectura del calendario con `GITHUB_TOKEN`.** No está verificado que el `GITHUB_TOKEN` de un workflow pueda leer `user(login:).contributionsCollection` por GraphQL; en local solo se probó con el token personal de `gh`. Modo de fallo seguro: si la consulta da error HTTP, errores de GraphQL o un calendario incompleto, el generador sale con código 1 sin escribir, el job falla y no hay commit (el SVG publicado queda como estaba). Verificación: primer run manual con `workflow_dispatch` tras la fusión, revisando el log y el commit del bot.
- **Riesgo: contribuciones privadas.** Con `GITHUB_TOKEN`, el calendario incluye las privadas solo como nivel y solo si Ariel tiene activado «Private contributions» en su perfil; la documentación no lo confirma de forma explícita para `GITHUB_TOKEN`. No se cambia ese ajuste. El SVG nunca muestra conteos ni fechas.
- **Riesgo: retrasos del schedule.** GitHub puede retrasar o saltarse runs con carga alta; un día sin run solo deja el mapa un día atrás.

## 2026-10-28 — Total de contribuciones en el desfragmentador (GHP-PERFIL-4; textos aprobados por Ariel)

- **Reemplaza** de GHP-PERFIL-3: la leyenda «Sin actividad · Poca · Mucha», la línea «Desfragmentando…» y «sin números».
- **Textos aprobados (exactos):** arriba de la rejilla «<N> contribuciones en el último año» (N = 1: «1 contribución en el último año»); abajo, junto a la barra, «Compilando ideas…». La barra de título, los colores de los bloques y la animación de la barra no cambian.
- **Dato:** la consulta GraphQL pide además `totalContributions`. El generador sale con código 1 sin escribir si falta o no es un entero ≥ 0 (un bool no cuenta). **Límite agregado:** ≤ 9 999 999, para que el número quepa en el viewBox; fuera de ese rango también sale con código 1. `--vacio` muestra «0 contribuciones…».
- **Formato:** número sin separador de miles, IBM Plex Mono 400 de 30 (igual que el resto), compuesto con un trazado por dígito (`D0`–`D9`, 18 unidades cada uno, fuente monoespaciada) y la frase como trazado (`CONTRIB_N` 576 = 32 × 18; `CONTRIB_1` 540 = 30 × 18; ambas con el espacio inicial). Se quitaron `SIN`, `POCA` y `MUCHA` de `scripts/desfragmentador_textos.json`; `ESTADO` pasó a «Compilando ideas…» (306 unidades).
- **Medidas** (viewBox sin cambios, 830 × 312, para no tocar el `height` del README): texto del total con base en y = 99, x = 28,5 (alineado con el marco de la rejilla); marco de la rejilla en y = 120 (antes 80), bloques desde y = 124 (antes 84); la franja de la leyenda (y 215–237) desaparece y la línea de estado queda donde estaba (barra en y = 266). Ancho del texto de arriba: 36 caracteres = 648 unidades con 1064 (hasta x = 676,5); con 9 999 999 mide 702 y termina en x = 730,5, dentro del marco (hasta x = 801,5). A 343 px el texto mide ≈ 12,4 px.
- **Hueco entre «Compilando ideas…» y la barra:** el texto termina en x = 334,5 y el marco de la barra empieza en 349,5: 15 unidades (≈ 6 px a 343 px). Revisado en captura a 375 px: legible y no se pega; no se ajustó.
- **Sin cambios:** el SVG no tiene `<title>`, `<desc>` ni `aria-label`, así que no hay dónde incluir el número; el alt del README no puede llevarlo (cambia a diario) y no se tocó. El SVG versionado no se modifica en esta rama: lo regenera el workflow tras la fusión.
- **Riesgo (igual que en GHP-PERFIL-3):** que el `GITHUB_TOKEN` del workflow vea un total distinto del que muestra el perfil. Se comprobará en el run manual tras la fusión.
