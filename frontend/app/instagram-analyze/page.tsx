"use client";

import { useState } from "react";
import UrlForm from "@/components/UrlForm";
import ResultCard from "@/components/ResultCard";
import { scrapeInstagram } from "@/lib/api";

export default function InstagramAnalyzePage() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleScrape = async (url: string) => {
    setLoading(true);
    setResult(null);

    const response = await scrapeInstagram(url);
    setResult(response);

    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-black text-white flex flex-col items-center py-20 px-6">
      <h1 className="text-4xl font-extrabold mb-8 bg-gradient-to-r from-blue-400 to-indigo-400 bg-clip-text text-transparent">
        Premium Instagram Business Analyzer
      </h1>

      <UrlForm onSubmit={handleScrape} loading={loading} />

      {result && <ResultCard result={result} />}
    </div>
  );
}
