---
tags: [frameworks-e-modelos, defesa]
---

# MITRE D3FEND

**Definição:** grafo de conhecimento de contramedidas defensivas que
relaciona técnicas de defesa às táticas ofensivas que elas mitigam,
complementar ao MITRE ATT&CK.

!!! info "Origem"
    Desenvolvido pela MITRE com financiamento da Agência de Segurança
    Nacional dos EUA (NSA) e lançado publicamente em junho de 2021.

## Explicação

Enquanto o ATT&CK descreve o comportamento do adversário, o D3FEND
descreve o lado defensivo: cada contramedida é classificada em uma de
cinco táticas gerais — endurecer (*harden*), detectar, isolar, enganar e
remover (*evict*) — e conectada formalmente às técnicas ofensivas que
neutraliza. O grafo foi construído a partir de literatura técnica e de uma
amostra de mais de 500 patentes de contramedidas de segurança. A própria
MITRE descreve o lançamento inicial como não exaustivo.

## Exemplo prático

Um time de engenharia de detecção quer priorizar controles contra
movimentação lateral via RDP (técnica do ATT&CK). Consultando o D3FEND,
encontra contramedidas relacionadas, como segmentação de rede e
autenticação multifator, já conectadas formalmente à técnica ofensiva
correspondente.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O D3FEND é o par defensivo direto do [MITRE ATT&CK](mitre-attack.md): cada
técnica ofensiva do ATT&CK pode ser consultada no D3FEND para localizar as
contramedidas conhecidas.

## Termos relacionados

- [MITRE ATT&CK](mitre-attack.md)
- [MITRE ATLAS](mitre-atlas.md)

## Referências

- MITRE D3FEND™ Knowledge Graph. Disponível em: <https://d3fend.mitre.org/>
