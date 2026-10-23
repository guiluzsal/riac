"""Carrega data/recursos.yaml para o ambiente de macros do Zensical.

Expõe `recursos_da_categoria(categoria)` para as páginas em
docs/recursos/, que renderizam o catálogo a partir do YAML em vez de
manterem markdown duplicado por recurso.
"""

from pathlib import Path

import yaml


def define_env(env):
    data_path = Path(env.project_dir) / "data" / "recursos.yaml"
    with data_path.open(encoding="utf-8") as arquivo:
        recursos = yaml.safe_load(arquivo) or []
    env.variables["recursos"] = recursos

    @env.macro
    def recursos_da_categoria(categoria):
        itens = sorted(
            (r for r in recursos if r.get("categoria") == categoria),
            key=lambda r: r["nome"].lower(),
        )
        if not itens:
            return "_Nenhum recurso cadastrado nesta categoria ainda._"
        cartoes = []
        for r in itens:
            bloco = (
                f"-   ## [{r['nome']}]({r['url']}) {{: .catalogo-card__titulo }}\n\n"
                f"    {r['descricao']}\n"
                f"    {{: .catalogo-card__descricao }}"
            )
            tags = r.get("tags", [])
            if tags:
                chips = " ".join(
                    f'<span class="catalogo-card__tag">{t}</span>' for t in tags
                )
                bloco += f"\n\n    {chips}\n    {{: .catalogo-card__tags }}"
            cartoes.append(bloco)
        corpo = "\n\n".join(cartoes)
        return f'<div class="grid cards" markdown>\n\n{corpo}\n\n</div>'
