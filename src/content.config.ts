import { defineCollection, z } from 'astro:content'
import { glob } from 'astro/loaders'

const projetos = defineCollection({
  loader: glob({ pattern: '**/index.md', base: './src/content/projetos' }),
  schema: z.object({
    title: z.string(),
    resumo: z.string(),
    autor: z.string(),
    email: z.string().optional(),
    data: z.string(),
    categoria: z.string(),
    idade: z.string().optional(),
    dificuldade: z.string(),
    duracao: z.string(),
    capa: z.string().optional(),
    tags: z.array(z.string()).default([]),
  }),
})

export const collections = { projetos }