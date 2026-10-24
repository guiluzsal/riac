"""Carrega os catálogos YAML para o ambiente de macros do Zensical.

Expõe `recursos_da_categoria(categoria)` para as páginas em
docs/recursos/, e `itens_do_ecossistema(tipo)` para as páginas em
docs/ecossistema/, que renderizam os catálogos a partir do YAML em vez
de manterem markdown duplicado por item.
"""

from pathlib import Path

import yaml


def _carregar_yaml(env, nome_arquivo):
    data_path = Path(env.project_dir) / "data" / nome_arquivo
    with data_path.open(encoding="utf-8") as arquivo:
        return yaml.safe_load(arquivo) or []


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
