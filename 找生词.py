# -*- coding: utf-8 -*-
"""从你自己写的 .java 文件里找出「还没进术语表」的英文词。

用法：双击 找生词.bat
结果：在同目录生成 待补词.txt，按出现次数排序。

它**不会**直接改你的术语表 —— 自动加会把 println / args 这种噪音也塞进去，
词表一脏就没人愿意看了。你扫一眼，把真见过的词复制进 术语表.txt 就行。
"""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
GLOSSARY = os.path.join(BASE, "术语表.txt")
OUT = os.path.join(BASE, "待补词.txt")

# Java 关键字/字面量：这些是语法，不是生词，不往词表里塞
KEYWORDS = set("""
abstract assert boolean break byte case catch char class const continue default do
double else enum extends final finally float for goto if implements import instanceof
int interface long native new package private protected public return short static
strictfp super switch synchronized this throw throws transient try void volatile while
true false null var record sealed permits yield
""".split())

# 纯噪音：出现再多次也没必要单独记
NOISE = set("""
main args arg str tmp temp res result ret val obj item data list arr i j k n x y z
equals tostring hashcode
java util demo converter hello system out print println printf
""".split())

CJK = re.compile(r"[\u4e00-\u9fff]")


def words_in(text):
    """把代码里的标识符切成一个一个英文小词：userName -> user, name"""
    out = []
    for ident in re.findall(r"[A-Za-z][A-Za-z0-9_]{2,}", text):
        # camelCase / PascalCase
        parts = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", ident).split()
        # snake_case
        more = []
        for p in parts:
            more.extend(p.split("_"))
        for p in more:
            if len(p) >= 3 and p.isalpha():
                out.append(p.lower())
    return out


def known_words():
    known = set()
    if not os.path.exists(GLOSSARY):
        return known
    for line in open(GLOSSARY, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        first = line.split("|")[0].strip().lower()
        if first:
            known.add(first)
    return known


def main():
    known = known_words()
    counts = {}
    files = []
    for root, dirs, names in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in (".git", ".idea", "out", "target")]
        for name in names:
            if name.endswith(".java"):
                files.append(os.path.join(root, name))

    for path in files:
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for w in words_in(text):
            if w in KEYWORDS or w in NOISE or w in known:
                continue
            counts[w] = counts.get(w, 0) + 1

    rows = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    lines = [
        "# 待补词 —— 从你的 .java 文件里挑出来的，还没进术语表的英文词",
        "# 按出现次数排序。扫一眼，把「真见过、真不认识」的复制进 术语表.txt：",
        "#   英文 | 中文 | （例子先空着，去网页里写）",
        "# 不用全抄：一次 5 个，抄完双击 更新术语表.bat。",
        "",
    ]
    for w, c in rows:
        lines.append(f"{w} |  |    # 出现 {c} 次")
    open(OUT, "w", encoding="utf-8").write("\n".join(lines))
    print(f"扫了 {len(files)} 个 .java 文件，找到 {len(rows)} 个待补词")
    print(f"已生成 {OUT}")


if __name__ == "__main__":
    main()