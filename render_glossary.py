# -*- coding: utf-8 -*-
"""把 术语表.txt 渲染成两个文件：

  术语表.md    —— 给手机/GitHub 看的表格
  术语表.html  —— 给电脑看的：能搜、能遮住中文自测

平时只改 术语表.txt，然后双击 更新术语表.bat。
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "术语表.txt")
MD = os.path.join(BASE, "术语表.md")
HTML = os.path.join(BASE, "术语表.html")

# ---------- 读 txt ----------
sections = []          # [(名字, [[en, zh, note], ...])]
current = "生词本"
for line in open(SRC, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    if line.startswith("#"):
        if "=====" in line:
            current = line.replace("#", "").replace("=", "").strip()
            sections.append((current, []))
        continue
    if not sections:
        sections.append((current, []))
    parts = [p.strip() for p in line.split("|")]
    while len(parts) < 3:
        parts.append("")
    sections[-1][1].append(parts[:3])

total = sum(len(rows) for _, rows in sections)

# ---------- 写 md ----------
out = [
    "# 术语表",
    "",
    "> 这个文件由 `术语表.txt` 自动生成，**别直接改这里**；要加词就改 txt，再双击 `更新术语表.bat`。",
    ">",
    "> 电脑上更推荐看 `术语表.html`：能搜索，能点「遮住中文」自测。",
    ">",
    "> 规则：① 只记真见过的词 ②「我的例子」必须自己写 ③ 每周日遮住中文列自测 10 分钟。",
    "",
]
for name, rows in sections:
    out += [f"## {name}", "", "| 英文 | 中文 | 我的例子 |", "|---|---|---|"]
    for en, zh, note in rows:
        out.append(f"| {en} | {zh} | {note} |")
    out.append("")
open(MD, "w", encoding="utf-8").write("\n".join(out))

# ---------- 写 html ----------
data = [{"name": name, "rows": rows} for name, rows in sections]
payload = json.dumps(data, ensure_ascii=False)

TEMPLATE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>术语表 · Java</title>
<style>
:root{
  --bg:#f5f3ee; --card:#fffdf8; --ink:#24231f; --muted:#8b8679;
  --line:#e3ded2; --accent:#2f6f5e; --amber:#b07a1e;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.65 system-ui,"Segoe UI","Microsoft YaHei",sans-serif}
.mono{font-family:ui-monospace,"Cascadia Code",Consolas,monospace}
.wrap{max-width:900px;margin:0 auto;padding:28px 20px 60px}
header{display:flex;align-items:baseline;gap:14px;margin-bottom:18px}
h1{font-size:24px;margin:0;letter-spacing:.5px}
.sub{font-size:12px;color:var(--muted);letter-spacing:1px}
.sub b{color:var(--accent)}
.bar{position:sticky;top:0;z-index:5;display:flex;gap:10px;
  padding:10px 0;background:linear-gradient(var(--bg) 80%,rgba(245,243,238,0));
  backdrop-filter:blur(6px)}
#q{flex:1;padding:10px 14px;border:1px solid var(--line);border-radius:10px;
  background:var(--card);font-size:14px;color:var(--ink);outline:none}
#q:focus{border-color:var(--accent)}
#quiz{padding:10px 16px;border:1px solid var(--line);border-radius:10px;
  background:var(--card);color:var(--ink);font-size:14px;cursor:pointer;white-space:nowrap}
#quiz:hover{border-color:var(--accent);color:var(--accent)}
h2{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:600;
  color:var(--muted);letter-spacing:1.5px;margin:26px 0 10px}
h2 .tag{padding:2px 8px;border:1px solid var(--line);border-radius:99px;background:var(--card)}
h2 .cnt{font-weight:400;color:#b7b1a2;font-size:12px}
.sec{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.row{display:grid;grid-template-columns:minmax(110px,1.05fr) minmax(80px,.95fr) minmax(0,1.5fr);
  gap:16px;align-items:baseline;padding:11px 16px;border-bottom:1px solid #f0ece2;
  cursor:pointer;transition:background .12s}
.row:last-child{border-bottom:0}
.row:hover{background:#faf7ef}
.en{font-family:ui-monospace,"Cascadia Code",Consolas,monospace;
  font-size:14px;font-weight:600;color:var(--accent)}
.zh{color:var(--ink)}
.eg{color:var(--muted);font-size:13px}
.eg:empty::after{content:"—";color:#d8d2c4}
body.quiz .zh{color:transparent;background:#e9e4d6;border-radius:5px;user-select:none}
body.quiz .row.on .zh{color:var(--ink);background:transparent;user-select:auto}
body.quiz .row{cursor:pointer}
#empty{padding:40px 0;text-align:center;color:var(--muted)}
.foot{margin-top:34px;font-size:12.5px;color:var(--muted);line-height:1.9}
.foot code{background:#eae5d8;padding:1px 5px;border-radius:4px;font-size:12px}
@media (max-width:700px){
  .row{grid-template-columns:1fr;gap:2px;padding:12px 14px}
  .eg{font-size:12px}
  .wrap{padding:20px 14px 50px}
}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>术语表</h1>
    <span class="sub mono">JAVA · GLOSSARY · <b id="count">0</b> 条</span>
  </header>
  <div class="bar">
    <input id="q" placeholder="搜英文或中文，比如 cast / 强转 / 异常" autocomplete="off">
    <button id="quiz">遮住中文</button>
  </div>
  <div id="list"></div>
  <p id="empty" hidden>没有匹配的词。换个关键词，或者点「显示中文」。</p>
  <p class="foot">
    加词改 <code>术语表.txt</code>（一行一个：英文 | 中文 | 我的例子），再双击 <code>更新术语表.bat</code>。<br>
    自测：点「遮住中文」，看英文想中文，想不起来就点那一行翻看；每天 3 分钟，比背单词书管用。
  </p>
</div>
<script>
const DATA = __DATA__;
const list = document.getElementById('list');
const q = document.getElementById('q');
const quiz = document.getElementById('quiz');
const count = document.getElementById('count');
const empty = document.getElementById('empty');

function render() {
  const kw = q.value.trim().toLowerCase();
  list.innerHTML = '';
  let n = 0;
  for (const sec of DATA) {
    const rows = sec.rows.filter(r =>
      !kw || (r[0] + ' ' + r[1] + ' ' + r[2]).toLowerCase().includes(kw));
    if (!rows.length) continue;
    const h = document.createElement('h2');
    h.innerHTML = '<span class="tag">' + sec.name + '</span>' +
      '<span class="cnt">' + rows.length + ' 条</span>';
    list.appendChild(h);
    const box = document.createElement('div');
    box.className = 'sec';
    for (const r of rows) {
      const row = document.createElement('div');
      row.className = 'row';
      const en = document.createElement('div');
      en.className = 'en'; en.textContent = r[0];
      const zh = document.createElement('div');
      zh.className = 'zh'; zh.textContent = r[1] || '—';
      const eg = document.createElement('div');
      eg.className = 'eg'; eg.textContent = r[2] || '';
      row.append(en, zh, eg);
      row.addEventListener('click', () => row.classList.toggle('on'));
      box.appendChild(row);
      n++;
    }
    list.appendChild(box);
  }
  count.textContent = n;
  empty.hidden = n > 0;
}

quiz.addEventListener('click', () => {
  const on = document.body.classList.toggle('quiz');
  quiz.textContent = on ? '显示中文' : '遮住中文';
  if (!on) document.querySelectorAll('.row.on').forEach(r => r.classList.remove('on'));
});

q.addEventListener('input', render);
render();
</script>
</body>
</html>
"""

open(HTML, "w", encoding="utf-8").write(
    TEMPLATE.replace("__DATA__", payload)
)
print(f"已生成 {MD}")
print(f"已生成 {HTML}")
print(f"共 {total} 条")