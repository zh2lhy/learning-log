# -*- coding: utf-8 -*-
"""把 术语表.txt 渲染成 术语表.md（表格）。双击 更新术语表.bat 即可运行。"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "术语表.txt")
DST = os.path.join(BASE, "术语表.md")

sections = []          # 保持顺序：[(名字, [行...])]
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
    sections[-1][1].append(parts)

out = [
    "# 术语表",
    "",
    "> 这个文件由 `术语表.txt` 自动生成，**别直接改这里**；要加词就改 txt，再双击 `更新术语表.bat`。",
    ">",
    "> 规则：① 只记真见过的词 ②「我的例子」必须自己写 ③ 每周日遮住中文列自测 10 分钟。",
    "",
]
total = 0
for name, rows in sections:
    out += [f"## {name}", "", "| 英文 | 中文 | 我的例子 |", "|---|---|---|"]
    for en, zh, note in rows:
        out.append(f"| {en} | {zh} | {note} |")
        total += 1
    out.append("")

open(DST, "w", encoding="utf-8").write("\n".join(out))
print(f"已生成 {DST}，共 {total} 条")