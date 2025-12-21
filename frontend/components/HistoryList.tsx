'use client';
import { useEffect, useState } from 'react';

export default function HistoryList() {
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function load() {
      setLoading(true);
      try {
        const resp = await fetch('/api/history');
        if (!resp.ok) throw new Error('Failed to load');
        const data = await resp.json();
        setItems(data);
      } catch (e: any) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    }
    load();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div className="text-red-600">{error}</div>;
  if (!items.length) return <div className="text-sm text-slate-500">No history yet</div>;

  return (
    <div className="space-y-3">
      {items.slice().reverse().map((it: any, idx: number) => (
        <div key={idx} className="border rounded p-2 bg-white">
          <div className="text-sm font-medium">{it.url}</div>
          <div className="text-xs text-slate-500 truncate">{it.analysis?.summary?.split('\n')[0]}</div>
        </div>
      ))}
    </div>
  );
}
