# RIAC — Repositório de Inteligência de Ameaças Cibernéticas

Este arquivo orienta o Claude Code no desenvolvimento do RIAC. Leia-o inteiro antes de qualquer tarefa.

## Visão geral
O RIAC é uma plataforma colaborativa e aberta, em português, que reúne recursos e verbetes sobre Cyber Threat Intelligence (CTI). Ela recebe contribuições da comunidade via GitHub.

- Idioma do conteúdo, dos commits, das issues e dos comentários: **português do Brasil**.
- Público-alvo: analistas de CTI brasileiros de todos os níveis, com atenção especial a iniciantes.

## Escopo

### Dentro do escopo
- **Recursos:** links curados para ferramentas, bases e referências de CTI, com descrição em português e metadados.
- **Verbetes:** artigos explicativos sobre conceitos, modelos e práticas de CTI.
- **Glossário bilíngue EN↔PT:** cada termo traz a tradução recomendada e a justificativa.
- **Contexto brasileiro:**
  - CERT.br, CTIR Gov e CAIS/RNP;
  - legislação brasileira relevante;
  - ameaças que atingem o Brasil.
- **Templates operacionais em PT:** relatório de inteligência, RFI, PIRs e perfil de ator.
- **Trilhas de aprendizado** por nível (fase 2).
- **Fichas de ameaças brasileiras, agregador de notícias e API/JSON do catálogo** (fase 3).

### Fora do escopo
- Hospedar amostras de malware, IOCs sensíveis ou qualquer material que não seja TLP:CLEAR.
- Backend dinâmico, banco de dados ou área de login. O site é 100% estático.

