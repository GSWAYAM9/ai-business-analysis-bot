'use client';
import { useState } from 'react';
import { apiPostAnalyze, apiGetHistory } from '../app/apiProxy';
import AnalysisCard from './AnalysisCard';

export default function LinkForm() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState<any | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setAnalysis(null);
    setLoading(true);
    try {
      const res = await apiPostAnalyze(url);
      setAnalysis(res.analysis);
    } catch (err: any) {
      setError(err.message || 'Failed');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <form onSubmit={submit} className="flex flex-col gap-3">
        <input
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://instagram.com/your_brand"
          className="border rounded px-3 py-2 outline-none focus:ring"
        />
        <div className="flex gap-3 items-center">
          <button type="submit" disabled={loading || !url} className="bg-slate-800 text-white px-4 py-2 rounded disabled:opacity-60">
            {loading ? 'Analyzing...' : 'Analyze'}
          </button>
          <button type="button" onClick={async() => {
            // quick load example
            setUrl('https://example.com');
          }} className="text-sm text-slate-600">Use sample</button>
        </div>
      </form>

      <div className="mt-6">
        {error && <div className="text-red-600">{error}</div>}
        {analysis && <AnalysisCard analysis={analysis} />}
      </div>
    </div>
  );
}
