# Como contribuir

O RIAC é mantido pela comunidade. Você pode contribuir mesmo sem usar Git
no dia a dia.

## Sem usar Git

Use um dos formulários de issue do repositório:

- [Sugerir um recurso](https://github.com/guiluzsal/riac/issues/new?template=sugerir-recurso.yml) —
  para indicar uma ferramenta, base ou referência de CTI que falta no
  catálogo.
- [Sugerir um verbete](https://github.com/guiluzsal/riac/issues/new?template=sugerir-verbete.yml) —
  para propor um conceito, modelo ou prática que mereça um verbete.
- [Sugerir item do ecossistema](https://github.com/guiluzsal/riac/issues/new?template=sugerir-ecossistema.yml) —
  para indicar uma instituição ou uma norma/legislação brasileira que falta
  na seção Ecossistema.

Você também pode clicar no ícone de lápis (✎) no canto superior direito de
qualquer página deste site para editá-la diretamente no GitHub — isso abre
um Pull Request pronto para revisão, sem precisar clonar o repositório.

## Usando Git e Pull Requests

1. Leia o [`CLAUDE.md`](https://github.com/guiluzsal/riac/blob/main/CLAUDE.md)
   na raiz do repositório: ele define o escopo do projeto, o template de
   verbete e o modelo de dados do catálogo.
2. Crie uma branch a partir de `main` e faça suas alterações.
3. Rode `zensical build` localmente para confirmar que o site compila.
4. Abra um Pull Request. O CI de qualidade (links, schema, markdownlint,
   ortografia, build) roda automaticamente.
5. Um mantenedor revisa e mescla.

## Regras que valem para qualquer contribuição

- Só material **TLP:CLEAR**. Nunca inclua amostras de malware ou IOCs
  sensíveis — aponte para quem já hospeda isso com os controles
  adequados.
- Cada recurso do catálogo tem **uma única categoria principal**; use
  `tags` para aspectos secundários. As regras de desambiguação entre
  categorias estão no `CLAUDE.md`.
- Cite fontes. Todo verbete precisa de ao menos uma referência
  verificável; não invente dados, datas ou atribuições.

Veja o guia completo em
[`CONTRIBUTING.md`](https://github.com/guiluzsal/riac/blob/main/CONTRIBUTING.md).
