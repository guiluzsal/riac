---
tags: [padroes, resposta-a-incidentes]
---

# VERIS (Vocabulary for Event Recording and Incident Sharing)

**Definição:** conjunto de métricas e vocabulário padronizado para
descrever incidentes de segurança de forma estruturada e repetível,
permitindo comparar e agregar dados de incidentes entre organizações.

!!! info "Origem"
    Desenvolvido pela Verizon, que o tornou público em código aberto.
    Batizado originalmente de "Verizon Enterprise Risk and Incident
    Sharing", foi renomeado para "Vocabulary for Event Recording and
    Incident Sharing" para facilitar sua adoção por outras organizações.

## Explicação

O VERIS estrutura um incidente em torno de quatro eixos — os "4 As":
**Agente** (quem causou o incidente), **Ativo** (o que foi afetado),
**Atributo** (como a segurança do ativo foi violada: confidencialidade,
integridade ou disponibilidade) e **Ação** (o que o agente fez). Esse
vocabulário é a base de dados por trás do Data Breach Investigations
Report (DBIR) da Verizon, publicado anualmente.

## Exemplo prático

Uma equipe de resposta a incidentes documenta um ataque de phishing
seguido de uso de credenciais roubadas, classificando-o em VERIS como
ação "Social" (engenharia social) seguida de ação "Hacking" (uso de
credenciais válidas) sobre um ativo do tipo "Servidor", permitindo
comparar esse padrão com milhares de outros incidentes catalogados da
mesma forma.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O VERIS tem mapeamento documentado para técnicas do
[MITRE ATT&CK](mitre-attack.md), permitindo traduzir incidentes
catalogados em VERIS para a terminologia de táticas e técnicas do
framework.

## Termos relacionados

- [MITRE ATT&CK](mitre-attack.md)

## Referências

- VERIS Community. *The VERIS Framework*. Disponível em:
  <https://verisframework.org/>
