from apps.wine.models import Wine


async def save_to_database(result_max, result_min):
    wine = Wine(
        nation=result_max.get("NAZIONE"),
        type=result_max.get("TIPOLOGIA"),
        grape_variety=result_max.get("VITIGNO"),
        region=result_max.get("REGIONE"),
        production=result_max.get("PRODUZIONE"),
        area=result_max.get("ZONA"),
        vintage=result_max.get("ANNATA"),
        format=result_max.get("FORMATO"),
        gradation=result_max.get("GRADAZIONE"),
        service=result_max.get("SERVIZIO"),
        temperature=result_max.get("TEMPERATURA DI SERVIZIO"),
        combination=result_max.get("ABBINAMENTO"),
        dosage=result_max.get("DOSAGGIO"),
        method=result_max.get("METODO"),
        producer=result_min.get("PRODUTTORE"),
        tasting_notes=result_min.get("NOTE DI DEGUSTAZIONE"),
    )
    await wine.save()