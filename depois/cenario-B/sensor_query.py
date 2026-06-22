from db_connection import buscar_leituras_por_obra

FATOR_EMISSAO_KG_CO2_POR_KWH = 0.0817


def calcular_emissao_co2(consumo_kwh: float) -> float:
    return consumo_kwh * FATOR_EMISSAO_KG_CO2_POR_KWH


def gerar_relatorio_emissao_obra(obra_id: int):
    leituras = buscar_leituras_por_obra(obra_id)

    consumo_total_kwh = sum(
        leitura[3] or 0
        for leitura in leituras
    )

    emissao_total = calcular_emissao_co2(consumo_total_kwh)

    return {
        "obra_id": obra_id,
        "consumo_total_kwh": consumo_total_kwh,
        "emissao_total_kg_co2": emissao_total,
        "fator_utilizado": FATOR_EMISSAO_KG_CO2_POR_KWH,
        "total_leituras": len(leituras),
    }


if __name__ == "__main__":
    print(gerar_relatorio_emissao_obra(12))
