export default function Header() {
    return (
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-3">
          <img src="/logo.svg" alt="logo" className="w-8 h-8" />
          <div>
            <div className="text-lg font-semibold">AI Business Analysis</div>
            <div className="text-xs text-slate-500">Analyze links, get meaningful insights</div>
          </div>
        </div>
      </div>
    );
  }
  