# Como contribuir

O RIAC é um projeto colaborativo e aberto. Contribuições de verbetes, recursos
do catálogo, correções e melhorias são bem-vindas via Pull Request.

> Este guia está em construção. Ele será expandido com instruções detalhadas
> sobre Issue Forms, template de Pull Request e regras de revisão assim que
> esses mecanismos estiverem configurados no repositório.

## Antes de contribuir

Leia o [`CLAUDE.md`](CLAUDE.md) na raiz do repositório. Ele define o escopo
do projeto, as convenções de conteúdo (template de verbete, modelo de dados
do catálogo em `data/recursos.yaml`, categorias válidas) e as regras
obrigatórias de conteúdo (apenas material TLP:CLEAR, não inventar dados,
citar fontes).

## Ambiente de desenvolvimento

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install zensical
zensical serve      # prévia local em http://localhost:8000
zensical build       # gera o site em site/
```

## Fluxo de contribuição

1. Faça um fork ou crie uma branch a partir de `main`.
2. Adicione ou edite o conteúdo seguindo as convenções do `CLAUDE.md`.
3. Rode `zensical build` localmente para confirmar que o site compila sem
   erros.
4. Abra um Pull Request descrevendo a mudança.
5. Todo PR de conteúdo precisa da revisão de pelo menos um mantenedor antes
   de ser mesclado.

## Licenciamento das contribuições

Ao contribuir, você concorda que:

- Alterações de código são licenciadas sob a licença MIT ([`LICENSE`](LICENSE));
- Alterações de conteúdo (verbetes, catálogo, glossário) são licenciadas sob
  CC BY-SA 4.0 ([`LICENSE-CONTENT`](LICENSE-CONTENT)).

## Código de conduta

Ao participar deste projeto, você concorda em seguir o nosso
[Código de Conduta](CODE_OF_CONDUCT.md).
