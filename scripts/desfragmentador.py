"""Genera assets/ventana-desfragmentador.svg con la actividad del último año en GitHub.

Solo biblioteca estándar de Python 3. Uso:
  python scripts/desfragmentador.py            # consulta GraphQL con GITHUB_TOKEN (o GH_TOKEN)
  python scripts/desfragmentador.py --vacio    # calendario sin actividad, sin red
  python scripts/desfragmentador.py --entrada respuesta.json --salida tmp/x.svg

Si la consulta falla o la respuesta no trae un año de días, sale con código 1
y no escribe el SVG. Misma entrada → mismos bytes.
"""
import argparse
import datetime
import json
import os
import sys
import urllib.error
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALIDA = os.path.join(RAIZ, "assets", "ventana-desfragmentador.svg")
TEXTOS = os.path.join(RAIZ, "scripts", "desfragmentador_textos.json")

MARFIL = "#f1ece8"
CARBON = "#242625"
AZUL = "#2563eb"
NARANJA = "#b9370a"

# contributionLevel → color: sin actividad, poca, mucha.
NIVELES = {
    "NONE": MARFIL,
    "FIRST_QUARTILE": AZUL,
    "SECOND_QUARTILE": AZUL,
    "THIRD_QUARTILE": NARANJA,
    "FOURTH_QUARTILE": NARANJA,
}

CONSULTA = """query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks { contributionDays { date weekday contributionLevel } }
      }
    }
  }
}"""

# Medidas del viewBox (830 de ancho, se muestra a ≈ 343–830 px).
ANCHO, ALTO = 830, 312
BARRA = 54
SEMANAS = 53
PASO, BLOQUE = 14.5, 11
REJILLA_X, REJILLA_Y = 32.5, 84
SEGMENTOS, SEG_PASO, SEG_ANCHO = 16, 28, 24
SEG_X, SEG_Y, SEG_ALTO = 353.5, 266, 16


class ErrorDatos(Exception):
    pass


