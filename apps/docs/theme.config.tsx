import React from 'react'
import { DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  logo: <span>Refinaid Docs</span>,
  project: {
    link: 'https://github.com/1chooo/refinaid',
  },
  head: (
    <>
      <link rel="icon" href="/favicon.png" type="image/png" />
    </>
  ),
  chat: {
    link: 'https://discord.com',
  },
  docsRepositoryBase: 'https://github.com/1chooo/refinaid',
  footer: {
    text: 'Refinaid Template',
  },
}

export default config
