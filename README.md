# RIAC — Repositório de Inteligência de Ameaças Cibernéticas

O RIAC é uma plataforma colaborativa e aberta, em português, que reúne
recursos e verbetes sobre Cyber Threat Intelligence (CTI). O conteúdo é
mantido como código (docs-as-code) e recebe contribuições da comunidade via
GitHub.

> **Status:** projeto em estágio inicial de construção.

🔗 Site publicado: <https://guiluzsal.github.io/riac/>

## O que o RIAC oferece

- Catálogo de recursos curados de CTI, com descrição em português e
  metadados estruturados.
- Verbetes explicativos sobre conceitos, modelos e práticas de CTI.
- Glossário bilíngue EN↔PT com justificativa de tradução.
- Conteúdo dedicado ao contexto brasileiro (CERT.br, CTIR Gov, CAIS/RNP,
  legislação brasileira relevante).

Veja o escopo completo, as convenções de conteúdo e o roadmap em
[`CLAUDE.md`](CLAUDE.md).

## Como contribuir

Contribuições são bem-vindas via Pull Request. Veja
[`CONTRIBUTING.md`](CONTRIBUTING.md) para o fluxo de contribuição e
[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) para as regras de convivência.

## Desenvolvimento local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install zensical
zensical serve      # prévia local em http://localhost:8000
zensical build       # gera o site em site/
```

## Licenciamento

- Código: [MIT](LICENSE)
- Conteúdo (verbetes, catálogo, glossário): [CC BY-SA 4.0](LICENSE-CONTENT)
