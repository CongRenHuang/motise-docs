#!/usr/bin/env python3
import os
import sys
import re
import html
import subprocess

# 預設範本 HTML 檔案
DEFAULT_TEMPLATE = 'doc/html/contract-zh-v3-print.html'

# Mermaid 圖表所需的樣式與渲染腳本（透過 CDN 載入 mermaid.js，將 ```mermaid 區塊渲染為 SVG）
MERMAID_CSS = """
    .mermaid {
      text-align: center;
      margin: 2mm 0 4mm 0;
      page-break-inside: avoid;
      break-inside: avoid;
    }
    .mermaid svg {
      max-width: 100% !important;
      height: auto !important;
    }
"""

MERMAID_SCRIPT = """  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({
      startOnLoad: true,
      theme: 'base',
      themeVariables: {
        fontFamily: 'Noto Sans TC, Noto Sans, sans-serif',
        primaryColor: '#eef3f8',
        primaryBorderColor: '#1a3a5c',
        primaryTextColor: '#1a1a1a',
        lineColor: '#1a3a5c'
      }
    });
  </script>
"""

def get_html_skeleton(template_path=None):
    """
    讀取 HTML 模板並切分成前半段與後半段，供注入 markdown 轉換後的 HTML 使用。
    如果模板不存在，則返回一個基礎的、相容該專案 CSS variables 與樣式的 HTML 骨架。
    """
    if template_path and os.path.exists(template_path):
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # 以 page-wrapper 切分
            if '<div class="page-wrapper">' in content:
                head_part, rest = content.split('<div class="page-wrapper">', 1)
                
                # 確保 prefix 中包含 Markdown 特有的 CSS 樣式
                # 如果模板裡沒有 appendix-disclaimer，在此處補上
                if '.appendix-disclaimer' not in head_part:
                    css_inject = """
    .appendix-disclaimer {
      font-size: var(--size-xs);
      color: var(--color-muted);
      margin-top: 5mm;
      font-family: var(--font-sans);
      text-indent: 0 !important;
    }
"""
                    head_part = head_part.replace('</style>', css_inject + '\n  </style>')

                # 確保 prefix 中包含 Mermaid 圖表所需的樣式
                if '.mermaid' not in head_part:
                    head_part = head_part.replace('</style>', MERMAID_CSS + '\n  </style>')

                prefix = head_part + '<div class="page-wrapper">\n<div class="article">\n'
                suffix = '\n</div>\n</div><!-- /page-wrapper -->\n' + MERMAID_SCRIPT + '</body>\n</html>'
                return prefix, suffix
        except Exception as e:
            print(f"Warning: Failed to parse template {template_path}: {e}. Falling back to default skeleton.")

    # 預設骨架（若無模板時使用，內含完整精美的列印與網頁樣式）
    css_content = """
    /* ─── Fonts ─── */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;700&family=Noto+Sans+TC:wght@400;500&display=swap');

    :root {
      --page-width: 210mm;
      --page-height: 297mm;
      --margin-top: 25mm;
      --margin-right: 20mm;
      --margin-bottom: 25mm;
      --margin-left: 25mm;
      --color-text: #1a1a1a;
      --color-muted: #555;
      --color-border: #bbb;
      --color-border-light: #ddd;
      --color-accent: #1a3a5c;
      --font-serif: 'Noto Serif TC', 'STSong', '宋體', Georgia, serif;
      --font-sans: 'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', sans-serif;
      --size-base: 10.5pt;
      --size-sm: 9pt;
      --size-xs: 8pt;
    }

    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: #e8e8e8;
      font-family: var(--font-serif);
      font-size: var(--size-base);
      color: var(--color-text);
      line-height: 1.8;
    }

    .page-wrapper {
      max-width: var(--page-width);
      margin: 32px auto;
      background: #fff;
      box-shadow: 0 4px 32px rgba(0,0,0,.18);
      padding: var(--margin-top) var(--margin-right) var(--margin-bottom) var(--margin-left);
    }

    .print-btn {
      position: fixed;
      top: 20px;
      right: 24px;
      background: var(--color-accent);
      color: #fff;
      border: none;
      padding: 8px 20px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      border-radius: 4px;
      letter-spacing: .04em;
      z-index: 100;
      box-shadow: 0 2px 8px rgba(0,0,0,.25);
    }
    .print-btn:hover { background: #255a8a; }

    .doc-header {
      text-align: center;
      margin-bottom: 10mm;
      padding-bottom: 6mm;
      border-bottom: 2px solid var(--color-accent);
    }
    .doc-header h1 {
      font-size: 16pt;
      font-weight: 700;
      letter-spacing: .12em;
      color: var(--color-accent);
      margin-bottom: 3px;
    }
    .doc-meta {
      font-family: var(--font-sans);
      font-size: var(--size-sm);
      color: var(--color-muted);
      display: flex;
      justify-content: center;
      gap: 32px;
    }

    hr {
      border: none;
      border-top: 1px solid var(--color-border-light);
      margin: 6mm 0;
    }

    .article {
      margin-bottom: 7mm;
    }
    .article h1 {
      text-align: center;
      font-size: 16pt;
      font-weight: 700;
      letter-spacing: .12em;
      color: var(--color-accent);
      margin-bottom: 10mm;
      padding-bottom: 6mm;
      border-bottom: 2px solid var(--color-accent);
    }
    .article h2 {
      font-family: var(--font-sans);
      font-size: 10pt;
      font-weight: 700;
      color: var(--color-accent);
      letter-spacing: .1em;
      border-left: 3px solid var(--color-accent);
      padding-left: 6px;
      margin-bottom: 4mm;
      page-break-after: avoid;
    }
    .article h3 {
      font-family: var(--font-sans);
      font-size: var(--size-sm);
      font-weight: 700;
      color: var(--color-accent);
      margin-top: 6mm;
      margin-bottom: 2mm;
    }
    .article p {
      font-size: var(--size-base);
      line-height: 1.85;
      margin-bottom: 4mm;
    }
    .clause {
      margin-bottom: 2.5mm;
    }
    .clause-num {
      font-weight: 500;
      color: var(--color-accent);
      margin-right: 4px;
    }

    ul, ol {
      margin-left: 2em;
      margin-bottom: 4mm;
      font-size: var(--size-sm);
      color: var(--color-muted);
      line-height: 1.75;
    }

    blockquote {
      margin: 3mm 0 4mm;
      padding: 3mm 6mm;
      border-left: 3px solid var(--color-border);
      background: #f9f9f9;
      font-family: var(--font-sans);
      font-size: var(--size-xs);
      color: var(--color-muted);
      line-height: 1.7;
    }

    pre {
      background: #f4f4f4;
      border: 1px solid var(--color-border-light);
      border-left: 3px solid var(--color-accent);
      padding: 4mm 6mm;
      margin: 2mm 0 4mm 0;
      font-family: 'Courier New', Courier, monospace;
      font-size: var(--size-sm);
      overflow-x: auto;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-family: var(--font-sans);
      font-size: var(--size-sm);
      margin: 2mm 0 4mm;
    }
    table th {
      background: var(--color-accent);
      color: #fff;
      font-weight: 600;
      padding: 4px 8px;
      text-align: left;
      letter-spacing: .04em;
    }
    table td {
      padding: 4px 8px;
      border-bottom: 1px solid var(--color-border-light);
      vertical-align: top;
      line-height: 1.6;
    }
    table tr:nth-child(even) td { background: #f7f8fa; }

    .formula {
      font-family: 'Courier New', Courier, monospace;
      font-size: var(--size-sm);
      background: #f4f4f4;
      border: 1px solid var(--color-border-light);
      border-left: 3px solid var(--color-accent);
      padding: 4mm 6mm;
      margin: 2mm 0 3mm 2em;
      line-height: 1.7;
      page-break-inside: avoid;
      white-space: pre-wrap;
    }

    .sig-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10mm;
      margin-top: 6mm;
    }
    .sig-block {
      border-top: 1.5px solid var(--color-accent);
      padding-top: 4mm;
    }
    .sig-block h4 {
      font-family: var(--font-sans);
      font-size: 9.5pt;
      font-weight: 700;
      color: var(--color-accent);
      margin-bottom: 4mm;
    }
    .sig-field {
      font-family: var(--font-sans);
      font-size: var(--size-sm);
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 2px;
      margin-bottom: 5mm;
      color: var(--color-muted);
    }
    .sig-field span { white-space: normal; }
    .sig-field span:first-child {
      font-weight: 700;
      color: var(--color-text);
    }
    .sig-line {
      flex: 1;
      border-bottom: 1px solid var(--color-border);
      min-width: 40px;
      height: 20px;
    }

    .appendix-disclaimer {
      font-size: var(--size-xs);
      color: var(--color-muted);
      margin-top: 5mm;
      font-family: var(--font-sans);
      text-indent: 0 !important;
    }

    /* Fix table column wrapping */
    .criteria-table { table-layout: fixed !important; width: 100% !important; }
    .criteria-table th:nth-child(1), .criteria-table td:nth-child(1) { width: 10% !important; white-space: nowrap !important; }
    .criteria-table th:nth-child(2), .criteria-table td:nth-child(2) { width: 30% !important; }
    .criteria-table th:nth-child(3), .criteria-table td:nth-child(3) { width: 60% !important; }

    .module-table { table-layout: fixed !important; width: 100% !important; }
    .module-table th:nth-child(1), .module-table td:nth-child(1) { width: 10% !important; white-space: nowrap !important; }
    .module-table th:nth-child(2), .module-table td:nth-child(2) { width: 25% !important; }
    .module-table th:nth-child(3), .module-table td:nth-child(3) { width: 45% !important; }
    .module-table th:nth-child(4), .module-table td:nth-child(4) { width: 20% !important; white-space: nowrap !important; }

    .tech-table { table-layout: fixed !important; width: 100% !important; }
    .tech-table th:nth-child(1), .tech-table td:nth-child(1) { width: 20% !important; white-space: nowrap !important; }
    .tech-table th:nth-child(2), .tech-table td:nth-child(2) { width: 25% !important; }
    .tech-table th:nth-child(3), .tech-table td:nth-child(3) { width: 55% !important; }

    .resource-table { table-layout: fixed !important; width: 100% !important; }
    .resource-table th:nth-child(1), .resource-table td:nth-child(1) { width: 45% !important; }
    .resource-table th:nth-child(2), .resource-table td:nth-child(2) { width: 55% !important; }
""" + MERMAID_CSS + """
    @media print {
      @page { size: A4; margin: 25mm 20mm 25mm 25mm; }
      @page :first { margin-top: 20mm; }
      body { background: #fff; font-size: 10pt; color: #000; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
      .page-wrapper { max-width: none; margin: 0; padding: 0; box-shadow: none; }
      .print-btn { display: none !important; }
      .pb-before { page-break-before: always; break-before: page; margin-top: 0; }
      .article h2 { page-break-after: avoid; break-after: avoid; }
      .party-block, .appendix-section, .payment-scenario, .sig-grid, .formula, .signature-section { page-break-inside: avoid; break-inside: avoid; }
      thead { display: table-header-group; }
      tfoot { display: table-footer-group; }
      tr { page-break-inside: avoid; break-inside: avoid; }
      p { orphans: 3; widows: 3; }
      a { text-decoration: none; color: inherit; }
      .parties { display: grid; }
    }
    """
    
    prefix = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Agreement Document</title>
  <style>
    {css_content}
  </style>
