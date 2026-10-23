---
tags: [padroes, indicadores]
---

# Indicador de Comprometimento (Indicator of Compromise, IOC)

**Definição:** artefato observável em um sistema ou rede — como um hash de
arquivo, endereço IP, domínio ou chave de registro — que sugere com algum
grau de confiança que houve uma intrusão ou atividade maliciosa.

!!! info "Origem"
    O termo e sua formalização técnica estão associados ao lançamento do
    OpenIOC pela Mandiant, em 1º de novembro de 2011: um formato aberto,
    em XML, para descrever e compartilhar indicadores de forma legível por
    máquina.

## Explicação

Um IOC descreve algo que *já aconteceu* ou *já está presente* — por
exemplo, o hash de um arquivo malicioso conhecido — em contraste com um
indicador de comportamento, que descreve um *padrão de ação* do
adversário. A [Pirâmide da Dor](pyramid-of-pain.md) classifica os IOCs
mais simples (hashes, IPs) como os mais fáceis e baratos de um adversário
contornar, e os indicadores de comportamento (TTPs) como os mais custosos.

## Exemplo prático

Um analista recebe uma lista de hashes de arquivos maliciosos associados
a uma campanha de phishing e os carrega no antivírus corporativo como
IOCs de bloqueio. Como são indicadores de baixo nível, o adversário pode
contornar o bloqueio simplesmente recompilando o malware com um hash
diferente — por isso IOCs costumam ser complementados por regras de
comportamento, como as escritas em [YARA](yara.md) ou [Sigma](sigma.md).

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

Os IOCs ocupam os níveis mais baixos da
[Pirâmide da Dor](pyramid-of-pain.md) e costumam ser representados em
formato [STIX](stix.md) como objetos do tipo *Indicator*.

## Termos relacionados

- [Pirâmide da Dor (Pyramid of Pain)](pyramid-of-pain.md)
- [STIX](stix.md)
- [YARA](yara.md)

## Referências

- Mandiant anuncia o padrão OpenIOC. Dark Reading, 1 nov. 2011.
  Disponível em:
  <https://www.darkreading.com/analytics/mandiant-releases-standard-for-sharing-threat-intelligence>
