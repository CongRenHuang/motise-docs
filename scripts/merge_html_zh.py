import re
import os

def extract_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Match the content inside <div class="article"> ... </div> before the closing page-wrapper div.
    # Greedy to the LAST </div></div> so inner nested double-closes (e.g. .sig-grid > .sig-block) don't truncate the body.
    match = re.search(r'<div class="article">([\s\S]*)</div>\s*</div>', content)
    if match:
        return match.group(1).strip()
    else:
        raise ValueError(f"Could not find article content in {file_path}")

def main():
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "html", "zh")
    
    contract_path = os.path.join(base_dir, "contract-zh-print.html")
    app_a_path = os.path.join(base_dir, "appendix-a-zh-print.html")
    app_b_path = os.path.join(base_dir, "appendix-b-zh-print.html")
    app_c_path = os.path.join(base_dir, "appendix-c-zh-print.html")
    app_d_path = os.path.join(base_dir, "appendix-d-zh-print.html")
    
    # 1. Read full contract to extract head and foot
    with open(contract_path, 'r', encoding='utf-8') as f:
        contract_full = f.read()
        
    # Split before <div class="page-wrapper">
    head_match = re.split(r'<div class="page-wrapper">', contract_full, maxsplit=1)
    if len(head_match) < 2:
        raise ValueError("Could not locate <div class='page-wrapper'> in contract HTML")
    html_head = head_match[0].strip() + "\n  <div class=\"page-wrapper\">"
    
    # Split after the last </div> before scripts using the comment as target
    foot_match = re.split(r'<!--\s*/page-wrapper\s*-->', contract_full, maxsplit=1)

    if len(foot_match) < 2:
        raise ValueError("Could not locate ending structures in contract HTML")

    # We want everything starting from the script tags to </html>
    html_foot = "\n    </div>\n  </div>\n  " + foot_match[1].strip()

    # 2. Extract contents of each document
    contract_body = extract_article(contract_path)
    app_a_body = extract_article(app_a_path)
    app_b_body = extract_article(app_b_path)
    app_c_body = extract_article(app_c_path)
    app_d_body = extract_article(app_d_path)
    
    # 3. Assemble merged HTML
    merged_html = f"""{html_head}
      <div class="article">
{contract_body}
      </div>
    </div>
    
    <div class="page-wrapper pb-before">
      <div class="article">
{app_a_body}
      </div>
    </div>
    
    <div class="page-wrapper pb-before">
      <div class="article">
{app_b_body}
      </div>
    </div>
    
    <div class="page-wrapper pb-before">
      <div class="article">
{app_c_body}
      </div>
    </div>
    
    <div class="page-wrapper pb-before">
      <div class="article">
{app_d_body}
      </div>
    </div>
{html_foot}"""

    # 5. Write to destination file
    output_path = os.path.join(base_dir, "merged-zh-print.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(merged_html)
        
    print(f"Successfully generated merged HTML at: {output_path}")

if __name__ == "__main__":
    main()
