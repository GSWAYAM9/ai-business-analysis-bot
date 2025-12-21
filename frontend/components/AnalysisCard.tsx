export default function AnalysisCard({ analysis }: { analysis: any }) {
    const { summary, strengths, weaknesses, improvements, scores, influencer_suggestions } = analysis || {};
  
    return (
      <div className="bg-white p-6 rounded shadow">
        <h3 className="text-xl font-semibold mb-2">Executive Summary</h3>
        <pre className="whitespace-pre-wrap text-sm text-slate-700 bg-slate-50 p-3 rounded mb-4">{summary}</pre>
  
        <div className="grid md:grid-cols-3 gap-4 mb-4">
          <div className="p-3 bg-slate-50 rounded">
            <h4 className="font-medium">Brand Health</h4>
            <div className="text-2xl font-bold">{scores?.brand_health ?? '—'}</div>
          </div>
          <div className="p-3 bg-slate-50 rounded">
            <h4 className="font-medium">Engagement</h4>
            <div className="text-2xl font-bold">{scores?.engagement ?? '—'}</div>
          </div>
          <div className="p-3 bg-slate-50 rounded">
            <h4 className="font-medium">Influencers</h4>
            <div>{influencer_suggestions?.map((i:any)=> (<div key={i.handle}>{i.handle} • {i.followers} followers</div>))}</div>
          </div>
        </div>
  
        <div className="mb-4">
          <h4 className="font-medium">Strengths</h4>
          <pre className="whitespace-pre-wrap text-sm bg-slate-50 p-3 rounded">{strengths}</pre>
        </div>
  
        <div className="mb-4">
          <h4 className="font-medium">Weaknesses</h4>
          <pre className="whitespace-pre-wrap text-sm bg-slate-50 p-3 rounded">{weaknesses}</pre>
        </div>
  
        <div className="mb-4">
          <h4 className="font-medium">30/60/90 Day Plan</h4>
          <pre className="whitespace-pre-wrap text-sm bg-slate-50 p-3 rounded">{improvements}</pre>
        </div>
      </div>
    )
  }
  