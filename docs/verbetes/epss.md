---
tags: [vulnerabilidades, priorizacao]
---

# EPSS (Exploit Prediction Scoring System)

**Definição:** modelo que estima, em uma escala de 0 a 1, a probabilidade
de uma vulnerabilidade divulgada ser explorada ativamente nos próximos
30 dias, usado para priorizar a correção de vulnerabilidades.

!!! info "Origem"
    Desenvolvido por um Special Interest Group (SIG) formado no FIRST
    (Forum of Incident Response and Security Teams) no início de 2020,
    liderado por Jay Jacobs; os primeiros escores públicos do modelo foram
    publicados em janeiro de 2021.

## Explicação

Diferente do CVSS, que mede a *severidade* potencial de uma
vulnerabilidade (o dano que causaria se explorada), o EPSS mede a
*probabilidade* de exploração de fato acontecer no curto prazo, com base
em dados históricos de exploração observada. Os dois escores são
complementares: uma vulnerabilidade pode ter CVSS alto e EPSS baixo (grave
em teoria, mas raramente explorada), ou o contrário.

## Exemplo prático

Um time de gestão de vulnerabilidades tem centenas de CVEs de severidade
"alta" (CVSS) em aberto e não consegue corrigir todas de uma vez. Ao
cruzar a lista com os escores de EPSS, prioriza primeiro as
vulnerabilidades com maior probabilidade de exploração iminente,
concentrando o esforço onde o risco real é mais alto.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O EPSS é usado em conjunto com o Catálogo de Vulnerabilidades
Conhecidamente Exploradas (KEV) da CISA, que confirma retroativamente
quais vulnerabilidades já foram exploradas na prática.

## Termos relacionados

- (nenhum verbete relacionado ainda)

## Referências

- FIRST EPSS Special Interest Group. *Exploit Prediction Scoring System
  (EPSS)*. Disponível em: <https://www.first.org/epss/>
