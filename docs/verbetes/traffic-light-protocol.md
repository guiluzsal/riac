---
tags: [frameworks-e-modelos, compartilhamento]
---

# Traffic Light Protocol (TLP)

**Definição:** conjunto de quatro rótulos de cores que indicam até onde
uma informação sensível pode ser compartilhada, usado para permitir a
troca de inteligência sem comprometer fontes e métodos.

!!! info "Origem"
    Criado pelo NISCC (National Infrastructure Security Co-ordination
    Centre) do Reino Unido em 1999. Passou a ser mantido pelo FIRST (Forum
    of Incident Response and Security Teams), que publicou a revisão
    TLP 2.0 em agosto de 2022.

## Explicação

O TLP 2.0 define quatro rótulos, do mais restrito ao mais aberto:
**TLP:RED** (restrito aos participantes da conversa), **TLP:AMBER** (e a
variante AMBER+STRICT, restrita à própria organização), **TLP:GREEN**
(compartilhável dentro da comunidade de interesse, mas não publicamente) e
**TLP:CLEAR** (sem restrições de compartilhamento). A revisão 2.0
substituiu o antigo TLP:WHITE por TLP:CLEAR e adicionou o nível
AMBER+STRICT.

## Exemplo prático

Um CSIRT recebe de um parceiro um relatório técnico marcado TLP:AMBER
sobre uma campanha em andamento. A equipe pode usar as informações
internamente e repassá-las a clientes diretamente afetados, mas não pode
publicá-las em um blog público — isso só seria permitido se o documento
fosse TLP:CLEAR.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O TLP é usado em conjunto com o Permissible Actions Protocol
([PAP](permissible-actions-protocol.md)): o TLP controla *quem* pode
receber a informação, e o PAP controla *que ações* o receptor pode tomar
com ela.

## Termos relacionados

- [Permissible Actions Protocol (PAP)](permissible-actions-protocol.md)
- [Admiralty Code](admiralty-code.md)

## Referências

- FIRST. *Traffic Light Protocol (TLP) — FIRST Standards Definitions and
  Usage Guidance — Version 2.0*. Disponível em:
  <https://www.first.org/tlp/>
