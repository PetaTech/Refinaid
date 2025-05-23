"use client";

import { useLocale, useTranslations } from "next-intl";
import { Languages } from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import { useRouter, usePathname } from "next/navigation";
import { routing } from "@/i18n/routing";

export function LanguageToggle() {
  const t = useTranslations("LocaleSwitcher");
  const locale = useLocale();
  const router = useRouter();
  const pathname = usePathname();

  const handleLocaleChange = (newLocale: string) => {
    // Get the current path segments after the locale
    const pathSegments = pathname.split("/").slice(2);
    // Create new path with the selected locale and the rest of the path
    const newPath = `/${newLocale}/${pathSegments.join("/")}`;
    router.push(newPath);
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="ghost" size="sm" aria-label="Language toggle">
          <Languages className="w-4" />
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent>
        {routing.locales.map((cur) => (
          <DropdownMenuItem
            key={cur}
            onClick={() => handleLocaleChange(cur)}
            className={cur === locale ? "font-semibold" : ""}
          >
            {t(`locale.${cur}`)}
          </DropdownMenuItem>
        ))}
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
