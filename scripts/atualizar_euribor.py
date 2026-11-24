"""Atualiza a Euribor a 12 meses em taxas.json. Os spreads não são alterados."""
import json, re, sys, urllib.request
from datetime import datetime

URL = "https://www.euribor-rates.eu/pt/taxas-euribor-actuais/4/euribor-taxa-12-meses/"
req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0 (compatible; atualizador-taxas)"})
html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"&nbsp;|\s+", " ", text)

# Linhas da tabela: "dd/mm/aaaa 3,222 %"
pares = re.findall(r"(\d{1,2}/\d{1,2}/20\d\d)\s+(-?\d{1,2}[.,]\d{2,3})\s*%", text)
if not pares:
    sys.exit("Não encontrei valores da Euribor na página; taxas.json fica como está.")

def quando(d):
    return datetime.strptime(d, "%d/%m/%Y")

data, valor = max(pares, key=lambda p: quando(p[0]))
valor = float(valor.replace(",", "."))
if not -2 < valor < 15:
    sys.exit(f"Valor fora do intervalo esperado ({valor}); taxas.json fica como está.")

with open("taxas.json", encoding="utf-8") as f:
    taxas = json.load(f)
taxas["euribor12m"] = valor
taxas["data"] = quando(data).strftime("%d/%m/%Y")
with open("taxas.json", "w", encoding="utf-8") as f:
    json.dump(taxas, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Euribor 12M {valor}% em {taxas['data']}")
