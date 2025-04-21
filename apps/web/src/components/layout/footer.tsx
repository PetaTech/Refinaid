import React from "react";
import { Github, Mail } from "lucide-react";
import Link from "next/link";

import Image from "next/image";

const Footer = () => {
  return (
    <div className="flex w-full flex-col items-center justify-between gap-10 border-t dark:border-[#ffffff20] py-20 lg:flex-row border-[#00000020]">
      <div className="flex flex-col items-center gap-4 lg:ml-32 lg:items-start">
        <Image
          className="flex items-center gap-2 text-xl font-bold"
          src="/favicon.ico"
          alt="Logo of Refinaid"
          quality={100}
          width={48}
          height={48}
          draggable={false}
        />
        <span className="text-xs text-[#00000070] dark:text-[#ffffff70]">
          Copyright © 2023-{new Date().getFullYear()} Refinaid
        </span>
        <div className="flex items-center justify-center gap-3">
          <Link
            href="https://github.com/PetaTech"
            className="cursor-pointer text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
            target="_blank"
            rel="noreferrer noopener"
            aria-label="GitHub"
          >
            <Github />
          </Link>
          <Link
            href="mailto:official@lovedbymen.com"
            className="ml-1 cursor-pointer text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
            target="_blank"
            rel="noreferrer noopener"
            aria-label="Mail"
          >
            <Mail />
          </Link>
        </div>
      </div>
      <div className="grid grid-cols-2 gap-20 sm:grid-cols-3 lg:mr-64">
        <div className="flex flex-col gap-2">
          <div className="font-medium">COMMUNITY</div>
          <Link
            href="/#"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
          >
            Blog
          </Link>
          <Link
            href="https://github.com/PetaTech/refinaid/issues"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
            target="_blank"
            rel="noreferrer noopener"
            aria-label="Feedback"
          >
            Feedback
          </Link>
          <Link
            href="/#"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
            target="_blank"
            rel="noreferrer noopener"
            aria-label="Feedback"
          >
            Docs
          </Link>
        </div>
        <div className="flex flex-col gap-2">
          <div className="font-medium">PRODUCT</div>
          <Link
            href="/#get-started"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
          >
            Features
          </Link>
          <Link
            href="/#"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
          >
            Mechanism
          </Link>
        </div>
        <div className="flex flex-col gap-2">
          <div className="font-medium">COMPANY</div>
          <Link
            href="/#"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
          >
            Privacy
          </Link>
          <Link
            href="/#"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
          >
            Terms
          </Link>
          <Link
            href="https://github.com/PetaTech/refinaid/blob/main/LICENSE"
            className="text-sm text-[#00000070] dark:text-[#ffffff70] transition-all hover:text-black dark:hover:text-white"
          >
            License
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Footer;
