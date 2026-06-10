import os
import subprocess
import re

html_template = 'doc/html/contract-zh-v3-print.html'
with open(html_template, 'r', encoding='utf-8') as f:
    content = f.read()

# Split around page-wrapper
head_part, rest = content.split('<div class="page-wrapper">', 1)
prefix = head_part + '<div class="page-wrapper">\n<div class="article">\n'
suffix = '\n</div>\n</div><!-- /page-wrapper -->\n</body>\n</html>'

# Add some global CSS for markdown tags to match the design
css_inject = """
    /* Markdown Styles */
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
    .article h3 {
      font-family: var(--font-sans);
      font-size: var(--size-sm);
      font-weight: 700;
      color: var(--color-accent);
      margin-top: 6mm;
      margin-bottom: 2mm;
    }
    .article p {
      text-indent: 0;
      margin-bottom: 4mm;
    }
    .article ul, .article ol {
      margin-left: 2em;
      margin-bottom: 4mm;
      font-size: var(--size-sm);
      color: var(--color-muted);
      line-height: 1.75;
    }
    .article blockquote {
      margin: 3mm 0 4mm;
      padding: 3mm 6mm;
      border-left: 3px solid var(--color-border);
      background: #f9f9f9;
      font-family: var(--font-sans);
      font-size: var(--size-xs);
      color: var(--color-muted);
      line-height: 1.7;
    }
    .article pre {
      background: #f4f4f4;
      border: 1px solid var(--color-border-light);
      border-left: 3px solid var(--color-accent);
      padding: 4mm 6mm;
      margin: 2mm 0 4mm 0;
      font-family: 'Courier New', Courier, monospace;
      font-size: var(--size-sm);
      overflow-x: auto;
    }
    /* Fix table column wrapping */
    .criteria-table {
      table-layout: fixed !important;
      width: 100% !important;
    }
    .criteria-table th:nth-child(1),
    .criteria-table td:nth-child(1) {
      width: 10% !important;
      white-space: nowrap !important;
    }
    .criteria-table th:nth-child(2),
    .criteria-table td:nth-child(2) {
      width: 30% !important;
    }
    .criteria-table th:nth-child(3),
    .criteria-table td:nth-child(3) {
      width: 60% !important;
    }
    /* A-2 Module Table CSS */
    .module-table {
      table-layout: fixed !important;
      width: 100% !important;
    }
    .module-table th:nth-child(1),
    .module-table td:nth-child(1) {
      width: 10% !important;
      white-space: nowrap !important;
    }
    .module-table th:nth-child(2),
    .module-table td:nth-child(2) {
      width: 25% !important;
    }
    .module-table th:nth-child(3),
    .module-table td:nth-child(3) {
      width: 45% !important; /* Limit Description column width */
    }
    .module-table th:nth-child(4),
    .module-table td:nth-child(4) {
      width: 20% !important;
      white-space: nowrap !important; /* Avoid wrapping iOS · Android */
    }
    /* A-5-2 Tech Table CSS */
    .tech-table {
      table-layout: fixed !important;
      width: 100% !important;
    }
    .tech-table th:nth-child(1),
    .tech-table td:nth-child(1) {
      width: 20% !important;
      white-space: nowrap !important;
    }
    .tech-table th:nth-child(2),
    .tech-table td:nth-child(2) {
      width: 25% !important;
    }
    .tech-table th:nth-child(3),
    .tech-table td:nth-child(3) {
      width: 55% !important; /* Limit Rationale column width */
    }
    /* A-6 Resource Table CSS */
    .resource-table {
      table-layout: fixed !important;
      width: 100% !important;
    }
    .resource-table th:nth-child(1),
    .resource-table td:nth-child(1) {
      width: 45% !important; /* Increase Item column width to prevent wrapping */
    }
    .resource-table th:nth-child(2),
    .resource-table td:nth-child(2) {
      width: 55% !important; /* Decrease Delivery Method column width */
    }
"""

prefix = prefix.replace('</style>', css_inject + '</style>')

files = [
    ('doc/markdown/en/appendix-a-en.md', 'doc/html/appendix-a-en-print.html'),
    ('doc/markdown/en/appendix-b-en.md', 'doc/html/appendix-b-en-print.html'),
    ('doc/markdown/en/appendix-c-en.md', 'doc/html/appendix-c-en-print.html'),
]

for in_file, out_file in files:
    print(f"Processing {in_file}...")
    with open(in_file, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    with open('temp.md', 'w', encoding='utf-8') as f:
        f.write(md_text)
    
    res = subprocess.run(['npx', '-y', 'marked@latest', '--gfm', 'temp.md'], capture_output=True, text=True)
    html_body = res.stdout
    
    # Auto-add class="criteria-table" to tables that start with "#" header to apply custom column widths
    html_body = re.sub(
        r'<table>(\s*<thead>\s*<tr>\s*<th>#</th>)',
        r'<table class="criteria-table">\1',
        html_body
    )
    # Auto-add class="module-table" to tables that start with "No." and "Module Name" headers
    html_body = re.sub(
        r'<table>(\s*<thead>\s*<tr>\s*<th>No\.</th>\s*<th>Module Name</th>)',
        r'<table class="module-table">\1',
        html_body
    )
    # Auto-add class="tech-table" to tables that start with "Technology" header
    html_body = re.sub(
        r'<table>(\s*<thead>\s*<tr>\s*<th>Technology</th>)',
        r'<table class="tech-table">\1',
        html_body
    )
    # Auto-add class="resource-table" to tables that start with "Item" and "Delivery Method" headers
    html_body = re.sub(
        r'<table>(\s*<thead>\s*<tr>\s*<th>Item</th>\s*<th>Delivery Method</th>)',
        r'<table class="resource-table">\1',
        html_body
    )
    
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(prefix + html_body + suffix)
    
    print(f"Saved {out_file}")

if os.path.exists('temp.md'):
    os.remove('temp.md')
print("Task completed successfully.")
