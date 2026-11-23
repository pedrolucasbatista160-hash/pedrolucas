import json
import requests

ceps = ["01001000", "76380000", "00000000"]
resultados = []

for cep in ceps:
    try:
        resp = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
        resp.raise_for_status()
        dados = resp.json()

        if "erro" in dados:
            print(f"CEP {cep} não encontrado.")
        else:
            resultados.append({
                "cep": dados["cep"],
                "cidade": dados["localidade"],
                "uf": dados["uf"]
            })
    except requests.RequestException as e:
        print(f"Erro ao consultar CEP {cep}: {e}")

with open("ceps_consultados.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, ensure_ascii=False, indent=4)

print("Consulta finalizada e salva em ceps_consultados.json.")