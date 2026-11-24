# Crédito · Bruno Duarte (KW Azores)

Landing page de captação de leads com simulador de crédito habitação.

- `index.html` — a página.
- `taxas.json` — Euribor a 12 meses e spreads usados no simulador.
  - A Euribor é atualizada automaticamente nos dias úteis pela GitHub Action `Atualizar Euribor`.
  - Os **spreads** (`ate60`, `ate80`, `ate90`, em %) alteram-se à mão neste ficheiro.
