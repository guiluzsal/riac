---
tags: [frameworks-e-modelos, analise-de-intrusao]
---

# Modelo Diamante (Diamond Model of Intrusion Analysis)

**Definição:** modelo analítico que representa cada evento de intrusão como
um diamante com quatro vértices — adversário, infraestrutura, capacidade e
vítima — conectados por arestas que representam as relações entre eles.

!!! info "Origem"
    Proposto por Sergio Caltagirone, Andrew Pendergast e Christopher Betz
    em 2013, no relatório técnico "The Diamond Model of Intrusion
    Analysis".

## Explicação

Cada evento de intrusão é modelado como um diamante cujos quatro vértices
são:

- **Adversário:** quem conduz a intrusão.
- **Infraestrutura:** os meios técnicos usados pelo adversário (domínios,
  IPs, e-mails).
- **Capacidade:** as ferramentas e técnicas empregadas (malware, exploits).
- **Vítima:** o alvo da intrusão.

As arestas entre os vértices representam as relações sociopolíticas (entre
adversário e vítima) e tecnológicas (entre infraestrutura e capacidade) que
conectam o evento. Vários diamantes, conectados ao longo do tempo, formam
uma "atividade-ameaça" (*activity thread*), que por sua vez pode ser
agrupada em "grupos de atividade" (*activity groups*) para revelar
campanhas mais amplas de um mesmo adversário.

## Exemplo prático

Um analista identifica um e-mail de phishing (infraestrutura: domínio de
envio) que entrega um anexo malicioso (capacidade: malware) contra o
departamento financeiro de uma empresa (vítima). Ao preencher os quatro
vértices desse evento, o analista pode pivotar: buscando outros eventos que
compartilhem a mesma infraestrutura ou capacidade, revelando se o mesmo
adversário atacou outras vítimas.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O Diamond Model é frequentemente usado em conjunto com a
[Cadeia de Ataque Cibernética](cyber-kill-chain.md): cada fase da Kill
Chain pode ser representada como um diamante, permitindo correlacionar
eventos ao longo de uma campanha. Também se complementa com o MITRE
ATT&CK, que detalha a dimensão de "capacidade" (táticas e técnicas) em
profundidade.

## Termos relacionados

- [Cadeia de Ataque Cibernética (Cyber Kill Chain)](cyber-kill-chain.md)
- [Pirâmide da Dor (Pyramid of Pain)](pyramid-of-pain.md)
- MITRE ATT&CK

## Referências

- Caltagirone, S., Pendergast, A., & Betz, C. (2013). *The Diamond Model of
  Intrusion Analysis*. Center for Cyber Intelligence Analysis and Threat
  Research. Disponível em:
  <https://apps.dtic.mil/sti/pdfs/ADA586960.pdf>
