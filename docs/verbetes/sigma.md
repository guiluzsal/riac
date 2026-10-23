---
tags: [padroes, deteccao]
---

# Sigma

**Definição:** formato genérico e aberto para escrever regras de detecção
sobre logs, convertidas por "backends" para a linguagem de consulta
específica de diferentes SIEMs.

!!! info "Origem"
    Criado por Florian Roth e Thomas Patzke, com a primeira versão
    publicada em 2017.

## Explicação

Uma regra Sigma é escrita em YAML e descreve a fonte do log e a lógica de
detecção de forma independente de produto. Conversores ("backends")
traduzem essa regra para a sintaxe de SIEMs específicos (como Splunk,
Elastic ou Microsoft Sentinel), evitando que times de detecção precisem
reescrever a mesma lógica várias vezes para ferramentas diferentes. O
projeto descreve a si mesmo como o equivalente, para arquivos de log, do
que o YARA é para arquivos e o Snort é para tráfego de rede.

## Exemplo prático

Um time de detecção escreve uma regra Sigma para identificar criação
suspeita de tarefas agendadas via `schtasks.exe` com parâmetros incomuns.
Essa única regra é convertida automaticamente para consultas equivalentes
em dois SIEMs diferentes usados por unidades de negócio distintas da
mesma empresa.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

Muitas regras publicadas pela comunidade SigmaHQ trazem referências diretas
a técnicas do [MITRE ATT&CK](mitre-attack.md), facilitando mapear a
cobertura de detecção de um ambiente às táticas e técnicas do framework.

## Termos relacionados

- [YARA](yara.md)
- [MITRE ATT&CK](mitre-attack.md)

## Referências

- SigmaHQ. Disponível em: <https://sigmahq.io/>
