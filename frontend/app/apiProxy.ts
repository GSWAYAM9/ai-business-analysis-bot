export async function apiPostAnalyze(url: string) {
    const resp = await fetch('/api/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });
    if (!resp.ok) {
      const text = await resp.text();
      throw new Error(text || 'API error');
    }
    return resp.json();
  }
  
  export async function apiGetHistory() {
    const resp = await fetch('/api/history');
    if (!resp.ok) throw new Error('History fetch failed');
    return resp.json();
  }
  