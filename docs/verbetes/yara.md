---
tags: [padroes, deteccao]
---

# YARA

**Definição:** linguagem de regras baseada em padrões (textuais, binários
ou por expressões regulares) usada para identificar e classificar
amostras de malware e outros arquivos de interesse.

!!! info "Origem"
    Criada por Victor M. Alvarez, então na VirusTotal, e lançada
    publicamente no GitHub em 2013. Em 2024, Alvarez anunciou o YARA-X, uma
    reescrita do projeto em Rust, com a primeira versão estável lançada em
    junho de 2025.

## Explicação

Uma regra YARA combina uma lista de "strings" (padrões a buscar) com uma
condição lógica sobre quais e quantas dessas strings precisam aparecer em
um arquivo para que ele seja classificado como correspondente. Além de
malware, a ferramenta serve para triagem forense e caça a ameaças em larga
escala, já que pode ser aplicada contra grandes volumes de arquivos ou
integrada a sandboxes e EDRs.

## Exemplo prático

Um pesquisador analisa uma nova família de ransomware e identifica
strings de configuração recorrentes no binário. Ele escreve uma regra
YARA com essas strings e a condição de que ao menos três delas precisam
estar presentes; a regra passa então a ser usada para varrer repositórios
de amostras em busca de variantes da mesma família.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

Regras YARA costumam ser associadas a famílias de malware catalogadas em
bases como o Malpedia, e complementam indicadores de baixo nível (hashes)
descritos na [Pirâmide da Dor](pyramid-of-pain.md), por operarem sobre
padrões estruturais em vez de um único hash exato.

## Termos relacionados

- [Pirâmide da Dor (Pyramid of Pain)](pyramid-of-pain.md)
- [Sigma](sigma.md)

## Referências

- YARA Documentation. Disponível em: <https://yara.readthedocs.io/>
