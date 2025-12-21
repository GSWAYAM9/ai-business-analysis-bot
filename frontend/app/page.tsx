"use client";

import { useState } from "react";
import AnalyzeModal from "@/components/AnalyzeModal";
import ResultCard from "@/components/ResultCard";

export default function Home() {
  const [open, setOpen] = useState(false);
  const [result, setResult] = useState<any>(null);

  return (
    <main className="relative min-h-screen bg-gradient-to-br from-purple-950 via-black to-black text-white">
      {/* Header */}
      <div className="text-center pt-20">
        <h1 className="text-4xl font-extrabold">Analyze a Business</h1>
        <p className="text-gray-400 mt-2">Instagram Analyzer</p>
      </div>

      {/* Result */}
      {result && (
        <div className="mt-12 px-4">
          <ResultCard result={result} />
        </div>
      )}

      {/* Floating + Button */}
      <button
        onClick={() => setOpen(true)}
        className="fixed bottom-8 right-8 z-50 w-14 h-14 rounded-full
                   bg-gradient-to-r from-purple-600 to-pink-600
                   text-white text-3xl font-bold shadow-2xl
                   hover:scale-110 transition"
      >
        +
      </button>

      {/* Modal */}
      <AnalyzeModal
        open={open}
        onClose={() => setOpen(false)}
        onResult={setResult}
      />
    </main>
  );
}
