# UdescMake

Plataforma colaborativa para compartilhar e descobrir projetos maker da comunidade UDESC e além. O objetivo é ser um repositório central de projetos DIY com instruções passo a passo, permitindo que qualquer pessoa contribua com seus próprios projetos.

## Sobre o Projeto

O UdescMake foi desenvolvido como parte do Projeto Integrador I do curso de Engenharia de Software da UDESC. A plataforma conecta criadores e aprendizes em torno de projetos práticos nas mais diversas áreas: eletrônica, robótica, impressão 3D, programação, marcenaria, costura, culinária, arte e muito mais.

### Funcionalidades

- **Galeria de projetos** com busca por título, resumo e tags
- **Filtros** por categoria, nível de dificuldade, duração e faixa etária
- **Página de detalhes** com instruções passo a passo e imagens
- **Formulário de envio** em múltiplas etapas para submissão de novos projetos (gera um arquivo `.zip` com a estrutura pronta)
- **Guia de contribuição** via fork e pull request no GitHub

## Tecnologias

- [Astro](https://astro.build) — gerador de sites estáticos
- [Tailwind CSS](https://tailwindcss.com) — estilização utilitária
- [JSZip](https://stuk.github.io/jszip/) — geração de arquivos ZIP no navegador
- TypeScript

## Estrutura do Projeto

```text
/
├── public/
│   ├── favicon.svg
│   └── videos/              # Vídeos do banner animado (video1–5.mp4)
├── src/
│   ├── content/
│   │   └── projetos/        # Arquivos .md de cada projeto
│   │       └── nome-do-projeto/
│   │           ├── index.md
│   │           └── imagens…
│   ├── layouts/
│   │   └── Layout.astro     # Layout base (header, nav, footer)
│   ├── pages/
│   │   ├── index.astro          # Página inicial com galeria e filtros
│   │   ├── enviar.astro         # Formulário de envio de projetos
│   │   ├── contribuir.astro     # Guia de contribuição
│   │   └── projetos/[slug].astro # Página dinâmica de cada projeto
│   ├── styles/
│   │   └── global.css
│   └── content.config.ts    # Schema das coleções de conteúdo
└── package.json
```

## Como Rodar Localmente

**Pré-requisito:** Node.js >= 22.12.0

```sh
# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm run dev
```

Acesse [http://localhost:4321](http://localhost:4321) no navegador.

## Comandos Disponíveis

| Comando             | Ação                                              |
| :------------------ | :------------------------------------------------ |
| `npm install`       | Instala as dependências                           |
| `npm run dev`       | Inicia o servidor local em `localhost:4321`       |
| `npm run build`     | Gera o site de produção em `./dist/`              |
| `npm run preview`   | Pré-visualiza o build antes de publicar           |

## Como Contribuir com um Projeto

1. Faça um **fork** do repositório
2. Crie uma pasta em `src/content/projetos/nome-do-seu-projeto/`
3. Adicione um arquivo `index.md` com o frontmatter e as instruções
4. Adicione as imagens na mesma pasta
5. Abra um **Pull Request**

O site é atualizado automaticamente via GitHub Actions quando o PR é aprovado.

### Estrutura do `index.md`

```yaml
---
title: Nome do Projeto
resumo: Breve descrição do projeto
autor: Seu Nome
email: seu@email.com        # opcional
data: "2025-01-01"
categoria: Eletrônica       # Eletrônica | Robótica | Impressão 3D | Programação | Marcenaria | Costura | Culinária | Arte | Outros
dificuldade: Iniciante      # Iniciante | Intermediário | Avançado
duracao: 1 hora
idade: "+10 Anos"           # opcional
capa: ./capa.png            # opcional
tags: [arduino, led, iniciante]
---

## Materiais Necessários
...

## Passo 1 — Título do passo
...
```

> Você também pode usar o [formulário de envio](/enviar) da plataforma para gerar automaticamente a estrutura de pastas e o arquivo `.zip` pronto para o PR.

## Licença

Este projeto é desenvolvido para fins educacionais no contexto do Projeto Integrador I — UDESC.
