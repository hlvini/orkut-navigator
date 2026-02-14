import argparse
import re
from playwright.sync_api import sync_playwright

# definicao dos argumentos necessarios para funcionamento do codigo
parser = argparse.ArgumentParser()
parser.add_argument("--letra", required=True)
parser.add_argument("--palavra", required=True)
args = parser.parse_args()

url_inicial = f"https://web.archive.org/web/2/http://orkut.google.com/l-{args.letra}.html" # url do acervo 

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page() # abre aba
    page.goto(url_inicial) # vai pro acervo
    page.wait_for_load_state("networkidle") # espera carregar td

    while True:
        texto = page.inner_text("body")
        if re.search(rf"\b{re.escape(args.palavra)}\b", texto, re.IGNORECASE): 
            print(f"PALAVRA INFORMADA <<{args.palavra}>> ENCONTRADO(A) EM -> ", page.url)

        next_btn = page.locator(rf"text=\bnext\b")
        if next_btn.count() == 0:
            break

        next_btn.first.click()
        page.wait_for_load_state("networkidle")

    browser.close()
