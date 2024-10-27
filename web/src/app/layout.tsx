import "./globals.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { Analytics } from "@vercel/analytics/react";
import Footer from "@/src/components/footer";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Refinaid",
  description: "Enabling everyone unfamiliar with programming languages to easily engage with AI and open the doors to the world of the future.",
  icons: {
    shortcut: "/favicon.png",
  },
  openGraph: {
    title: "Refinaid",
    description: "We are Refinaid.",
    url: "https://refinaid.vercel.app/",
    siteName: "Refinaid",
    images: [
      {
        url: "https://refinaid-docs.vercel.app/banner-thin.png",
        width: 2608,
        height: 769,
      },
    ],
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div
          className={
            "background-dotted w-screen fixed left-0 top-0 h-screen z-[-1] dark:opacity-10"
          }
        />
        {children}

        <Analytics />
        <Footer />
      </body>
    </html>
  );
}
