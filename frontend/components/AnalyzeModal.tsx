"use client";

import { motion, AnimatePresence } from "framer-motion";
import ChatInput from "@/components/ChatInput";

type Props = {
  open: boolean;
  onClose: () => void;
  onResult: (data: any) => void;
};

export default function AnalyzeModal({ open, onClose, onResult }: Props) {
  if (!open) return null;

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          className="fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-sm"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        >
          <motion.div
            initial={{ scale: 0.95, y: 40 }}
            animate={{ scale: 1, y: 0 }}
            exit={{ scale: 0.95, y: 40 }}
            transition={{ duration: 0.25 }}
            className="w-full max-w-xl bg-[#12091f] border border-white/10 rounded-3xl p-6 text-white shadow-2xl"
          >
            {/* Header */}
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-2xl font-bold">+ Analyze Business</h2>
              <button
                onClick={onClose}
                className="text-gray-400 hover:text-white text-xl"
              >
                ×
              </button>
            </div>

            {/* Chat Input */}
            <ChatInput
              onResult={onResult}
              onClose={onClose}
            />
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
