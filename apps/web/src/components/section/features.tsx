import Image from 'next/image';

export default function Features() {
  return (
    <div
      id="features"
      className="relative mb-24 flex w-full flex-col items-center gap-40 px-3 text-center"
    >
      <div
        className="mt-32 flex flex-col items-center justify-center gap-10 lg:flex-row"
      >
        <Image
          src="/chatger.png"
          draggable="false"
          className="ml-2 w-full max-w-xl rounded-xl shadow-xl"
          alt="Chatger"
          width={1600}
          height={900}
        />
        <div className="flex max-w-[24rem] flex-col gap-5">
          <h2 className="text-3xl font-bold">Chatger</h2>
          <div>
            Code with expert {" "}
            <span className="underline decoration-primary decoration-wavy">
              AI tutors
            </span> {" "}
            and get instant feedback on your code.
          </div>
        </div>
      </div>
      <div className="flex flex-col items-center justify-center gap-10 lg:flex-row">
        <div className="flex max-w-[24rem] flex-col gap-5">
          <h2 className="text-3xl font-bold">Simple AI</h2>
          <div>
            Easily integrate with {" "}
            <span
              className="underline decoration-primary decoration-wavy"
            >web browsers
            </span> {" "}
            and train your model in a single click.
          </div>
        </div>
        <Image
          draggable="false"
          src="/simple-ai.png"
          alt="Simple AI"
          className="ml-2 w-full max-w-xl rounded-xl shadow-xl"
          width={1600}
          height={900}
        />
      </div>
    </div>
  );
}