"use client";

import Link from 'next/link'
import React from 'react'
import Image from 'next/image'
import { UserNav } from './user-nav';
import { ModeToggle } from "@/components/theme/mode-toggle";
import { VisitGitHub } from "@/components/visit-github";



const Header = () => {
  return (
    <header className='fixed inset-x-0 top-0 z-40 shadow-sm saturate-100 backdrop-blur-[10px]'>
      <div className='mx-auto flex h-[60px] max-w-4xl items-center justify-between px-8'>
        <Link href='/' aria-label='Home' title='Home'>
          <Image
            src="https://www.1chooo.com/favicon.ico"
            alt="Profile"
            className="w-10 h-10 rounded-full object-cover"
            width={40}
            height={40}
          />
        </Link>
        <div className="flex flex-1 items-center justify-end">
          <VisitGitHub />
          <ModeToggle />
          <UserNav />
        </div>
      </div>
    </header>
  )
}

export default Header
