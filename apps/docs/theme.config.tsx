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
      <link rel="icon" href="/favicon.png" type="image/png" />
    </>
  ),
  project: {
    link: 'https://github.com/1chooo/refinaid',
  },
  docsRepositoryBase: 'https://github.com/1chooo/refinaid',
} as DocsThemeConfig;