## Stack
- **Fonte de verdade:** este repositório GitHub (docs-as-code).
- **Gerador de site:** [Zensical](https://zensical.org/docs/), com configuração em `zensical.toml`.
  - **Não use Material for MkDocs nem MkDocs.** O Material chega ao fim de vida em 05/11/2026 e o ecossistema MkDocs está instável.
  - Antes de alterar o `zensical.toml` ou adicionar plugins, consulte a documentação oficial do Zensical. O projeto é novo e muda rápido; não presuma compatibilidade com plugins MkDocs.
- **Hospedagem:** GitHub Pages, publicado via GitHub Actions (`.github/workflows/docs.yml`).
- **Contribuição:**
  - Pull Requests;
  - botão "Editar esta página";
  - Issue Forms para quem não usa Git.

## Estrutura do repositório
```
riac/
├── CLAUDE.md
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE                  # MIT (código)
├── LICENSE-CONTENT          # CC BY-SA 4.0 (conteúdo)
├── zensical.toml
├── overrides/
│   └── 404.html             # página 404 customizada (theme.custom_dir)
├── docs/
│   ├── index.md
│   ├── verbetes/            # um arquivo .md por verbete
│   ├── glossario.md
│   ├── recursos/            # páginas do catálogo por categoria
│   ├── templates/           # templates operacionais
│   └── contribuir.md
├── data/
│   └── recursos.yaml        # catálogo estruturado
├── schemas/
│   └── recursos.schema.json # schema de validação do YAML
└── .github/
    ├── workflows/
    │   ├── docs.yml         # build e deploy no Pages
    │   └── qualidade.yml    # lint, links, schema, ortografia
    ├── ISSUE_TEMPLATE/      # Issue Forms
    ├── PULL_REQUEST_TEMPLATE.md
    └── CODEOWNERS
```

## Comandos
Ambiente de referência: Ubuntu 24.04. Use sempre um ambiente virtual, porque o pip do sistema é bloqueado (PEP 668).

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install zensical
zensical serve      # prévia local em http://localhost:8000
zensical build      # gera o site em site/
```

## Convenções de conteúdo

### Template de verbete
Todo verbete em `docs/verbetes/` segue esta estrutura:

```markdown
---
tags: [categoria, subtema]
---

# Nome do Conceito (Nome em inglês, se houver)

**Definição:** uma ou duas frases objetivas.

!!! info "Origem"
    Autor(es), ano e contexto.

## Explicação
## Exemplo prático
## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)
## Termos relacionados
## Referências
```

- Nomes de arquivo em kebab-case e sem acento, por exemplo `diamond-model.md`.
- Todo verbete precisa ter ao menos uma referência verificável.
- Use admonitions (`!!! info`, `!!! tip`, `!!! warning`) e abas (`=== "..."`) com moderação.

### Modelo de dados do catálogo (`data/recursos.yaml`)
```yaml
- nome: Malpedia
  url: https://malpedia.caad.fkie.fraunhofer.de/
  descricao: Catálogo de famílias de malware com referências e regras YARA.
  categoria: malware
  idioma: [en]
  fase_ciclo: [coleta, processamento]
  tags: [yara, familias, atribuicao]
  verificado_em: 2026-10-22
```

Categorias válidas (use exatamente estes slugs no campo `categoria`):

| Slug | O que agrega | Exemplos |
|---|---|---|
| `varredura` | Mecanismos que varrem a internet e indexam serviços expostos: portas, banners, tecnologias e certificados por IP. Servem para mapear e pivotar infraestrutura de C2, servidores de phishing e ativos expostos, e para separar varredura em massa (ruído) de atividade direcionada. | Shodan, Censys, FOFA, ZoomEye, GreyNoise |
| `ip` | Titularidade, roteamento e contexto de endereços IP: WHOIS/RDAP dos registros regionais (RIRs), ASN, histórico de BGP, geolocalização e tipo de rede (residencial, datacenter, VPN/proxy). Servem para identificar o provedor por trás de um IP e pivotar por ASN, por exemplo para detectar bulletproof hosting. | bgp.he.net (Hurricane Electric), RIPEstat, IPinfo, Team Cymru IP-to-ASN, RDAP/WHOIS da LACNIC, ARIN e RIPE NCC, Registro.br |
| `dominio` | Fontes sobre domínios e sua história: WHOIS, DNS passivo, subdomínios e transparência de certificados (CT logs). Servem para descobrir infraestrutura relacionada a partir de um domínio e detectar domínios recém-registrados ou imitadores. | SecurityTrails, crt.sh, DNSDumpster, ViewDNS.info |
| `ioc` | Feeds e plataformas de Indicador de Comprometimento (IOC) multi-fonte, não organizados por família de malware: compartilhamento comunitário, agregação e correlação de IPs, domínios, URLs e hashes maliciosos. | AbuseIPDB, AlienVault OTX, Pulsedive, VirusTotal, Spamhaus |
| `malware` | Bases sobre famílias de malware (descrição técnica, capacidades, regras de detecção, amostras por link e IOCs públicos associados, organizados por família) e serviços que analisam um artefato específico — URL, arquivo ou hash — submetido pelo analista, devolvendo veredito, comportamento e capturas de tela. | Malpedia, MalwareBazaar, ThreatFox, URLhaus, urlscan.io, Hybrid Analysis, ANY.RUN, Joe Sandbox |
| `ator` | Bases sobre grupos de ameaça: perfis, aliases entre fornecedores, motivação, setores e países visados, TTPs e histórico de campanhas. Servem à atribuição e ao rastreamento de adversários. | MITRE ATT&CK Groups, ETDA Threat Group Cards, MISP Galaxy (threat actors) |
| `ransomware` | Bases e plataformas dedicadas a grupos e operações de ransomware: rastreamento de grupos, vítimas, sites de vazamento de dados (leak sites) e TTPs específicas dessas operações. | ransomware.live, Ransomwatch |
| `hacktivismo` | Bases e plataformas sobre grupos, campanhas e operações de hacktivismo: motivação ideológica ou política, alvos, DDoS e defacements atribuídos, canais próprios de divulgação. | — (sem recursos cadastrados ainda) |
| `vazamentos` | Monitoramento de vazamentos de dados e de atividade em fóruns e mercados da dark web: mapeamento de publicações, vazamentos de credenciais, ofertas de acesso e dados comprometidos, com atribuição a fórum, autor e data quando disponível. | Have I Been Pwned, analyzer.vecert.io |
| `vulnerabilidade` | Fontes para identificar, priorizar e acompanhar vulnerabilidades e sua exploração ativa. | NVD, CVE.org, CISA KEV, EPSS, Exploit-DB |
| `ferramenta` | Software que o analista instala ou opera: plataformas de inteligência (TIPs), gestão de casos, análise e detecção. | MISP, OpenCTI, TheHive/Cortex, CyberChef, Suricata, Zeek |
| `ecossistema` | Instituições, normas e fontes do Brasil: CSIRTs nacionais, órgãos de governo, legislação e políticas de cibersegurança. É o diferencial do RIAC. | CERT.br, CTIR Gov, CAIS/RNP, Política Nacional de Cibersegurança, LGPD, Marco Civil da Internet |

Regras de classificação:
- Cada recurso tem **uma** categoria principal. Use `tags` para aspectos secundários.
- Em caso de dúvida, classifique pelo **uso principal do recurso no trabalho de CTI**, não por quem o publica. Exemplo: a CISA KEV é publicada por um órgão de governo dos EUA, mas entra em `vulnerabilidade`, não em `ecossistema` (reservada a instituições, normas e políticas do Brasil).
- Recursos brasileiros que se encaixam claramente em outra categoria ficam nela, com a tag `brasil`. Exemplo: um feed de indicadores publicado por um CSIRT brasileiro iria para `ioc`. A categoria `ecossistema` é para instituições, normas e políticas do Brasil.
- **Categorias de infraestrutura** (`varredura`, `ip`, `dominio`): classifique pela **pergunta que o recurso responde melhor**.
  - "O que está rodando neste IP, ou ele é só ruído de varredura em massa?" → `varredura`.
  - "A quem pertence este IP e por onde ele é roteado?" → `ip`.
  - "Quem é dono deste domínio e o que mais está ligado a ele?" → `dominio`.
  - Plataformas multiuso (ex.: Censys) ficam na categoria do uso mais comum e recebem as demais como tags.
- **`malware` × `ioc`:** bases e feeds organizados por família de malware vão para `malware` (mesmo quando o conteúdo são IOCs, como ThreatFox e URLhaus); feeds e plataformas de IOC multi-fonte, não organizados por família, vão para `ioc` (AbuseIPDB, AlienVault OTX, Pulsedive, VirusTotal).
- **`malware` × `ator`:** classifique pelo eixo principal do recurso. Se ele é organizado por família de malware, use `malware`; se é organizado por grupo de ameaça, use `ator`. Bases que cobrem os dois igualmente ficam na categoria de maior uso e recebem a tag da outra.
- **`ator` × `ransomware`:** grupos cuja atividade principal é ransomware (extorsão por criptografia e/ou vazamento de dados) vão para `ransomware`; catálogos genéricos de grupos de ameaça, mesmo que incluam grupos de ransomware entre outros, ficam em `ator`.
- **`ator` × `hacktivismo`:** grupos cuja motivação principal é ideológica ou política (não financeira) vão para `hacktivismo`; os demais grupos de ameaça ficam em `ator`.
- **`ransomware` × `vazamentos`:** recursos focados em um grupo de ransomware específico (perfil, vítimas atribuídas, TTPs) vão para `ransomware`; recursos focados no vazamento ou no fórum/mercado em si, independente da origem, vão para `vazamentos`.
- **`ioc` × `vazamentos`:** feeds de IOC compartilhados pela comunidade (IPs, domínios, hashes) vão para `ioc`; monitoramento de vazamentos de dados, credenciais e atividade em fóruns da dark web vai para `vazamentos`.
- **Especificações, formatos e linguagens (ex.: STIX, YARA, Sigma) não entram no catálogo de recursos.** Elas ficam só nos verbetes (ex.: [YARA](docs/verbetes/yara.md), [Sigma](docs/verbetes/sigma.md), [STIX](docs/verbetes/stix.md)). Um recurso só vai para `ferramenta` se for algo que se instala ou executa — por exemplo, um scanner que executa regras YARA vai para `ferramenta`, mas a linguagem YARA em si não entra no catálogo.

Ao adicionar ou alterar campos, atualize também `schemas/recursos.schema.json`.

## Regras de conteúdo (obrigatórias)
- Sempre que um termo tiver entrada no [glossário](docs/glossario.md), use a forma em
  português no corpo do texto (verbetes, catálogo, templates), não o termo em inglês —
  um dos objetivos do RIAC é disseminar o uso desses termos em português. A sigla
  consolidada (ex.: APT, IOC, TTPs) pode acompanhar entre parênteses na primeira
  ocorrência, conforme o próprio glossário já faz. O termo em inglês continua a existir
  no glossário e pode aparecer citado quando necessário (ex.: nome oficial de um
  framework), mas não deve substituir a forma em português como escolha padrão de
  texto corrido.
- Só material **TLP:CLEAR**.
- Nunca hospedar amostras de malware; apenas apontar para repositórios que já fazem isso com controles.
- Citar fontes e respeitar licenças de terceiros. Exemplo: o MITRE ATT&CK pode ser reutilizado com atribuição.
- Não inventar dados, datas ou atribuições. Se não houver fonte, não inclua a afirmação.
- Licenças do projeto: CC BY-SA 4.0 para o conteúdo e MIT para o código.

## Qualidade e CI
O workflow `qualidade.yml` deve rodar em todo PR:
- `lychee`: verifica links quebrados;
- validação de `data/recursos.yaml` contra o schema;
- `markdownlint`;
- corretor ortográfico pt-BR (cspell ou Vale);
- `zensical build`: o site precisa compilar sem erros.

Antes de concluir qualquer tarefa, rode `zensical build` e as validações aplicáveis localmente.

## Governança
- Os arquivos `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CODEOWNERS` e o template de PR devem existir e estar atualizados.
- Todo PR de conteúdo precisa da revisão de pelo menos um mantenedor.
- Prévias de PR são desejáveis (fase 2).

## Roadmap
- **Fase 1:**
  - repositório com Zensical;
  - cerca de 50 recursos e 20 verbetes;
  - glossário v1;
  - Issue Forms e CI de qualidade;
  - deploy no Pages.
- **Fase 2:**
  - trilhas de aprendizado;
  - templates operacionais;
  - prévias de PR;
  - entrada de co-mantenedores.
- **Fase 3:**
  - fichas de ameaças brasileiras;
  - agregador de notícias (RSS);
  - API/JSON do catálogo.