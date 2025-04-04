import Image from "next/image";

export default function Home() {
  let helloWorld = "Hello World";

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <h1 className="text-4xl sm:text-6xl font-bold text-center text-white-800">
        Top Players
      </h1>
    </div>
  );
}
