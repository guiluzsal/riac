---
tags: [frameworks-e-modelos, analise-de-intrusao]
---

# Cadeia de Ataque Cibernética (Cyber Kill Chain)

**Definição:** modelo que descreve uma intrusão como uma sequência de sete
fases, do reconhecimento até a ação sobre os objetivos, permitindo que
defensores identifiquem e interrompam o ataque em qualquer etapa da
cadeia.

!!! info "Origem"
    Proposto por Eric M. Hutchins, Michael J. Cloppert e Rohan M. Amin,
    pesquisadores da Lockheed Martin, em 2011, no artigo
    "Intelligence-Driven Computer Network Defense Informed by Analysis of
    Adversary Campaigns and Intrusion Kill Chains".

## Explicação

O modelo define sete fases sequenciais de uma intrusão:

1. **Reconhecimento** (*Reconnaissance*) — pesquisa e seleção de alvos.
2. **Armamento** (*Weaponization*) — criação de um artefato malicioso
   (ex.: exploit + backdoor).
3. **Entrega** (*Delivery*) — transmissão do artefato ao alvo (ex.:
   e-mail, mídia removível).
4. **Exploração** (*Exploitation*) — execução do código malicioso na
   vítima.
5. **Instalação** (*Installation*) — instalação de um backdoor
   persistente.
6. **Comando e controle** (*Command & Control*, C2) — canal remoto para
   controlar o implante.
7. **Ações sobre os objetivos** (*Actions on Objectives*) — o adversário
   atinge seu objetivo final (ex.: exfiltração de dados).

A premissa central do modelo é que o adversário precisa completar todas as
fases com sucesso, enquanto o defensor só precisa interromper uma delas
para frustrar o ataque.

## Exemplo prático

Em uma campanha de ransomware, o adversário envia um e-mail de phishing
com um documento malicioso (entrega), que ao ser aberto executa uma macro
(exploração) e instala um implante (instalação) que se comunica com um
servidor de C2. A partir daí, o adversário se move lateralmente e, por
fim, implanta o ransomware (ações sobre os objetivos). Um defensor que
bloqueia o e-mail na fase de entrega interrompe toda a cadeia.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O MITRE ATT&CK pode ser visto como um detalhamento das táticas e técnicas
que ocorrem dentro de cada fase da Kill Chain, com granularidade muito
maior. O [Modelo Diamante](diamond-model.md) complementa a Kill Chain ao
modelar, para cada fase, o adversário, a infraestrutura, a capacidade e a
vítima envolvidos.

## Termos relacionados

- [Modelo Diamante (Diamond Model)](diamond-model.md)
- [Pirâmide da Dor (Pyramid of Pain)](pyramid-of-pain.md)
- MITRE ATT&CK

## Referências

- Hutchins, E. M., Cloppert, M. J., & Amin, R. M. (2011).
  *Intelligence-Driven Computer Network Defense Informed by Analysis of
  Adversary Campaigns and Intrusion Kill Chains*. Lockheed Martin
  Corporation. Disponível em:
  <https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf>
