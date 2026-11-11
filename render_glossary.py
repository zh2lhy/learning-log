# -*- coding: utf-8 -*-
"""把 术语表.txt 渲染成两个文件：

  术语表.md    —— 给手机/GitHub 看的表格
  术语表.html  —— 给电脑看的：能搜、能遮住中文自测、能直接写「我的例子」

平时只改 术语表.txt 加新词，然后双击 更新术语表.bat。
「我的例子」直接在网页里写，自动存在浏览器里，不会被重新生成冲掉。
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
    "> 电脑上更推荐看 `术语表.html`：能搜索、能遮住中文自测、能直接写「我的例子」。",
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
  --line:#e3ded2; --accent:#2f6f5e; --amber:#b07a1e; --soft:#eae5d8;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.65 system-ui,"Segoe UI","Microsoft YaHei",sans-serif}
.mono{font-family:ui-monospace,"Cascadia Code",Consolas,monospace}
.wrap{max-width:900px;margin:0 auto;padding:28px 20px 60px}
header{display:flex;align-items:baseline;gap:14px;margin-bottom:14px;flex-wrap:wrap}
h1{font-size:24px;margin:0;letter-spacing:.5px}
.sub{font-size:12px;color:var(--muted);letter-spacing:1px}
.sub b{color:var(--accent)}
.tabs{display:flex;gap:8px;margin-bottom:6px}
.tabs button{padding:7px 16px;border:1px solid var(--line);border-radius:99px;
  background:var(--card);color:var(--muted);font-size:13.5px;cursor:pointer}
.tabs button.on{background:var(--accent);border-color:var(--accent);color:#fff}
.bar{position:sticky;top:0;z-index:5;display:flex;gap:10px;
  padding:10px 0;background:linear-gradient(var(--bg) 80%,rgba(245,243,238,0));
  backdrop-filter:blur(6px)}
#q,#eq{flex:1;padding:10px 14px;border:1px solid var(--line);border-radius:10px;
  background:var(--card);font-size:14px;color:var(--ink);outline:none}
#q:focus,#eq:focus{border-color:var(--accent)}
#quiz,#onlyEmpty,#exportEg{padding:10px 16px;border:1px solid var(--line);border-radius:10px;
  background:var(--card);color:var(--ink);font-size:14px;cursor:pointer;white-space:nowrap}
#quiz:hover,#onlyEmpty:hover,#exportEg:hover{border-color:var(--accent);color:var(--accent)}
#onlyEmpty.on{background:var(--accent);border-color:var(--accent);color:#fff}
h2{display:flex;align-items:center;gap:10px;font-size:13px;font-weight:600;
  color:var(--muted);letter-spacing:1.5px;margin:26px 0 10px}
h2 .tag{padding:2px 8px;border:1px solid var(--line);border-radius:99px;background:var(--card)}
h2 .cnt{font-weight:400;color:#b7b1a2;font-size:12px}
.sec{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.row{display:grid;grid-template-columns:minmax(110px,1fr) minmax(80px,.85fr) minmax(0,1.7fr);
  gap:14px;align-items:start;padding:10px 16px;border-bottom:1px solid #f0ece2;
  cursor:pointer;transition:background .12s}
.row:last-child{border-bottom:0}
.row:hover{background:#faf7ef}
.en{font-family:ui-monospace,"Cascadia Code",Consolas,monospace;
  font-size:14px;font-weight:600;color:var(--accent);padding-top:3px}
.zh{color:var(--ink);padding-top:2px}
textarea.eg{width:100%;border:1px dashed transparent;border-radius:8px;background:transparent;
  color:var(--muted);font:13px/1.6 system-ui,"Segoe UI","Microsoft YaHei",sans-serif;
  padding:3px 6px;resize:none;overflow:hidden;min-height:26px;outline:none}
textarea.eg:hover{border-color:var(--line)}
textarea.eg:focus{border-color:var(--accent);background:#fff;color:var(--ink)}
textarea.eg::placeholder{color:#c9c2b2}
body.quiz .zh{color:transparent;background:#e9e4d6;border-radius:5px;user-select:none}
body.quiz textarea.eg{color:transparent}
body.quiz .row.on .zh{color:var(--ink);background:transparent}
body.quiz .row.on textarea.eg{color:var(--muted)}
#empty{padding:40px 0;text-align:center;color:var(--muted)}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;
  padding:14px 18px;margin-bottom:10px}
.card .head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:8px}
.card .w{font-family:ui-monospace,"Cascadia Code",Consolas,monospace;
  font-size:16px;font-weight:700;color:var(--accent)}
.card .m{color:var(--ink);font-size:14px}
.card .done{margin-left:auto;font-size:12px;color:var(--accent)}
.card textarea{width:100%;border:1px solid var(--line);border-radius:10px;background:#fff;
  color:var(--ink);font:14px/1.7 system-ui,"Segoe UI","Microsoft YaHei",sans-serif;
  padding:9px 12px;resize:vertical;min-height:44px;outline:none}
.card textarea:focus{border-color:var(--accent)}
.tip{font-size:12.5px;color:var(--muted);margin:12px 0 0}
.foot{margin-top:34px;font-size:12.5px;color:var(--muted);line-height:1.9}
.foot code{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:12px}
@media (max-width:700px){
  .row{grid-template-columns:1fr;gap:2px;padding:12px 14px}
  .wrap{padding:20px 14px 50px}
}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>术语表</h1>
    <span class="sub mono">JAVA · <b id="count">0</b> 条 · 例子 <b id="egN">0</b></span>
  </header>

  <div class="tabs">
    <button id="tabList" class="on">词表 · 背</button>
    <button id="tabEg">实例本 · 写</button>
  </div>

  <section id="viewList">
    <div class="bar">
      <input id="q" placeholder="搜英文或中文，比如 cast / 强转 / 异常" autocomplete="off">
      <button id="quiz">遮住中文</button>
    </div>
    <div id="list"></div>
    <p id="empty" hidden>没有匹配的词。换个关键词，或者点「显示中文」。</p>
    <p class="tip">
      左边英文、中间中文、右边「我的例子」——<b>点一下右边就能直接打字</b>，边打边存。
      遮住中文时例子也会藏起来，想不起来就点那一行翻看。
    </p>
  </section>

  <section id="viewEg" hidden>
    <div class="bar">
      <input id="eq" placeholder="做题时想到哪个词，就在这儿搜" autocomplete="off">
      <button id="onlyEmpty">只看还没写的</button>
      <button id="exportEg">导出例子</button>
    </div>
    <div id="egList"></div>
    <p class="tip">
      例子不用写完整句子，写「你在哪儿见过它」就够：<code>cast = 把 double 硬塞进 int</code>。
      写不出来就先空着——空着不丢人，硬编才丢人。写完自动存在这台电脑的浏览器里，不会因为重新生成而丢。
    </p>
  </section>

  <p class="foot">
    加词改 <code>术语表.txt</code>（一行一个：英文 | 中文 | 我的例子），再双击 <code>更新术语表.bat</code>。<br>
    自测：点「遮住中文」，看英文想中文；每天 3 分钟，比背单词书管用。
  </p>
</div>
<script>
const DATA = __DATA__;
const KEY = 'java.glossary.eg.v1';
const st = (() => { try { return JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { return {}; } })();

const el = id => document.getElementById(id);
const list = el('list'), egList = el('egList');
const q = el('q'), quiz = el('quiz'), count = el('count'), egN = el('egN');
const empty = el('empty'), eq = el('eq'), onlyEmpty = el('onlyEmpty');

let saveTimer = 0;
function save() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {}
  }, 250);
  const n = Object.keys(st).filter(k => st[k]).length;
  egN.textContent = n;
}

function egOf(en, fallback) {
  return Object.prototype.hasOwnProperty.call(st, en) ? st[en] : (fallback || '');
}

function grow(t) {
  t.style.height = 'auto';
  t.style.height = Math.max(26, t.scrollHeight) + 'px';
}

function bindEg(t, en) {
  t.value = egOf(en, t.dataset.fb || '');
  grow(t);
  t.addEventListener('input', () => {
    const v = t.value.trim();
    if (v) st[en] = v; else delete st[en];
    grow(t);
    save();
    document.querySelectorAll('textarea[data-en="' + CSS.escape(en) + '"]').forEach(o => {
      if (o !== t) { o.value = t.value; grow(o); }
    });
    const nm = document.querySelector('.card[data-en="' + CSS.escape(en) + '"] .done');
    if (nm) nm.textContent = v ? '✓ 写过了' : '';
  });
  t.addEventListener('click', e => e.stopPropagation());
}

function renderList() {
  const kw = q.value.trim().toLowerCase();
  list.innerHTML = '';
  let n = 0;
  for (const sec of DATA) {
    const rows = sec.rows.filter(r =>
      !kw || (r[0] + ' ' + r[1] + ' ' + r[2] + ' ' + egOf(r[0])).toLowerCase().includes(kw));
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
      const eg = document.createElement('textarea');
      eg.className = 'eg mono'; eg.rows = 1; eg.dataset.en = r[0]; eg.dataset.fb = r[2] || '';
      eg.placeholder = '点这儿写你的例子…';
      bindEg(eg, r[0]);
      row.append(en, zh, eg);
      row.addEventListener('click', () => row.classList.toggle('on'));
      box.appendChild(row);
      n++;
    }
    list.appendChild(box);
  }
  count.textContent = DATA.reduce((a, s) => a + s.rows.length, 0);
  egN.textContent = Object.keys(st).filter(k => st[k]).length;
  empty.hidden = n > 0;
}

function renderEg() {
  const kw = eq.value.trim().toLowerCase();
  const only = onlyEmpty.classList.contains('on');
  egList.innerHTML = '';
  let n = 0;
  for (const sec of DATA) {
    const rows = sec.rows.filter(r => {
      if (kw && !(r[0] + ' ' + r[1]).toLowerCase().includes(kw)) return false;
      if (only && egOf(r[0])) return false;
      return true;
    });
    if (!rows.length) continue;
    const h = document.createElement('h2');
    h.innerHTML = '<span class="tag">' + sec.name + '</span><span class="cnt">' + rows.length + ' 条</span>';
    egList.appendChild(h);
    for (const r of rows) {
      const card = document.createElement('div');
      card.className = 'card'; card.dataset.en = r[0];
      const head = document.createElement('div');
      head.className = 'head';
      head.innerHTML = '<span class="w">' + r[0] + '</span><span class="m">' +
        (r[1] || '') + '</span><span class="done">' + (egOf(r[0]) ? '✓ 写过了' : '') + '</span>';
      const ta = document.createElement('textarea');
      ta.rows = 2; ta.dataset.en = r[0]; ta.dataset.fb = r[2] || '';
      ta.placeholder = '写一句你自己的：在哪儿见过 / 它干了什么';
      bindEg(ta, r[0]);
      card.append(head, ta);
      egList.appendChild(card);
      n++;
    }
  }
  if (!n) {
    const p = document.createElement('p');
    p.id = 'empty'; p.textContent = '都写完了，或者没搜到。';
    egList.appendChild(p);
  }
}

quiz.addEventListener('click', () => {
  const on = document.body.classList.toggle('quiz');
  quiz.textContent = on ? '显示中文' : '遮住中文';
  if (!on) document.querySelectorAll('.row.on').forEach(r => r.classList.remove('on'));
});

q.addEventListener('input', renderList);
eq.addEventListener('input', renderEg);
onlyEmpty.addEventListener('click', () => {
  onlyEmpty.classList.toggle('on');
  renderEg();
});

el('tabList').addEventListener('click', () => {
  el('tabList').classList.add('on'); el('tabEg').classList.remove('on');
  el('viewList').hidden = false; el('viewEg').hidden = true;
});
el('tabEg').addEventListener('click', () => {
  el('tabEg').classList.add('on'); el('tabList').classList.remove('on');
  el('viewList').hidden = true; el('viewEg').hidden = false;
  renderEg();
});

el('exportEg').addEventListener('click', () => {
  const lines = [];
  for (const sec of DATA) for (const r of sec.rows) {
    const v = egOf(r[0]);
    if (v) lines.push(r[0] + ' | ' + (r[1] || '') + ' | ' + v.replace(/\\s+/g, ' ').trim());
  }
  const blob = new Blob([lines.join('\\n') + '\\n'], {type: 'text/plain;charset=utf-8'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = '例子-' + new Date().toISOString().slice(0, 10) + '.txt';
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
});

renderList();
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