"use client";

import { motion } from "framer-motion";

export default function ResultCard({ result }: { result: any }) {
  if (!result) return null;

  // ✅ FIXED: correct data path
  const scraped = result.scraped_data?.instagram || {};
  const ai = result.analysis || {};

  // ✅ FIXED: robust detection
  const hasInstagram =
    scraped &&
    Object.keys(scraped).length > 0 &&
    (scraped.username || scraped.fullname);

  return (
    <motion.div
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="w-full max-w-4xl mt-16 mx-auto rounded-3xl overflow-hidden
                 shadow-2xl border border-white/10
                 bg-gradient-to-br from-[#2a1455]/60 to-black/60
                 backdrop-blur-xl text-white"
    >
      {/* ================= PROFILE SECTION ================= */}
      {hasInstagram && (
        <div className="relative p-10 bg-gradient-to-r from-purple-800/40 to-purple-500/20 border-b border-white/10">
          <div className="flex items-center gap-6">
            <img
              src={scraped.profile_pic || "/placeholder-user.png"}
              className="w-24 h-24 rounded-full border-4 border-white/30 bg-black/40 object-cover"
              onError={(e) =>
                ((e.target as HTMLImageElement).src = "/placeholder-user.png")
              }
            />

            <div>
              <h2 className="text-3xl font-bold text-white">
                {scraped.fullname || scraped.username}
              </h2>
              {scraped.username && (
                <p className="text-purple-300 text-lg">
                  @{scraped.username}
                </p>
              )}
            </div>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-6 mt-10">
            <AnimatedStat label="Followers" value={scraped.followers} />
            <AnimatedStat label="Following" value={scraped.following} />
            <AnimatedStat label="Posts" value={scraped.posts_count} />
          </div>
        </div>
      )}

      {/* ================= AI ANALYSIS ================= */}
      <div className="p-10 space-y-8">
        <Section title="Business Summary" body={ai.summary} />
        <Section title="Strengths" body={ai.strengths} />
        <Section title="Weaknesses" body={ai.weaknesses} />
        <Section title="Recommended Improvements" body={ai.improvements} />
      </div>
    </motion.div>
  );
}

/* ================= SUB COMPONENTS ================= */

function Section({ title, body }: { title: string; body?: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.4 }}
      className="bg-white/5 border border-white/10 rounded-2xl p-6 shadow-xl"
    >
      <h3 className="text-2xl font-semibold mb-4 text-purple-300">
        {title}
      </h3>

      <p className="whitespace-pre-line text-gray-200 leading-relaxed text-lg">
        {body?.trim()
          ? body
          : "AI analysis will appear here after processing your input."}
      </p>
    </motion.div>
  );
}

function AnimatedStat({
  label,
  value,
}: {
  label: string;
  value: number | undefined;
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: 0.4 }}
      className="text-center bg-white/10 border border-white/20
                 p-6 rounded-2xl shadow-lg"
    >
      <div className="text-3xl font-extrabold text-white">
        {typeof value === "number" ? value.toLocaleString() : "-"}
      </div>
      <div className="text-sm text-gray-300 mt-1 tracking-wide">
        {label}
      </div>
    </motion.div>
  );
}
