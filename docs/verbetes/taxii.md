---
tags: [padroes, interoperabilidade]
---

# TAXII (Trusted Automated eXchange of Indicator Information)

**Definição:** protocolo de transporte para a troca automatizada de
inteligência de ameaças cibernéticas, tipicamente usado para distribuir
dados no formato [STIX](stix.md) entre sistemas.

!!! info "Origem"
    Desenvolvido junto com o STIX, como projeto do Departamento de
    Segurança Interna dos EUA (DHS) operado tecnicamente pela MITRE a
    partir do início dos anos 2010. Passou para o comitê técnico de Cyber
    Threat Intelligence (CTI TC) da OASIS, que padronizou o TAXII 2.1 em
    2021.

## Explicação

O TAXII define serviços e troca de mensagens via HTTPS — como
"Collections" (coleções de dados que um servidor expõe) e "Channels"
(canais de publicação e assinatura) — mas, deliberadamente, não define
acordos de confiança, governança ou aspectos não técnicos do
compartilhamento de informação; isso fica a cargo de cada comunidade que
o utiliza.

## Exemplo prático

Um CSIRT setorial mantém um servidor TAXII com uma Collection de
indicadores recentes. Organizações associadas configuram seus TIPs para
consultar essa Collection periodicamente via API TAXII, recebendo
automaticamente os pacotes STIX novos sem intervenção manual.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O TAXII é o mecanismo de transporte mais comum para disseminar dados
estruturados em [STIX](stix.md); os dois padrões são normalmente adotados
juntos.

## Termos relacionados

- [STIX](stix.md)

## Referências

- OASIS Cyber Threat Intelligence Technical Committee. *TAXII Version
  2.1*. Disponível em: <https://oasis-open.github.io/cti-documentation/>
