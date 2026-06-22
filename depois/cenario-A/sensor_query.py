from numbers import Number

from db_connection import buscar_leituras_por_obra


# REG-01
# Fonte: VALOR HERDADO DO SISTEMA (referência informada no código: 2021)
# ESTE FATOR DEVE SER VALIDADO COM DADOS OFICIAIS ATUALIZADOS
# DA ANEEL/MCTI ANTES DO USO EM PRODUÇÃO.
FATOR_EMISSAO_KG_CO2_POR_KWH = 0.0817


def validar_consumo_kwh(consumo_kwh):

    if consumo_kwh is None:
        raise ValueError("consumo_kwh nao pode ser nulo")

    if not isinstance(consumo_kwh, Number):
        raise TypeError("consumo_kwh deve ser numerico")

    if consumo_kwh < 0:
        raise ValueError("consumo_kwh nao pode ser negativo")

    return consumo_kwh


def calcular_emissao_co2(consumo_kwh):

    consumo_kwh = validar_consumo_kwh(consumo_kwh)

    return consumo_kwh * FATOR_EMISSAO_KG_CO2_POR_KWH


def gerar_relatorio_emissao_obra(obra_id):

    leituras = buscar_leituras_por_obra(obra_id)

    consumo_total_kwh = 0

    for indice, leitura in enumerate(leituras):

        if len(leitura) <= 3:
            raise ValueError(
                f"Schema inesperado na leitura {indice}"
            )

        consumo = validar_consumo_kwh(leitura[3])

        consumo_total_kwh += consumo

    emissao_total = calcular_emissao_co2(consumo_total_kwh)

    return {
        "obra_id": obra_id,
        "consumo_total_kwh": consumo_total_kwh,
        "emissao_total_kg_co2": emissao_total,
        "fator_utilizado": FATOR_EMISSAO_KG_CO2_POR_KWH,
        "alerta_validacao":
            "Fator de emissao precisa ser validado antes do deploy."
    }
