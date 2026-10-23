---
tags: [padroes, interoperabilidade]
---

# STIX (Structured Threat Information eXpression)

**Definição:** linguagem e formato de serialização para representar
informações de inteligência de ameaças cibernéticas — indicadores,
TTPs, atores, campanhas e suas relações — de forma estruturada e
compartilhável entre ferramentas e organizações.

!!! info "Origem"
    Iniciado como projeto do Departamento de Segurança Interna dos EUA
    (DHS) por volta de 2012, com a MITRE operando como mantenedora técnica.
    A partir de 2017 (STIX 2.0), a especificação passou a ser desenvolvida
    pelo comitê técnico de Cyber Threat Intelligence (CTI TC) da OASIS, que
    publicou o padrão STIX 2.1 em 2021.

## Explicação

O STIX define "Objetos de Domínio Cibernético" (SDOs) — como
*Indicator*, *Malware*, *Threat Actor* e *Campaign* — e relações entre
eles, permitindo expressar não só indicadores isolados, mas o contexto que
os conecta (por exemplo, qual ator usa qual malware em qual campanha). É
tipicamente serializado em JSON e trocado entre sistemas via
[TAXII](taxii.md).

## Exemplo prático

Um TIP (plataforma de threat intelligence) recebe um pacote STIX contendo
um objeto *Indicator* (um hash de arquivo), relacionado a um objeto
*Malware* (uma família de ransomware) e a um objeto *Threat Actor*. Ao
importar o pacote, a plataforma reconstrói automaticamente essas relações
no seu grafo interno, sem que o analista precise recriá-las manualmente.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O STIX é o formato mais comum para exportar e trocar dados estruturados
sobre os elementos do [Modelo Diamante](diamond-model.md) (adversário,
infraestrutura, capacidade, vítima) e sobre técnicas do
[MITRE ATT&CK](mitre-attack.md), que podem ser referenciadas diretamente
dentro de objetos STIX.

## Termos relacionados

- [TAXII](taxii.md)
- [MITRE ATT&CK](mitre-attack.md)

## Referências

- OASIS Cyber Threat Intelligence Technical Committee. *STIX Version 2.1*.
  Disponível em: <https://oasis-open.github.io/cti-documentation/>
