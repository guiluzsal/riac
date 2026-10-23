---
tags: [frameworks-e-modelos, estrategia]
---

# Sliding Scale of Cyber Security

**Definição:** modelo que organiza investimentos e ações de segurança em
cinco categorias — Arquitetura, Defesa Passiva, Defesa Ativa, Inteligência
e Ofensiva — ordenadas da mais fundamental à mais avançada, para orientar
a priorização de investimentos.

!!! info "Origem"
    Proposto por Robert M. Lee em artigo de política publicado pelo SANS
    Institute e pela New America em 2 de setembro de 2015.

## Explicação

As cinco categorias, da esquerda para a direita, são: **Arquitetura**
(projetar e configurar sistemas de forma segura), **Defesa Passiva**
(controles que funcionam sem intervenção humana constante, como
firewalls), **Defesa Ativa** (monitoramento e resposta conduzidos por
analistas humanos), **Inteligência** (coleta e análise sobre adversários
para orientar a defesa) e **Ofensiva** (ações contra o próprio
adversário). O argumento central do modelo é que cada categoria depende
das anteriores como base, e que investir primeiro nas categorias da
esquerda produz o melhor retorno antes de avançar para a direita.

## Exemplo prático

Uma organização recém-criada investe primeiro em uma arquitetura de rede
bem segmentada e em controles de defesa passiva (antivírus, firewalls),
antes de montar uma equipe dedicada de resposta a incidentes (defesa
ativa) ou de assinar feeds de inteligência de ameaças — reconhecendo que
pular etapas da escala tende a gerar capacidades pouco sustentadas.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

A categoria "Inteligência" da escala é onde modelos como o
[MITRE ATT&CK](mitre-attack.md) e o [Modelo Diamante](diamond-model.md)
são tipicamente aplicados; a categoria "Defesa Passiva" se conecta
diretamente ao [MITRE D3FEND](mitre-d3fend.md).

## Termos relacionados

- [MITRE ATT&CK](mitre-attack.md)
- [MITRE D3FEND](mitre-d3fend.md)

## Referências

- Lee, R. M. (2015). *The Sliding Scale of Cyber Security*. SANS
  Institute / New America. Disponível em:
  <https://www.newamerica.org/cybersecurity-initiative/policy-papers/the-sliding-scale-of-cyber-security/>
