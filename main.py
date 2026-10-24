"""Carrega os catálogos YAML para o ambiente de macros do Zensical.

Expõe `recursos_da_categoria(categoria)` para as páginas em
docs/recursos/, `itens_do_ecossistema(tipo)` para as páginas em
docs/ecossistema/, e `ficha_legislacao(page)` para as páginas em
docs/ecossistema/legislacao/, que renderizam os catálogos e os
metadados de frontmatter em vez de manterem markdown duplicado por
item.
"""

from datetime import date
from pathlib import Path

import yaml

_MESES = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro",
}

_TIPOS_NORMA = {
    "lei": "Lei",
    "decreto": "Decreto",
    "medida_provisoria": "Medida Provisória",
    "portaria": "Portaria",
    "instrucao_normativa": "Instrução Normativa",
    "resolucao": "Resolução",
    "projeto_de_lei": "Projeto de Lei",
}

_SITUACOES = {
    "vigente": "Vigente",
    "revogada": "Revogada",
    "alterada": "Alterada",
}


def _carregar_yaml(env, nome_arquivo):
    data_path = Path(env.project_dir) / "data" / nome_arquivo
    with data_path.open(encoding="utf-8") as arquivo:
        return yaml.safe_load(arquivo) or []


def _formatar_data_pt(valor):
    if isinstance(valor, str):
        valor = date.fromisoformat(valor)
    return f"{valor.day} de {_MESES[valor.month]} de {valor.year}"


def _renderizar_cartoes(itens, vazio):
    if not itens:
        return vazio
    cartoes = []
    for item in itens:
        bloco = (
            f"-   ## [{item['nome']}]({item['url']}) {{: .catalogo-card__titulo }}\n\n"
            f"    {item['descricao']}\n"
            f"    {{: .catalogo-card__descricao }}"
        )
        tags = item.get("tags", [])
        if tags:
            chips = " ".join(
                f'<span class="catalogo-card__tag">{t}</span>' for t in tags
            )
            bloco += f"\n\n    {chips}\n    {{: .catalogo-card__tags }}"
        cartoes.append(bloco)
    corpo = "\n\n".join(cartoes)
    return f'<div class="grid cards" markdown>\n\n{corpo}\n\n</div>'


def define_env(env):
    recursos = _carregar_yaml(env, "recursos.yaml")
    ecossistema = _carregar_yaml(env, "ecossistema.yaml")
    env.variables["recursos"] = recursos
    env.variables["ecossistema"] = ecossistema

    @env.macro
    def recursos_da_categoria(categoria):
        itens = sorted(
            (r for r in recursos if r.get("categoria") == categoria),
            key=lambda r: r["nome"].lower(),
        )
        return _renderizar_cartoes(
            itens, "_Nenhum recurso cadastrado nesta categoria ainda._"
        )

    @env.macro
    def itens_do_ecossistema(tipo):
        itens = sorted(
            (e for e in ecossistema if e.get("tipo") == tipo),
            key=lambda e: e["nome"].lower(),
        )
        return _renderizar_cartoes(
            itens, "_Nenhum item cadastrado nesta seção ainda._"
        )

    @env.macro
    def ficha_legislacao(page):
        meta = page.meta
        linhas = []

        descricao = meta.get("descricao")
        if descricao:
            linhas.append(f"**Descrição:** {descricao}")

        tipo_norma = meta.get("tipo_norma")
        numero = meta.get("numero")
        if tipo_norma or numero:
            rotulo = _TIPOS_NORMA.get(tipo_norma, tipo_norma)
            identificacao = " ".join(
                parte for parte in [rotulo, f"nº {numero}" if numero else None]
                if parte
            )
            linhas.append(f"**Norma:** {identificacao}")

        data_assinatura = meta.get("data_assinatura")
        if data_assinatura:
            linhas.append(f"**Assinatura:** {_formatar_data_pt(data_assinatura)}")

        data_publicacao = meta.get("data_publicacao")
        if data_publicacao:
            linhas.append(
                f"**Publicação (DOU):** {_formatar_data_pt(data_publicacao)}"
            )

        orgao = meta.get("orgao")
        if orgao:
            linhas.append(f"**Órgão responsável:** {orgao}")

        situacao = meta.get("situacao")
        if situacao:
            linhas.append(f"**Situação:** {_SITUACOES.get(situacao, situacao)}")

        fonte_oficial = meta.get("fonte_oficial")
        if fonte_oficial:
            linhas.append(
                f"**Fonte oficial:** [{fonte_oficial['nome']}]({fonte_oficial['url']})"
            )

        if not linhas:
            return ""

        corpo = "\n\n    ".join(linhas)
        return f'!!! info "Sobre esta norma"\n    {corpo}'
