export async function analyzeBusiness(data: {
  file?: File;
  url?: string;
  question?: string;
}) {
  const formData = new FormData();

  if (data.file) formData.append("file", data.file);
  if (data.url) formData.append("url", data.url);
  if (data.question) formData.append("question", data.question);

  const res = await fetch("http://127.0.0.1:8000/api/scrape/instagram", {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Analysis failed");
  }

  return res.json();
}
