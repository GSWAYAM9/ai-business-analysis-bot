import '../styles/globals.css';

import Link from 'next/link';

export const metadata = {
  title: 'AI Business Analysis Dashboard',
  description: 'Analyze businesses from a link and get strengths, weaknesses and growth plan.'
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="min-h-screen flex flex-col">
          <header className="bg-white shadow">
            <div className="container mx-auto px-6 py-4 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <img src="/logo.svg" alt="logo" className="w-10 h-10" />
                <h1 className="text-xl font-semibold">AI Business Analysis</h1>
              </div>
              <nav>
                <Link href="/" className="text-slate-600 hover:text-slate-900 px-3">Home</Link>
              </nav>
            </div>
          </header>
          <main className="container mx-auto px-6 py-8 flex-1">
            {children}
          </main>
          <footer className="bg-white border-t">
            <div className="container mx-auto px-6 py-4 text-sm text-slate-500">
              © {new Date().getFullYear()} AI Business Analysis Bot
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}
