 Cronograma de execução em estágios — RIAC

 Contexto

 O repositório /home/kiwi/Code/riac contém hoje apenas o arquivo CLAUDE.md — uma especificação completa e coesa do projeto RIAC (plataforma colaborativa em pt-BR sobre Cyber Threat Intelligence, site estático gerado com Zensical, hospedado no GitHub Pages). Não há git inicializado, nem nenhum outro arquivo, diretório, ambiente Python ou instalação do Zensical. O projeto está no estágio zero de implementação.

 O roadmap do próprio CLAUDE.md define a Fase 1 em termos de metas finais (repositório com Zensical, ~50 recursos, ~20 verbetes, glossário v1, Issue Forms, CI de qualidade, deploy no Pages), mas não em termos de ordem de execução nem de dependências reais entre essas entregas. O objetivo destecronograma é quebrar a Fase 1 em estágios sequenciáveis e verificáveis, identificando o que é trabalho de infraestrutura (sequencial, feito pormantenedores) versus produção de conteúdo (paralelizável, incremental, eventualmente comunitário), e deixar claro como isso se conecta às Fases 2 e 3.

 Este documento é o cronograma solicitado — uma referência de planejamento, não uma execução imediata de código. A execução real de cada estágio deve ser conduzida (e aprovada) estágio por estágio.

 Estágios

 Estágio 0 — Fundação do repositório

 - Entregas: git init + primeiro commit; README.md; LICENSE (MIT); LICENSE-CONTENT (CC BY-SA 4.0); CODE_OF_CONDUCT.md; CONTRIBUTING.md mínimo; .gitignore.
 - Dependências: nenhuma.
 - Tipo: infraestrutura/governança, sequencial, baixo esforço.
 - Pronto quando: histórico git existe, git status limpo, as duas licenças (código vs. conteúdo) estão presentes e distintas.

 Estágio 1 — Ambiente Zensical mínimo e primeiro build local

 - Entregas: .venv com zensical instalado (PEP 668 / Ubuntu 24.04); zensical.toml mínimo (nome, idioma pt-BR, nav inicial); docs/index.md stub; primeiro zensical build e zensical serve validados.
 - Dependências: Estágio 0.
 - Tipo: infraestrutura, sequencial — bloqueia CI e deploy.
 - Pronto quando: zensical build roda sem erro e zensical serve exibe a home em localhost:8000.
 - Nota: consultar a documentação oficial do Zensical antes de qualquer configuração além do mínimo (projeto novo, API muda rápido — regra do CLAUDE.md).

 Estágio 2 — Modelo de dados do catálogo (schema + seed)

 - Entregas: schemas/recursos.schema.json com todos os campos do modelo (nome, url, descricao, categoria com enum das 13 categorias, custo, requer_cadastro, idioma, fase_ciclo, nivel, tags, verificado_em); data/recursos.yaml com 3–5 entradas seed cobrindo categorias distintas; validação manual local contra o schema.
 - Dependências: Estágio 0.
 - Tipo: infraestrutura (schema) + conteúdo seed. Sequencial — trava que o próprio CLAUDE.md cita como exemplo (CI de schema não pode existir antes do schema).
 - Pronto quando: as entradas seed validam sem erro e pelo menos um caso ambíguo de categoria (ex.: VirusTotal) foi testado contra as regras de desambiguação do CLAUDE.md.

 Estágio 3 — Mecanismo de renderização do catálogo

 - Entregas: decisão documentada de como docs/recursos/ nasce de data/recursos.yaml (geração via script antes do build vs. mecanismo nativo do Zensical, se existir); docs/recursos/ com uma página por categoria, populada com o seed; nav do zensical.toml atualizado.
 - Dependências: Estágio 1 (build) + Estágio 2 (schema/seed).
 - Tipo: infraestrutura, decisão de arquitetura. A partir daqui a trilha de conteúdo do catálogo pode crescer em paralelo.
 - Pronto quando: adicionar uma entrada nova em data/recursos.yaml e rodar o mecanismo produz a página certa, sem edição manual de markdown.

 Estágio 4 — Template de verbete e verbetes piloto

 - Entregas: docs/verbetes/ com 2–3 verbetes piloto seguindo exatamente o template do CLAUDE.md (front matter tags, admonition de Origem, seções obrigatórias, kebab-case sem acento); nav atualizado; docs/glossario.md iniciado com os termos EN↔PT desses verbetes.
 - Dependências: Estágio 1. Independente dos Estágios 2/3, corre em paralelo.
 - Tipo: conteúdo (produção) + validação de que admonitions/abas do Zensical renderizam corretamente. A partir daqui a trilha de verbetes/glossário também corre em paralelo.
 - Pronto quando: os verbetes piloto compilam, cada um com ao menos uma referência verificável, seções na ordem do template.

 Estágio 5 — CI de qualidade (qualidade.yml)

 - Entregas: workflow com os 5 checks do CLAUDE.md — lychee (links), validação do YAML contra o schema, markdownlint (+ config), corretor ortográficopt-BR (cspell/Vale + dicionário de termos técnicos de CTI), zensical build como gate.
 - Dependências: Estágios 1, 2, 3 e 4 (precisa de build, schema e conteúdo real para calibrar os linters).
 - Tipo: infraestrutura, sequencial.
 - Pronto quando: um PR de teste com conteúdo novo passa nos 5 checks, e um PR de teste com erro deliberado (link morto, categoria inválida) falha no check certo.

 Estágio 6 — Deploy contínuo e GitHub Pages (docs.yml)

 - Entregas: workflow de build + deploy no merge para a branch principal; ativação do GitHub Pages; README.md atualizado com o link do site.
 - Dependências: Estágio 1 (build provado); idealmente Estágio 5 estável, mas pode avançar em paralelo ao fim dele.
 - Tipo: infraestrutura, sequencial — segundo exemplo citado explicitamente no CLAUDE.md.
 - Pronto quando: push na branch principal publica o site via Pages, refletindo o conteúdo atual.

 Estágio 7 — Fluxo de contribuição comunitária

 - Entregas: .github/ISSUE_TEMPLATE/ (Issue Forms para sugerir recurso/verbete, espelhando os campos do schema); .github/PULL_REQUEST_TEMPLATE.md; .github/CODEOWNERS; CONTRIBUTING.md expandido; docs/contribuir.md; botão "Editar esta página" se suportado pelo Zensical.
 - Dependências: Estágio 2 (schema para os campos do form), Estágio 5 (CI para o PR template referenciar os checks), Estágio 0 (CONTRIBUTING mínimo a expandir).
 - Tipo: infraestrutura/governança. Não bloqueia a trilha de conteúdo, que já roda desde os Estágios 3/4.
 - Pronto quando: uma Issue Form de teste gera uma issue bem formatada, um PR de teste é atribuído via CODEOWNERS, e a revisão de mantenedor é exigida no GitHub.

 Trilha contínua — Produção de conteúdo (checkpoints, não um estágio único)

 Começa no Estágio 3 (catálogo) e Estágio 4 (verbetes), corre em paralelo aos Estágios 5–7:

 ┌────────────┬──────────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
 │ Checkpoint │        Quando        │                                                Meta parcial                                                 │
 ├────────────┼──────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
 │ C1         │ durante Estágios 4–5 │ ~10 recursos em ≥8 categorias; 3–5 verbetes validados                                                       │
 ├────────────┼──────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
 │ C2         │ durante Estágios 6–7 │ ~25–30 recursos (todas as 13 categorias com ≥1 item); 10–12 verbetes; glossário com ~20 termos; primeiro    │
 │            │                      │ conteúdo lusófono (CERT.br, CTIR Gov, CAIS/RNP)                                                             │
 ├────────────┼──────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
 │ C3         │ fecha a Fase 1       │ ~50 recursos, ~20 verbetes, glossário v1, cobertura lusófona mínima (CERT.br, CTIR Gov, CAIS/RNP, CNCS,     │
 │            │ (Estágio 8)          │ CERT.PT, referência à LGPD/Marco Civil)                                                                     │
 └────────────┴──────────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

 Tipo: conteúdo, paralelizável/comunitário — cada item é um PR independente. Antes do Estágio 7, feito pelos mantenedores; depois, aberto à comunidade.

 Estágio 8 — Checkpoint de fechamento da Fase 1

 - Entregas: nenhuma nova — auditoria: contagem final de recursos/verbetes, CI verde, site publicado refletindo o estado atual, governança completa e coerente.
 - Dependências: todos os estágios anteriores + trilha de conteúdo em C3.
 - Tipo: verificação, não construção.
 - Pronto quando: todos os itens da Fase 1 do roadmap do CLAUDE.md estão marcados como concluídos e verificáveis publicamente.

 Conexão com Fases 2 e 3

 - Fase 2 (trilhas de aprendizado, templates operacionais, prévias de PR, co-mantenedores) reaproveita a infraestrutura da Fase 1: docs/templates/ pode nascer vazio já no Estágio 1 e ser populado só na Fase 2; trilhas de aprendizado são uma camada de navegação sobre o conteúdo já existente (via nivel/tags), sem novo modelo de dados; prévias de PR estendem o padrão de Actions do Estágio 6; co-mantenedores estendem o CODEOWNERS do Estágio 7.
 - Fase 3 (fichas de ameaças brasileiras, agregador RSS, API/JSON do catálogo) repete o padrão schema→template→CI da Fase 1 para um novo tipo deconteúdo (fichas); o agregador RSS é o primeiro componente genuinamente novo (workflow agendado); a API/JSON é a extensão mais barata, pois o Estágio 3 já resolve "YAML → saída derivada" — expor como JSON é outro alvo do mesmo mecanismo.

 Nenhum estágio interno de Fase 2/3 foi detalhado, por não fazer parte do pedido e por o próprio CLAUDE.md deixar isso para depois.

 Arquivos/áreas críticas referenciadas

 - /home/kiwi/Code/riac/CLAUDE.md (especificação-fonte de todas as regras usadas neste cronograma)
 - zensical.toml, docs/index.md (Estágio 1)
 - schemas/recursos.schema.json, data/recursos.yaml (Estágio 2)
 - docs/recursos/ (Estágio 3)
 - docs/verbetes/, docs/glossario.md (Estágio 4)
 - .github/workflows/qualidade.yml (Estágio 5)
 - .github/workflows/docs.yml (Estágio 6)
 - .github/ISSUE_TEMPLATE/, .github/PULL_REQUEST_TEMPLATE.md, .github/CODEOWNERS (Estágio 7)

 Verificação

 Cada estágio tem seu próprio critério de "pronto" (listado acima) e deve ser validado antes de avançar para o próximo:
 - Estágios 1, 3, 5, 6: validados rodando zensical build/zensical serve e observando o resultado (build sem erro, site renderizando as seções esperadas).
 - Estágio 2: validado rodando a validação do YAML contra o schema (localmente, antes de existir CI).
 - Estágio 5: validado com um PR de teste que deve passar e outro com erro proposital que deve falhar no check certo.
 - Estágio 6: validado checando se o site publicado no GitHub Pages reflete o commit mais recente.
 - Estágio 7: validado abrindo uma Issue Form de teste e um PR de teste para confirmar atribuição via CODEOWNERS.
 - Trilha de conteúdo: validada por contagem de entradas em data/recursos.yaml e arquivos em docs/verbetes/ contra as metas de cada checkpoint, todaspassando o CI do Estágio 5.