def num(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


def consultar(usuario, token):
    cuerpo = json.dumps({"query": CONSULTA, "variables": {"login": usuario}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=cuerpo,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "mrKanoh-desfragmentador",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except (urllib.error.URLError, ValueError) as e:
        raise ErrorDatos(f"consulta fallida: {e}") from None


def semanas_de(respuesta):
    """Valida la respuesta y devuelve las semanas como listas de (weekday, nivel)."""
    if respuesta.get("errors"):
        raise ErrorDatos(f"GraphQL devolvió errores: {respuesta['errors']}")
    try:
        semanas = respuesta["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
        dias = [d for s in semanas for d in s["contributionDays"]]
    except (KeyError, TypeError):
        raise ErrorDatos("respuesta sin calendario") from None
    # El calendario trae un año completado hasta el domingo inicial: 365–371 días.
    if not 364 <= len(dias) <= 371:
        raise ErrorDatos(f"se esperaban ≈ 365 días y llegaron {len(dias)}")
    anterior = None
    for d in dias:
        if d.get("contributionLevel") not in NIVELES or d.get("weekday") not in range(7):
            raise ErrorDatos(f"día inválido: {d}")
        fecha = datetime.date.fromisoformat(d["date"])
        if fecha.weekday() != (d["weekday"] - 1) % 7:
            raise ErrorDatos(f"weekday no coincide con la fecha: {d}")
        if anterior and fecha - anterior != datetime.timedelta(days=1):
            raise ErrorDatos(f"días no consecutivos: {anterior} → {fecha}")
        anterior = fecha
    return [[(d["weekday"], d["contributionLevel"]) for d in s["contributionDays"]] for s in semanas]


def semanas_vacias():
    return [[(w, "NONE") for w in range(7)] for _ in range(SEMANAS)]


def texto(textos, nombre, x, base, color):
    return f'<path transform="translate({num(x)} {num(base)})" d="{textos[nombre]["d"]}" fill="{color}"/>'


def svg(semanas, textos):
    # Últimas 53 columnas, como el calendario; el carbón queda donde no hay día.
    bloques = {color: [] for color in (MARFIL, AZUL, NARANJA)}
    for col, semana in enumerate(semanas[-SEMANAS:]):
        x = REJILLA_X + col * PASO
        for weekday, nivel in semana:
            y = REJILLA_Y + weekday * PASO
            bloques[NIVELES[nivel]].append(f"M{num(x)} {num(y)}h{BLOQUE}v{BLOQUE}h-{BLOQUE}z")
    rejilla_ancho = SEMANAS * PASO - (PASO - BLOQUE)
    rejilla_alto = 7 * PASO - (PASO - BLOQUE)

    # Leyenda: muestra carbón con el bloque dentro, y su texto.
    leyenda, x = [], REJILLA_X - 4
    for color, nombre in ((MARFIL, "SIN"), (AZUL, "POCA"), (NARANJA, "MUCHA")):
        leyenda.append(f'<rect x="{num(x)}" y="215" width="22" height="22" fill="{CARBON}"/>')
        leyenda.append(f'<rect x="{num(x + 4)}" y="219" width="14" height="14" fill="{color}"/>')
        leyenda.append(texto(textos, nombre, x + 32, 236.5, CARBON))
        x += 32 + textos[nombre]["ancho"] + 36

    seg_total = SEGMENTOS * SEG_PASO
    llenos = "".join(
        f"M{num(SEG_X + i * SEG_PASO)} {SEG_Y}h{SEG_ANCHO}v{SEG_ALTO}h-{SEG_ANCHO}z" for i in range(SEGMENTOS)
    )
    vacios = "".join(
        f"M{num(i * SEG_PASO)} 0h{SEG_ANCHO}v{SEG_ALTO}h-{SEG_ANCHO}z" for i in range(SEGMENTOS)
    )

    partes = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" height="{ALTO}" role="img">',
        "<style>",
        f".cubre{{animation:llenar 9s infinite}}",
        f"@keyframes llenar{{0%{{transform:translateX(0);animation-timing-function:steps({SEGMENTOS},end)}}"
        f"80%,100%{{transform:translateX({seg_total}px)}}}}",
        f"@media (prefers-reduced-motion:reduce){{.cubre{{animation:none;transform:translateX({seg_total // 2}px)}}}}",
        "</style>",
        f'<defs><clipPath id="barra"><rect x="{num(SEG_X)}" y="{SEG_Y}" width="{seg_total - (SEG_PASO - SEG_ANCHO)}" height="{SEG_ALTO}"/></clipPath></defs>',
        f'<rect x="1" y="1" width="{ANCHO - 2}" height="{ALTO - 2}" fill="{MARFIL}" stroke="{CARBON}" stroke-width="2"/>',
        f'<rect x="2" y="2" width="{ANCHO - 4}" height="{BARRA - 2}" fill="{CARBON}"/>',
        texto(textos, "BARRA", 24, 38.5, MARFIL),
        f'<rect x="{num(REJILLA_X - 4)}" y="{REJILLA_Y - 4}" width="{num(rejilla_ancho + 8)}" height="{num(rejilla_alto + 8)}" fill="{CARBON}"/>',
    ]
    for color, ds in bloques.items():
        if ds:
            partes.append(f'<path d="{"".join(ds)}" fill="{color}"/>')
    partes += leyenda
    partes += [
        texto(textos, "ESTADO", REJILLA_X - 4, 284.5, CARBON),
        f'<rect x="{num(SEG_X - 4)}" y="{SEG_Y - 4}" width="{seg_total - (SEG_PASO - SEG_ANCHO) + 8}" height="{SEG_ALTO + 8}" fill="{CARBON}"/>',
        f'<path d="{llenos}" fill="{AZUL}"/>',
        f'<g clip-path="url(#barra)"><g transform="translate({num(SEG_X)} {SEG_Y})">'
        f'<g class="cubre"><path d="{vacios}" fill="{MARFIL}"/></g></g></g>',
        "</svg>",
    ]
    return "\n".join(partes) + "\n"


def main():
    p = argparse.ArgumentParser(description="Genera la ventana del desfragmentador.")
    p.add_argument("--usuario", default="mrKanoh")
    p.add_argument("--salida", default=SALIDA)
    origen = p.add_mutually_exclusive_group()
    origen.add_argument("--entrada", help="respuesta GraphQL guardada (JSON) en vez de consultar")
    origen.add_argument("--vacio", action="store_true", help="calendario sin actividad, sin red")
    args = p.parse_args()

    with open(TEXTOS, encoding="utf-8") as f:
        textos = json.load(f)
    try:
        if args.vacio:
            semanas = semanas_vacias()
        else:
            if args.entrada:
                with open(args.entrada, encoding="utf-8") as f:
                    respuesta = json.load(f)
            else:
                token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
                if not token:
                    raise ErrorDatos("falta GITHUB_TOKEN o GH_TOKEN")
                respuesta = consultar(args.usuario, token)
            semanas = semanas_de(respuesta)
    except ErrorDatos as e:
        print(f"desfragmentador: {e}; no se escribe el SVG", file=sys.stderr)
        return 1

    contenido = svg(semanas, textos)
    temporal = args.salida + ".tmp"
    with open(temporal, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenido)
    os.replace(temporal, args.salida)
    return 0


if __name__ == "__main__":
    sys.exit(main())
