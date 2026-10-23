---
tags: [frameworks-e-modelos, indicadores]
---

# Pirâmide da Dor (Pyramid of Pain)

**Definição:** modelo que classifica os tipos de indicadores que um
defensor pode usar contra um adversário, ordenados pelo quanto de "dor"
(custo e esforço) cada tipo impõe ao adversário quando é detectado e
bloqueado.

!!! info "Origem"
    Proposto por David J. Bianco em 2013, no post de blog "The Pyramid of
    Pain".

## Explicação

A pirâmide tem seis níveis, do menos custoso ao mais custoso para o
adversário reagir:

1. **Hash values** (valores de hash) — triviais de mudar, custo quase
   nulo.
2. **IP addresses** (endereços IP) — fáceis de trocar.
3. **Domain names** (nomes de domínio) — um pouco mais custosos de
   registrar novamente.
4. **Network/host artifacts** (artefatos de rede/host) — exigem
   retrabalho de ferramentas.
5. **Tools** (ferramentas) — exigem desenvolver ou adquirir novas
   ferramentas.
6. **TTPs** (táticas, técnicas e procedimentos) — o nível mais alto;
   mudar o comportamento fundamental do ataque é o mais custoso e
   demorado para o adversário.

Quanto mais alto o nível do indicador detectado, maior o custo imposto ao
adversário — por isso, times de CTI devem priorizar a detecção de TTPs em
vez de apenas indicadores triviais como hashes e IPs.

## Exemplo prático

Um feed de IOCs que só bloqueia hashes de malware específicos impõe pouca
dor: o adversário recompila o binário e o hash muda. Já uma regra de
detecção baseada no comportamento (TTP) de um grupo de ransomware — por
exemplo, o uso recorrente de uma técnica específica de movimentação
lateral — continua eficaz mesmo quando o adversário troca de ferramentas.

## Relação com outros modelos (ATT&CK, Diamond Model, Kill Chain…)

A Pyramid of Pain reforça por que o MITRE ATT&CK (focado em TTPs) é mais
valioso para detecção robusta do que listas de indicadores atômicos.
Também se relaciona ao vértice de "capacidade" do
[Modelo Diamante](diamond-model.md): indicadores de capacidade de baixo
nível (hashes, IPs) têm baixo custo de troca para o adversário.

## Termos relacionados

- [Modelo Diamante (Diamond Model)](diamond-model.md)
- [Cadeia de Ataque Cibernética (Cyber Kill Chain)](cyber-kill-chain.md)
- MITRE ATT&CK

## Referências

- Bianco, D. J. (2013). *The Pyramid of Pain*. Disponível em:
  <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
