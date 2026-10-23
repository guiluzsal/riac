---
tags: [frameworks-e-modelos, coleta]
---

# Inteligência de Fontes Abertas (Open Source Intelligence, OSINT)

**Definição:** inteligência produzida a partir de informação disponível
publicamente — sites, redes sociais, registros públicos, dados técnicos
de internet — sem exigir acesso restrito ou clandestino à fonte.

!!! info "Origem"
    Como disciplina formal de inteligência, foi consolidada pela
    comunidade de inteligência dos EUA na Intelligence Community
    Directive 301, assinada pelo primeiro Diretor de Inteligência Nacional
    (DNI), John Negroponte, em 11 de julho de 2006, que determinou tratar
    fontes abertas como "fonte de primeiro recurso". A diretiva foi
    revogada em 2012, mas a prática de OSINT como disciplina de
    inteligência se manteve e se expandiu.

## Explicação

Em CTI, OSINT cobre desde a varredura de infraestrutura exposta
(ferramentas como Shodan e Censys) até a pesquisa de registros de
domínio, redes sociais e fóruns onde adversários discutem ou vendem
acesso. A disciplina se distingue de outras fontes de inteligência (como
HUMINT ou SIGINT) pelo critério de que a informação é, em princípio,
acessível a qualquer pessoa — embora a coleta e correlação em escala
exijam ferramental especializado.

## Exemplo prático

Um analista investiga uma campanha de phishing e usa OSINT para
correlacionar o domínio usado no ataque com registros de WHOIS históricos,
certificados TLS e menções em fóruns públicos, reconstruindo parte da
infraestrutura do adversário sem acessar nenhuma fonte restrita.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

OSINT é a principal fonte de dados para preencher os vértices de
infraestrutura e capacidade do [Modelo Diamante](diamond-model.md), e
corresponde à fase de coleta do ciclo de inteligência.

## Termos relacionados

- [Modelo Diamante (Diamond Model)](diamond-model.md)

## Referências

- Office of the Director of National Intelligence. *Intelligence
  Community Directive 301 — National Open Source Enterprise* (2006).
  Disponível em:
  <https://irp.fas.org/dni/icd/index.html>
