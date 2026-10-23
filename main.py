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
        blocos = []
        for r in itens:
            tags = ", ".join(r.get("tags", [])) or "—"
            blocos.append(
                f"## [{r['nome']}]({r['url']})\n\n"
                f"{r['descricao']}\n\n"
                f"- **Custo:** {r['custo']}\n"
                f"- **Requer cadastro:** {r['requer_cadastro']}\n"
                f"- **Nível:** {r['nivel']}\n"
                f"- **Tags:** {tags}"
            )
        return "\n\n".join(blocos)
