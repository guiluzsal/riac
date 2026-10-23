---
tags: [frameworks-e-modelos, ttps]
---

# MITRE ATT&CK

**Definição:** base de conhecimento pública e estruturada de táticas,
técnicas e procedimentos (TTPs) de adversários, organizada em uma matriz
que descreve o comportamento observado de ataques reais.

!!! info "Origem"
    Desenvolvido internamente pela MITRE Corporation a partir de 2013, no
    âmbito do projeto FMX (Fort Meade eXperiment), e lançado publicamente
    em maio de 2015.

## Explicação

O ATT&CK organiza o comportamento de adversários em **táticas** (os
objetivos de um ataque, como acesso inicial ou exfiltração) e **técnicas**
(como esse objetivo é alcançado), com sub-técnicas que detalham variações
específicas. Cada técnica traz exemplos de uso por grupos de ameaça reais,
mitigações e formas de detecção. O projeto nasceu focado em redes
corporativas Windows pós-comprometimento e hoje cobre também nuvem,
dispositivos móveis e sistemas de controle industrial (ICS).

## Exemplo prático

Um analista recebe um alerta de execução de PowerShell com codificação
Base64. Ao consultar o ATT&CK, identifica a técnica
T1059.001 (Command and Scripting Interpreter: PowerShell) na tática de
Execução, e usa as mitigações e detecções associadas para orientar a
resposta e fechar a lacuna de visibilidade.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O ATT&CK detalha com profundidade o que a [Cadeia de Ataque
Cibernética](cyber-kill-chain.md) trata em fases amplas, e descreve o
vértice de "capacidade" do [Modelo Diamante](diamond-model.md). O
[MITRE D3FEND](mitre-d3fend.md) mapeia contramedidas defensivas contra as
técnicas do ATT&CK.

## Termos relacionados

- [Cadeia de Ataque Cibernética (Cyber Kill Chain)](cyber-kill-chain.md)
- [Modelo Diamante (Diamond Model)](diamond-model.md)
- [MITRE D3FEND](mitre-d3fend.md)

## Referências

- MITRE ATT&CK®. Disponível em: <https://attack.mitre.org/>
