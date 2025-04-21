import React from 'react'
import type { DocsThemeConfig } from 'nextra-theme-docs';

export default {
  logo: <span>Refinaid Docs</span>,
  footer: {
    component: null
  },
  editLink: {
    component: null
  },
  head: (
    <>
      <link rel="icon" href="/favicon.ico" type="image/png" />
    </>
  ),
  project: {
    link: 'https://github.com/PetaTech/refinaid',
  },
  docsRepositoryBase: 'https://github.com/PetaTech/refinaid',
} as DocsThemeConfig;