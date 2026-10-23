---
tags: [frameworks-e-modelos, resposta-a-incidentes]
---

# Courses of Action Matrix

**Definição:** matriz que cruza as fases da Cadeia de Ataque Cibernética
com seis ações defensivas possíveis (detectar, negar, interromper,
degradar, enganar e destruir), ajudando a planejar como responder a cada
fase de uma intrusão.

!!! info "Origem"
    Proposta por Eric M. Hutchins, Michael J. Cloppert e Rohan M. Amin, no
    mesmo artigo de 2011 da Lockheed Martin que introduziu a
    [Cadeia de Ataque Cibernética](cyber-kill-chain.md).

## Explicação

Para cada uma das sete fases da Kill Chain (reconhecimento, armamento,
entrega, exploração, instalação, comando e controle, ações sobre os
objetivos), a matriz lista as seis ações defensivas possíveis, formando
uma grade de 7×6 opções. Nem toda célula é aplicável a todo incidente,
mas a matriz ajuda equipes a mapear sistematicamente onde já existem
controles e onde há lacunas de cobertura ao longo das fases do ataque.

## Exemplo prático

Um time de segurança mapeia seus controles existentes contra a matriz e
percebe que tem boa cobertura de detecção na fase de entrega (filtro de
e-mail) e de interrupção na fase de instalação (EDR), mas nenhuma ação
definida para a fase de comando e controle — uma lacuna que passa a
orientar o próximo investimento em segmentação de rede e filtragem de
DNS.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

A matriz é uma extensão direta da
[Cadeia de Ataque Cibernética](cyber-kill-chain.md), aplicando a cada fase
da cadeia o conjunto de ações defensivas possíveis.

## Termos relacionados

- [Cadeia de Ataque Cibernética (Cyber Kill Chain)](cyber-kill-chain.md)
- [MITRE D3FEND](mitre-d3fend.md)

## Referências

- Hutchins, E. M., Cloppert, M. J., & Amin, R. M. (2011).
  *Intelligence-Driven Computer Network Defense Informed by Analysis of
  Adversary Campaigns and Intrusion Kill Chains*. Lockheed Martin
  Corporation. Disponível em:
  <https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf>
