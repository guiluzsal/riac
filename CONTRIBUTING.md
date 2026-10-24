# Como contribuir

O RIAC é um projeto colaborativo e aberto. Contribuições de verbetes, recursos
do catálogo, correções e melhorias são bem-vindas via Pull Request ou, para
quem não usa Git, via formulário de issue.

## Antes de contribuir

Leia o [`CLAUDE.md`](CLAUDE.md) na raiz do repositório. Ele define o escopo
do projeto, as convenções de conteúdo (template de verbete, modelo de dados
do catálogo em `data/recursos.yaml` e do ecossistema em
`data/ecossistema.yaml`, categorias e tipos válidos) e as regras
obrigatórias de conteúdo (apenas material TLP:CLEAR, não inventar dados,
citar fontes).

## Sem usar Git

Use um dos formulários de issue:

- **[Sugerir um recurso](https://github.com/guiluzsal/riac/issues/new?template=sugerir-recurso.yml)** —
  os campos espelham `schemas/recursos.schema.json`.
- **[Sugerir um verbete](https://github.com/guiluzsal/riac/issues/new?template=sugerir-verbete.yml)** —
  para propor um conceito, modelo ou prática de CTI.
- **[Sugerir item do ecossistema](https://github.com/guiluzsal/riac/issues/new?template=sugerir-ecossistema.yml)** —
  os campos espelham `schemas/ecossistema.schema.json`.

Ou clique no ícone de lápis (✎) em qualquer página do
[site publicado](https://guiluzsal.github.io/riac/) para editá-la
diretamente no GitHub, o que já abre um Pull Request.

## Ambiente de desenvolvimento

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install zensical
zensical serve      # prévia local em http://localhost:8000
zensical build       # gera o site em site/
```

## Como os recursos e o ecossistema são gerados

As páginas em `docs/recursos/*.md` e `docs/ecossistema/*.md` **não listam
os itens manualmente**. Cada página chama uma macro — `recursos_da_categoria("<categoria>")`
para `docs/recursos/` ou `itens_do_ecossistema("<tipo>")` para
`docs/ecossistema/` (ambas definidas em `main.py`) — que lê, respectivamente,
`data/recursos.yaml` ou `data/ecossistema.yaml` em tempo de build e
renderiza os itens correspondentes. Isso usa a extensão nativa de macros do
Zensical (`[project.plugins.macros]` em `zensical.toml`), compatível com a
API do `mkdocs-macros-plugin`.

Na prática, isso significa que **para adicionar um item basta editar o YAML
correspondente** — a página é atualizada automaticamente no próximo
`zensical build`, sem precisar tocar em nenhum arquivo `.md` de
`docs/recursos/` ou `docs/ecossistema/`.

> **Atenção:** o Zensical não rastreia esses arquivos YAML como
> dependência das páginas que o `main.py` lê — só o conteúdo `.md` em si.
> Depois de editar um catálogo, rode `zensical build --clean` (não só
> `zensical build`) ou reinicie o `zensical serve`, senão o build
> incremental pode continuar mostrando o estado antigo da página.

## Como propor um recurso (via Pull Request)

1. Edite `data/recursos.yaml` seguindo o modelo de dados do `CLAUDE.md`.
2. Escolha **uma única categoria principal**, pelo uso mais comum do
   recurso em CTI (não por quem o publica). Use `tags` para aspectos
   secundários — por exemplo, uma plataforma multiuso como o VirusTotal
   fica na categoria do uso mais frequente e recebe as demais como tags.
   As regras completas de desambiguação entre categorias estão no
   `CLAUDE.md`.
3. Valide localmente:

   ```bash
   pip install check-jsonschema
   check-jsonschema --schemafile schemas/recursos.schema.json data/recursos.yaml
   ```

## Como propor um item do ecossistema

1. Edite `data/ecossistema.yaml` seguindo o modelo de dados do `CLAUDE.md`.
2. Escolha o `tipo` correto: `instituicao` (CSIRTs, órgãos de governo e
   demais entidades) ou `legislacao` (leis, decretos, políticas).
3. Valide localmente:

   ```bash
   pip install check-jsonschema
   check-jsonschema --schemafile schemas/ecossistema.schema.json data/ecossistema.yaml
   ```

## Como propor um verbete

1. Crie o arquivo em `docs/verbetes/` com nome em kebab-case e sem acento
   (ex.: `diamond-model.md`), seguindo exatamente o template definido no
   `CLAUDE.md` (front matter `tags`, admonition `!!! info "Origem"`,
   seções Definição, Explicação, Exemplo prático, Relação com outros
   modelos, Termos relacionados, Referências).
2. Inclua ao menos **uma referência verificável** — um verbete sem fonte
   checável não pode ser publicado.
3. Adicione o verbete à `nav` em `zensical.toml` e, se usar termos novos
   em inglês, inclua-os em `docs/glossario.md` com a tradução recomendada
   e a justificativa.

## Regras de conteúdo obrigatórias

- Só material **TLP:CLEAR**.
- Nunca hospede amostras de malware ou IOCs sensíveis; aponte para
  repositórios que já fazem isso com os controles adequados.
- Cite fontes e respeite licenças de terceiros.
- Não invente dados, datas ou atribuições. Sem fonte, sem afirmação.

## Rodando o CI de qualidade localmente

O workflow `qualidade.yml` roda em todo Pull Request. Para checar antes de
abrir o PR:

```bash
# build do site
zensical build

# schema do catálogo e do ecossistema
pip install check-jsonschema
check-jsonschema --schemafile schemas/recursos.schema.json data/recursos.yaml
check-jsonschema --schemafile schemas/ecossistema.schema.json data/ecossistema.yaml

# markdownlint e ortografia (requerem Node.js)
npm install
npx markdownlint-cli2
npx cspell "**/*.md"
```

Se o cspell acusar uma palavra correta como desconhecida (sigla, nome
próprio, termo técnico de CTI), adicione-a à lista `words` em
`cspell.json` em vez de reescrever o texto.

## Fluxo de contribuição (Pull Request)

1. Faça um fork ou crie uma branch a partir de `main`.
2. Adicione ou edite o conteúdo seguindo as convenções do `CLAUDE.md`.
3. Rode os checks da seção anterior localmente.
4. Abra um Pull Request — o template guia o checklist.
5. Todo PR de conteúdo precisa da revisão de pelo menos um mantenedor
   (ver [`CODEOWNERS`](.github/CODEOWNERS)) antes de ser mesclado.

## Licenciamento das contribuições

Ao contribuir, você concorda que:

- Alterações de código são licenciadas sob a licença MIT ([`LICENSE`](LICENSE));
- Alterações de conteúdo (verbetes, catálogo, glossário) são licenciadas sob
  CC BY-SA 4.0 ([`LICENSE-CONTENT`](LICENSE-CONTENT)).

## Código de conduta

Ao participar deste projeto, você concorda em seguir o nosso
[Código de Conduta](CODE_OF_CONDUCT.md).
