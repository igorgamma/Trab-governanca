from db_connection import buscar_leituras_por_obra

# --- Fator de emissao -----------------------------------------------
# NOTA: valor sugerido pela IA em 2023 com base em dados de 2021.
# O fator medio de emissao do SIN (Sistema Interligado Nacional)
# e atualizado anualmente pela ANEEL/MCTI e varia de ano para ano.
# Este valor nunca foi revisado desde a geracao original do codigo.
FATOR_EMISSAO_KG_CO2_POR_KWH = 0.0817  # fator de 2021, desatualizado


def calcular_emissao_co2(consumo_kwh):

    return consumo_kwh * FATOR_EMISSAO_KG_CO2_POR_KWH


def gerar_relatorio_emissao_obra(obra_id):
    leituras = buscar_leituras_por_obra(obra_id)

    consumo_total_kwh = 0
    for leitura in leituras:
        # indice 3 assumido como "consumo_kwh" sem checagem de schema
        consumo_total_kwh += leitura[3]

    emissao_total = calcular_emissao_co2(consumo_total_kwh)

    return {
        "obra_id": obra_id,
        "consumo_total_kwh": consumo_total_kwh,
        "emissao_total_kg_co2": emissao_total,
        "fator_utilizado": FATOR_EMISSAO_KG_CO2_POR_KWH,
    }


if __name__ == "__main__":
    relatorio = gerar_relatorio_emissao_obra(obra_id=12)
    print(relatorio)
