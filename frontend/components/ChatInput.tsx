"use client";

import { useState } from "react";
import { analyzeBusiness } from "@/lib/api";

type Props = {
  onResult: (data: any) => void;
  onClose?: () => void;
};

export default function ChatInput({ onResult, onClose }: Props) {
  const [message, setMessage] = useState("");
  const [url, setUrl] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async () => {
    setError(null);

    if (!url && !message && !file) {
      setError("Please provide a URL, a question, or upload a document.");
      return;
    }

    try {
      setLoading(true);

      const result = await analyzeBusiness({
        url: url || undefined,
        question: message || undefined,
        file: file || undefined,
      });

      onResult(result);

      // Reset input
      setMessage("");
      setUrl("");
      setFile(null);

      if (onClose) onClose();
    } catch (err) {
      setError("Analysis failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-4">
      {/* Instagram URL */}
      <input
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Instagram URL (optional)"
        className="w-full p-3 rounded-xl bg-white/10 border border-white/20 text-white placeholder-gray-400"
      />

      {/* File Upload */}
      <div className="flex items-center gap-3">
        <input
          type="file"
          accept=".pdf,.doc,.docx,.ppt,.pptx"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="text-sm text-gray-300"
        />

        {file && (
          <span className="text-xs text-green-400">
            {file.name}
          </span>
        )}
      </div>

      {/* Chat-style textarea */}
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask a question or describe what you want to analyze..."
        rows={4}
        className="w-full p-4 rounded-xl bg-white/10 border border-white/20 text-white placeholder-gray-400 resize-none"
      />

      {/* Error */}
      {error && (
        <p className="text-sm text-red-400">{error}</p>
      )}

      {/* Actions */}
      <div className="flex justify-end gap-3">
        {onClose && (
          <button
            onClick={onClose}
            className="text-gray-400 hover:text-white"
            disabled={loading}
          >
            Cancel
          </button>
        )}

        <button
          onClick={handleSubmit}
          disabled={loading}
          className="px-5 py-2 rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 text-white font-semibold disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </div>
    </div>
  );
}
