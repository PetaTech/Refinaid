import React from "react";
import Header from "@/components/header";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Refinaid | Donate",
  description: "Donate to Refinaid",
};

export default function Donate() {
  return (
    <>
      <Header />
      <div className="h-512px screen flex flex-col mt-16">
        <iframe
          src="https://bank.hackclub.com/donations/start/linkscape"
          name="donateFrame"
          height="780px"
          width="screen"
          allowFullScreen
        ></iframe>
      </div>
    </>
  );
}
