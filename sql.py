#severjs
import express from "express";
import cors from "cors";
import mysql from "mysql2/promise";

const app = express();
app.use(cors());

Kết nối MySQL
const db = await mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "comicsdb",
});

// Lấy danh sách chapter của truyện
app.get("/api/comics/:comicId/chapters", async (req, res) => {
  const { comicId } = req.params;

  try {
    const [rows] = await db.execute(
      "SELECT chapter_number FROM chapters WHERE comic_id = ? ORDER BY chapter_number ASC",
      [comicId]
    );
    const chapters = rows.map(row => row.chapter_number);
    res.json(chapters);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Lỗi khi lấy danh sách chương" });
  }
});

//  Lấy ảnh trong 1 chapter
app.get("/api/comics/:comicId/chapters/:chapterId", async (req, res) => {
  const { comicId, chapterId } = req.params;

  try {
    const [chapterRows] = await db.execute(
      "SELECT id FROM chapters WHERE comic_id=? AND chapter_number=?",
      [comicId, chapterId]
    );

    if (chapterRows.length === 0)
      return res.status(404).json({ error: "Không tìm thấy chapter" });

    const chapterIdDb = chapterRows[0].id;

    const [imageRows] = await db.execute(
      "SELECT image_url FROM chapter_images WHERE chapter_id=?",
      [chapterIdDb]
    );

    res.json({ images: imageRows.map(r => r.image_url) });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Lỗi server" });
  }
});

// Khởi động server
app.listen(3000, () => console.log("✅ Backend chạy tại http://localhost:3000"));



{
  "name": "backend",
  "version": "1.0.0",
  "description": "Backend server for Comic Website",
  "type": "module",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "cors": "^2.8.5",
    "express": "^5.1.0",
    "mysql2": "^3.9.0"
  }
}



import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App.jsx";
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);



import { Routes, Route } from "react-router-dom";
import Layout from "./components/layout/Layout";
import HomePage from "./pages/HomePage";
import ComicPage from "./pages/ComicPage";
import ChapterPage from "./pages/ChapterPage";

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/comic/:comicId" element={<ComicPage />} />
        <Route path="/comic/:comicId/chapter/:chapterId" element={<ChapterPage />} />
      </Routes>
    </Layout>
  );
}

export default App;



import { Link, useParams } from "react-router-dom";
import { useEffect, useState } from "react";

export default function ComicPage() {
  const { comicId } = useParams();
  const [chapters, setChapters] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:3000/api/comics/${comicId}/chapters`)
      .then(res => res.json())
      .then(data => setChapters(data))
      .catch(console.error);
  }, [comicId]);

  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Truyện {comicId}</h1>
      <p className="mb-6">Hiện mô tả truyện ở đây</p>

      <h2 className="text-xl font-semibold mb-3">Danh sách chương</h2>
      <ul className="list-disc pl-6">
        {chapters.map((ch) => (
          <li key={ch}>
            <Link
              to={`/comic/${comicId}/chapter/${ch}`}
              className="text-blue-600 hover:underline"
            >
              Chapter {ch}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
