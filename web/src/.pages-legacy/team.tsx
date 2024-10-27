import Link from "next/link";
import Head from "next/head";
import Image from "next/image";

const people = [
  {
    name: "ChunHo (Hugo) Lin",
    role: "Founder & CTO",
    imageUrl: "https://avatars.githubusercontent.com/u/94162591?v=4",
    github: "https://github.com/1chooo",
  },
  {
    name: "Reeve Wu",
    role: "ML Engineer",
    imageUrl: "https://avatars.githubusercontent.com/u/110542858?v=4",
    github: "https://github.com/ReeveWu",
  },
  {
    name: "Vincent Li",
    role: "ML Engineer",
    imageUrl: "https://avatars.githubusercontent.com/u/98581766?v=4",
    github: "https://github.com/VincentLi1216",
  },
];

export default function Team() {
  return (
    <div className="mb-10 mt-5 bg-white">
      <Head>
        <title>LinkScape | Team</title>
      </Head>
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <h2 className="mt-12 text-center text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
          Meet Our Team
        </h2>
        <ul
          role="list"
          className="mt-8 grid gap-x-8 gap-y-6 sm:grid-cols-2 sm:gap-x-6 sm:gap-y-8 xl:grid-cols-3 xl:gap-y-10"
        >
          {people.map((person, index) => (
            <div key={index}>
              <li className="flex items-center justify-center">
                <div className="flex flex-col items-center gap-2">
                  <Image
                    className="h-16 w-16 rounded-full"
                    src={person.imageUrl}
                    width={512}
                    height={512}
                    alt=""
                  />
                  <div className="text-center">
                    <Link href={person.github}>
                      <h3 className="text-base font-semibold leading-7 tracking-tight text-gray-900 hover:underline">
                        {person.name}
                      </h3>
                    </Link>
                    <p className="text-sm font-semibold leading-6 text-indigo-600">
                      {person.role}
                    </p>
                  </div>
                </div>
              </li>
            </div>
          ))}
        </ul>
      </div>
    </div>
  );
}