</head>
<body>
  <button class="print-btn" onclick="window.print()">Print / Export PDF</button>
  <div class="page-wrapper">
    <div class="article">
"""
    suffix = """
    </div>
  </div>
""" + MERMAID_SCRIPT + """</body>
</html>"""
    return prefix, suffix

def md_to_html_body(md_text):
    """
    將 Markdown 轉換成 HTML Body。
    優先使用 Python 的 markdown 庫，若沒有則調用 npx marked。
    """
    try:
        import markdown
        # 支援 tables、fenced code、gfm 換行
        html = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'nl2br'])
        return html
    except ImportError:
        # Fallback to npx marked
        temp_file = 'temp_md_converter.md'
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(md_text)
            res = subprocess.run(['npx', '-y', 'marked@latest', '--gfm', temp_file], capture_output=True, text=True, check=True)
            return res.stdout
        except Exception as e:
            print(f"Error executing npx marked fallback: {e}")
            sys.exit(1)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

def post_process_html(html_body):
    """
    對生成的 HTML 進行後處理，以符合合約排版：
    1. 表格欄寬類別注入。
    2. 自動套用 .clause 樣式於類似 3.1、5.2 的條款。
    3. 自動套用 .appendix-disclaimer 於底部的免責宣告。
    4. 將 ```mermaid 區塊轉換為 <div class="mermaid"> 供 Mermaid.js 渲染為 SVG。
    """
    # 0. 轉換 mermaid 程式碼區塊（marked / python-markdown 皆可能輸出 language-mermaid 或 mermaid class，
    #    且內容會被 HTML escape，需先 unescape 還原原始語法）
    def mermaid_replacer(match):
        code = html.unescape(match.group(1))
        return f'<div class="mermaid">\n{code}\n</div>'

    html_body = re.sub(
        r'<pre><code class="(?:language-|lang-)?mermaid">(.*?)</code></pre>',
        mermaid_replacer,
        html_body,
        flags=re.DOTALL
    )

    # 1. 注入表格類別
    html_body = re.sub(r'<table>(\s*<thead>\s*<tr>\s*<th>#</th>)', r'<table class="criteria-table">\1', html_body)
    html_body = re.sub(r'<table>(\s*<thead>\s*<tr>\s*<th>No\.</th>\s*<th>Module Name</th>)', r'<table class="module-table">\1', html_body)
    html_body = re.sub(r'<table>(\s*<thead>\s*<tr>\s*<th>Technology</th>)', r'<table class="tech-table">\1', html_body)
    html_body = re.sub(r'<table>(\s*<thead>\s*<tr>\s*<th>Item</th>\s*<th>Delivery Method</th>)', r'<table class="resource-table">\1', html_body)

    # 2. 轉換手寫數字條款為 .clause 元件
    clause_pattern = r'(?s)<p>(\d+\.\d+)\s*(.*?)</p>'
    def clause_replacer(match):
        num = match.group(1)
        content = match.group(2)
        return f'<div class="clause"><span class="clause-num">{num}</span>{content}</div>'
    html_body = re.sub(clause_pattern, clause_replacer, html_body)

    # 3. 處理免責聲明小字 (例如最後一段的 *Appendix A has the same...* 轉成 <em>...</em> )
    disclaimer_pattern = r'(?s)<p>(<em>(?:Appendix|本附件).*?</em>)</p>'
    html_body = re.sub(disclaimer_pattern, r'<p class="appendix-disclaimer">\1</p>', html_body)

    # 4. 把雙方簽署的 Dropbox Sign 時間戳記註解括弧稍微整理成精美 span
    html_body = html_body.replace('（由 Dropbox Sign 系統自動記錄）', '<span style="font-size:var(--size-xs);color:#aaa;font-style:italic;">(由 Dropbox Sign 系統自動記錄)</span>')
    html_body = html_body.replace('(由 Dropbox Sign 系統自動記錄)', '<span style="font-size:var(--size-xs);color:#aaa;font-style:italic;">(由 Dropbox Sign 系統自動記錄)</span>')

    return html_body

def main():
    if len(sys.argv) < 3:
        print("Usage: python Markdown2HTML.py <input_md_file> <output_html_file> [template_html_file]")
        print("Example: python Markdown2HTML.py doc/markdown/zh/appendix-d.md doc/html/appendix-d-zh-print.html")
        sys.exit(1)

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    template_file = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_TEMPLATE

    if not os.path.exists(in_file):
        print(f"Error: Input file '{in_file}' does not exist.")
        sys.exit(1)

    print(f"Reading {in_file}...")
    with open(in_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    print("Converting Markdown to HTML...")
    html_body = md_to_html_body(md_text)

    print("Post-processing HTML elements...")
    html_body = post_process_html(html_body)

    print("Applying HTML template...")
    prefix, suffix = get_html_skeleton(template_file)
    
    final_html = prefix + html_body + suffix

    # 確保輸出目錄存在
    out_dir = os.path.dirname(out_file)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    print(f"Saving to {out_file}...")
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print("Successfully completed Markdown to HTML conversion!")

if __name__ == '__main__':
    main()
