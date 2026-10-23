---
tags: [frameworks-e-modelos, compartilhamento]
---

# Permissible Actions Protocol (PAP)

**Definição:** protocolo que indica quais ações um receptor pode tomar com
uma informação de inteligência recebida, classificando o risco de revelar
ao adversário que ele foi detectado.

!!! info "Origem"
    Introduzido em 2016 como parte das taxonomias do MISP (Malware
    Information Sharing Platform), mantidas pelo CIRCL (Computer Incident
    Response Center Luxembourg).

## Explicação

O PAP define quatro níveis, geralmente usados junto com o
[TLP](traffic-light-protocol.md): **PAP:RED** (apenas investigação digital
ou detecção em infraestrutura dedicada, sem tocar o adversário),
**PAP:AMBER** (apenas exploração passiva), **PAP:GREEN** (interação não
intrusiva com fontes maliciosas permitida) e **PAP:CLEAR** (sem
restrições além de licenciamento e lei). O objetivo é evitar que uma ação
de resposta avise o adversário antes da hora.

## Exemplo prático

Um indicador de C2 chega marcado PAP:AMBER. Um analista pode usá-lo para
buscar passivamente logs internos em busca de conexões para aquele
endereço, mas não pode acessá-lo ativamente (por exemplo, varrendo portas
ou interagindo com o servidor), o que poderia alertar o operador da
infraestrutura maliciosa.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O PAP complementa o [TLP](traffic-light-protocol.md): o TLP regula *quem*
recebe a informação, o PAP regula *o que* o receptor pode fazer com ela.

## Termos relacionados

- [Traffic Light Protocol (TLP)](traffic-light-protocol.md)

## Referências

- MISP Project. *MISP Taxonomies — PAP*. Disponível em:
  <https://www.misp-project.org/taxonomies.html#_pap>
