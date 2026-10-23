---
tags: [frameworks-e-modelos, ia]
---

# MITRE ATLAS

**Definição:** base de conhecimento sobre táticas e técnicas de ataque
contra sistemas de inteligência artificial e aprendizado de máquina,
estruturada no mesmo formato do MITRE ATT&CK.

!!! info "Origem"
    Desenvolvido pela MITRE a partir do projeto AdvML Threat Matrix e
    lançado publicamente em junho de 2021, como extensão da metodologia do
    ATT&CK para o domínio de IA adversária.

## Explicação

O ATLAS (Adversarial Threat Landscape for Artificial-Intelligence
Systems) documenta táticas e técnicas observadas em ataques reais e
demonstrações de red team contra sistemas de IA — por exemplo, envenenamento
de dados de treinamento, extração de modelo e evasão por entradas
adversárias. Sua estrutura espelha a do ATT&CK, o que facilita a adoção
por times que já usam o framework original.

## Exemplo prático

Uma empresa que expõe um modelo de classificação de malware via API quer
mapear riscos. Consultando o ATLAS, identifica a técnica de *evasão* por
entradas manipuladas e a de *extração de modelo* por consultas repetidas,
e usa essas entradas para orientar controles de limitação de taxa e
monitoramento de consultas anômalas.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

O ATLAS é modelado diretamente sobre o [MITRE ATT&CK](mitre-attack.md),
reaproveitando sua estrutura de táticas e técnicas para o domínio de
sistemas de IA.

## Termos relacionados

- [MITRE ATT&CK](mitre-attack.md)
- [MITRE D3FEND](mitre-d3fend.md)

## Referências

- MITRE ATLAS™. Disponível em: <https://atlas.mitre.org/>
