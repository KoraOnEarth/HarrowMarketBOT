import requests
import json


def collect_data(item):
    url_name = warframes_to_url(item)
    r = requests.get(f"https://api.warframe.market/v1/items/{url_name}/orders")
    r_json = r.json()

    
    min_order = min(
        (o for o in r_json["payload"]["orders"] if o["user"]['status'] == "ingame" and o["region"] == "en" and o["order_type"] == "sell"),
        key=lambda o: o["platinum"],
    )
    min_plat = min_order["platinum"]
    author = min_order["user"]["ingame_name"]
    quantity = min_order["quantity"]
    

    # with open('min.json', 'w') as file:
    #     json.dump(r_json, file, indent=4, ensure_ascii=False)

    print(author, min_plat, quantity)
    return author, min_plat, quantity


def warframes_to_url(item):

    #Атлас
    if item.lower() == "атлас прайм сет":
        url_name = "atlas_prime_set"
    elif item.lower() == "атлас прайм комплект":
        url_name = "atlas_prime_set"
    elif item.lower() == "атлас прайм каркас":
        url_name = "atlas_prime_chassis"
    elif item.lower() == "атлас прайм система":
        url_name = "atlas_prime_systems"
    elif item.lower() == "атлас прайм нейрооптика":
        url_name = "atlas_prime_neuroptics"
    elif item.lower() == "атлас прайм чертеж":
        url_name = "atlas_prime_blueprint"

    #Банши
    if item.lower() == "банши прайм сет":
        url_name = "banshee_prime_set"
    elif item.lower() == "банши прайм комплект":
        url_name = "banshee_prime_set"
    elif item.lower() == "банши прайм каркас":
        url_name = "banshee_prime_chassis"
    elif item.lower() == "банши прайм система":
        url_name = "banshee_prime_systems"
    elif item.lower() == "банши прайм нейрооптика":
        url_name = "banshee_prime_neuroptics"
    elif item.lower() == "банши прайм чертеж":
        url_name = "banshee_prime_blueprint"
    
    #Валькирия
    if item.lower() == "валькирия прайм сет":
        url_name = "valkyr_prime_set"
    elif item.lower() == "валькирия прайм комплект":
        url_name = "valkyr_prime_set"
    elif item.lower() == "валькирия прайм каркас":
        url_name = "valkyr_prime_chassis"
    elif item.lower() == "валькирия прайм система":
        url_name = "valkyr_prime_systems"
    elif item.lower() == "валькирия прайм нейрооптика":
        url_name = "valkyr_prime_neuroptics"
    elif item.lower() == "валькирия прайм чертеж":
        url_name = "valkyr_prime_blueprint"

    #Вобан
    if item.lower() == "вобан прайм сет":
        url_name = "vauban_prime_set"
    elif item.lower() == "вобан прайм комплект":
        url_name = "vauban_prime_set"
    elif item.lower() == "вобан прайм каркас":
        url_name = "vauban_prime_chassis"
    elif item.lower() == "вобан прайм система":
        url_name = "vauban_prime_systems"
    elif item.lower() == "вобан прайм нейрооптика":
        url_name = "vauban_prime_neuroptics"
    elif item.lower() == "вобан прайм чертеж":
        url_name = "vauban_prime_blueprint"

    #Вольт
    if item.lower() == "вольт прайм сет":
        url_name = "volt_prime_set"
    elif item.lower() == "вольт прайм комплект":
        url_name = "volt_prime_set"
    elif item.lower() == "вольт прайм каркас":
        url_name = "volt_prime_chassis"
    elif item.lower() == "вольт прайм система":
        url_name = "volt_prime_systems"
    elif item.lower() == "вольт прайм нейрооптика":
        url_name = "volt_prime_neuroptics"
    elif item.lower() == "вольт прайм чертеж":
        url_name = "volt_prime_blueprint"

    #Вуконг
    if item.lower() == "вуконг прайм сет":
        url_name = "wukong_prime_set"
    elif item.lower() == "вуконг прайм комплект":
        url_name = "wukong_prime_set"
    elif item.lower() == "вуконг прайм каркас":
        url_name = "wukong_prime_chassis"
    elif item.lower() == "вуконг прайм система":
        url_name = "wukong_prime_systems"
    elif item.lower() == "вуконг прайм нейрооптика":
        url_name = "wukong_prime_neuroptics"
    elif item.lower() == "вуконг прайм чертеж":
        url_name = "wukong_prime_blueprint"

    #Гара
    if item.lower() == "гара прайм сет":
        url_name = "gara_prime_set"
    elif item.lower() == "гара прайм комплект":
        url_name = "gara_prime_set"
    elif item.lower() == "гара прайм каркас":
        url_name = "gara_prime_chassis"
    elif item.lower() == "гара прайм система":
        url_name = "gara_prime_systems"
    elif item.lower() == "гара прайм нейрооптика":
        url_name = "gara_prime_neuroptics"
    elif item.lower() == "гара прайм чертеж":
        url_name = "gara_prime_blueprint"

    #Гаруда
    if item.lower() == "гаруда прайм сет":
        url_name = "garuda_prime_set"
    elif item.lower() == "гаруда прайм комплект":
        url_name = "garuda_prime_set"
    elif item.lower() == "гаруда прайм каркас":
        url_name = "garuda_prime_chassis"
    elif item.lower() == "гаруда прайм система":
        url_name = "garuda_prime_systems"
    elif item.lower() == "гаруда прайм нейрооптика":
        url_name = "garuda_prime_neuroptics"
    elif item.lower() == "гаруда прайм чертеж":
        url_name = "garuda_prime_blueprint"

    #Гидроид
    if item.lower() == "гидроид прайм сет":
        url_name = "hydroid_prime_set"
    elif item.lower() == "гидроид прайм комплект":
        url_name = "hydroid_prime_set"
    elif item.lower() == "гидроид прайм каркас":
        url_name = "hydroid_prime_chassis"
    elif item.lower() == "гидроид прайм система":
        url_name = "hydroid_prime_systems"
    elif item.lower() == "гидроид прайм нейрооптика":
        url_name = "hydroid_prime_neuroptics"
    elif item.lower() == "гидроид прайм чертеж":
        url_name = "hydroid_prime_blueprint"

    #Зефир
    if item.lower() == "зефир прайм сет":
        url_name = "zephyr_prime_set"
    elif item.lower() == "зефир прайм комплект":
        url_name = "zephyr_prime_set"
    elif item.lower() == "зефир прайм каркас":
        url_name = "zephyr_prime_chassis"
    elif item.lower() == "зефир прайм система":
        url_name = "zephyr_prime_systems"
    elif item.lower() == "зефир прайм нейрооптика":
        url_name = "zephyr_prime_neuroptics"
    elif item.lower() == "зефир прайм чертеж":
        url_name = "zephyr_prime_blueprint"

    #Ивара
    if item.lower() == "ивара прайм сет":
        url_name = "ivara_prime_set"
    elif item.lower() == "ивара прайм комплект":
        url_name = "ivara_prime_set"
    elif item.lower() == "ивара прайм каркас":
        url_name = "ivara_prime_chassis"
    elif item.lower() == "ивара прайм система":
        url_name = "ivara_prime_systems"
    elif item.lower() == "ивара прайм нейрооптика":
        url_name = "ivara_prime_neuroptics"
    elif item.lower() == "ивара прайм чертеж":
        url_name = "ivara_prime_blueprint"

    #Инарос
    if item.lower() == "инарос прайм сет":
        url_name = "inaros_prime_set"
    elif item.lower() == "инарос прайм комплект":
        url_name = "inaros_prime_set"
    elif item.lower() == "инарос прайм каркас":
        url_name = "inaros_prime_chassis"
    elif item.lower() == "инарос прайм система":
        url_name = "inaros_prime_systems"
    elif item.lower() == "инарос прайм нейрооптика":
        url_name = "inaros_prime_neuroptics"
    elif item.lower() == "инарос прайм чертеж":
        url_name = "inaros_prime_blueprint"

    #Кора
    if item.lower() == "кора прайм сет":
        url_name = "khora_prime_set"
    elif item.lower() == "кора прайм комплект":
        url_name = "khora_prime_set"
    elif item.lower() == "кора прайм каркас":
        url_name = "khora_prime_chassis_blueprint"
    elif item.lower() == "кора прайм система":
        url_name = "khora_prime_systems_blueprint"
    elif item.lower() == "кора прайм нейрооптика":
        url_name = "khora_prime_neuroptics_blueprint"
    elif item.lower() == "кора прайм чертеж":
        url_name = "khora_prime_systems_blueprint"

    #Лимбо
    if item.lower() == "лимбо прайм сет":
        url_name = "limbo_prime_set"
    elif item.lower() == "лимбо прайм комплект":
        url_name = "limbo_prime_set"
    elif item.lower() == "лимбо прайм каркас":
        url_name = "limbo_prime_chassis"
    elif item.lower() == "лимбо прайм система":
        url_name = "limbo_prime_systems"
    elif item.lower() == "лимбо прайм нейрооптика":
        url_name = "limbo_prime_neuroptics"
    elif item.lower() == "лимбо прайм чертеж":
        url_name = "limbo_prime_blueprint"

    #Локи
    if item.lower() == "локи прайм сет":
        url_name = "loki_prime_set"
    elif item.lower() == "локи прайм комплект":
        url_name = "loki_prime_set"
    elif item.lower() == "локи прайм каркас":
        url_name = "loki_prime_chassis"
    elif item.lower() == "локи прайм система":
        url_name = "loki_prime_systems"
    elif item.lower() == "локи прайм нейрооптика":
        url_name = "loki_prime_neuroptics"
    elif item.lower() == "локи прайм чертеж":
        url_name = "loki_prime_blueprint"

    #Мираж
    if item.lower() == "мираж прайм сет":
        url_name = "mirage_prime_set"
    elif item.lower() == "мираж прайм комплект":
        url_name = "mirage_prime_set"
    elif item.lower() == "мираж прайм каркас":
        url_name = "mirage_prime_chassis"
    elif item.lower() == "мираж прайм система":
        url_name = "mirage_prime_systems"
    elif item.lower() == "мираж прайм нейрооптика":
        url_name = "mirage_prime_neuroptics"
    elif item.lower() == "мираж прайм чертеж":
        url_name = "mirage_prime_blueprint"

    #Миса
    if item.lower() == "миса прайм сет":
        url_name = "mesa_prime_set"
    elif item.lower() == "миса прайм комплект":
        url_name = "mesa_prime_set"
    elif item.lower() == "миса прайм каркас":
        url_name = "mesa_prime_chassis"
    elif item.lower() == "миса прайм система":
        url_name = "mesa_prime_systems"
    elif item.lower() == "миса прайм нейрооптика":
        url_name = "mesa_prime_neuroptics"
    elif item.lower() == "миса прайм чертеж":
        url_name = "mesa_prime_blueprint"

    #Мэг
    if item.lower() == "мэг прайм сет":
        url_name = "mag_prime_set"
    elif item.lower() == "мэг прайм комплект":
        url_name = "mag_prime_set"
    elif item.lower() == "мэг прайм каркас":
        url_name = "mag_prime_chassis"
    elif item.lower() == "мэг прайм система":
        url_name = "mag_prime_systems"
    elif item.lower() == "мэг прайм нейрооптика":
        url_name = "mag_prime_neuroptics"
    elif item.lower() == "мэг прайм чертеж":
        url_name = "mag_prime_blueprint"

    #Некрос
    if item.lower() == "некрос прайм сет":
        url_name = "nekros_prime_set"
    elif item.lower() == "некрос прайм комплект":
        url_name = "nekros_prime_set"
    elif item.lower() == "некрос прайм каркас":
        url_name = "nekros_prime_chassis"
    elif item.lower() == "некрос прайм система":
        url_name = "nekros_prime_systems"
    elif item.lower() == "некрос прайм нейрооптика":
        url_name = "nekros_prime_neuroptics"
    elif item.lower() == "некрос прайм чертеж":
        url_name = "nekros_prime_blueprint"

    #Нидус
    if item.lower() == "нидус прайм сет":
        url_name = "nidus_prime_set"
    elif item.lower() == "нидус прайм комплект":
        url_name = "nidus_prime_set"
    elif item.lower() == "нидус прайм каркас":
        url_name = "nidus_prime_chassis"
    elif item.lower() == "нидус прайм система":
        url_name = "nidus_prime_systems"
    elif item.lower() == "нидус прайм нейрооптика":
        url_name = "nidus_prime_neuroptics"
    elif item.lower() == "нидус прайм чертеж":
        url_name = "nidus_prime_blueprint"

    #Никс
    if item.lower() == "никс прайм сет":
        url_name = "nyx_prime_set"
    elif item.lower() == "никс прайм комплект":
        url_name = "nyx_prime_set"
    elif item.lower() == "никс прайм каркас":
        url_name = "nyx_prime_chassis"
    elif item.lower() == "никс прайм система":
        url_name = "nyx_prime_systems"
    elif item.lower() == "никс прайм нейрооптика":
        url_name = "nyx_prime_neuroptics"
    elif item.lower() == "никс прайм чертеж":
        url_name = "nyx_prime_blueprint"

    #Нова
    if item.lower() == "нова прайм сет":
        url_name = "nova_prime_set"
    elif item.lower() == "нова прайм комплект":
        url_name = "nova_prime_set"
    elif item.lower() == "нова прайм каркас":
        url_name = "nova_prime_chassis"
    elif item.lower() == "нова прайм система":
        url_name = "nova_prime_systems"
    elif item.lower() == "нова прайм нейрооптика":
        url_name = "nova_prime_neuroptics"
    elif item.lower() == "нова прайм чертеж":
        url_name = "nova_prime_blueprint"

    #Нэчжа
    if item.lower() == "нэчжа прайм сет":
        url_name = "nezha_prime_set"
    elif item.lower() == "нэчжа прайм комплект":
        url_name = "nezha_prime_set"
    elif item.lower() == "нэчжа прайм каркас":
        url_name = "nezha_prime_chassis"
    elif item.lower() == "нэчжа прайм система":
        url_name = "nezha_prime_systems"
    elif item.lower() == "нэчжа прайм нейрооптика":
        url_name = "nezha_prime_neuroptics"
    elif item.lower() == "нэчжа прайм чертеж":
        url_name = "nezha_prime_blueprint"

    #Оберон
    if item.lower() == "оберон прайм сет":
        url_name = "oberon_prime_set"
    elif item.lower() == "оберон прайм комплект":
        url_name = "oberon_prime_set"
    elif item.lower() == "оберон прайм каркас":
        url_name = "oberon_prime_chassis"
    elif item.lower() == "оберон прайм система":
        url_name = "oberon_prime_systems"
    elif item.lower() == "оберон прайм нейрооптика":
        url_name = "oberon_prime_neuroptics"
    elif item.lower() == "оберон прайм чертеж":
        url_name = "oberon_prime_blueprint"

    #Октавия
    if item.lower() == "октавия прайм сет":
        url_name = "octavia_prime_set"
    elif item.lower() == "октавия прайм комплект":
        url_name = "octavia_prime_set"
    elif item.lower() == "октавия прайм каркас":
        url_name = "octavia_prime_chassis"
    elif item.lower() == "октавия прайм система":
        url_name = "octavia_prime_systems"
    elif item.lower() == "октавия прайм нейрооптика":
        url_name = "octavia_prime_neuroptics"
    elif item.lower() == "октавия прайм чертеж":
        url_name = "octavia_prime_blueprint"

    #Ревенант
    if item.lower() == "ревенант прайм сет":
        url_name = "revenant_prime_set"
    elif item.lower() == "ревенант прайм комплект":
        url_name = "revenant_prime_set"
    elif item.lower() == "ревенант прайм каркас":
        url_name = "revenant_prime_chassis_blueprint"
    elif item.lower() == "ревенант прайм система":
        url_name = "revenant_prime_systems_blueprint"
    elif item.lower() == "ревенант прайм нейрооптика":
        url_name = "revenant_prime_neuroptics_blueprint"
    elif item.lower() == "ревенант прайм чертеж":
        url_name = "revenant_prime_blueprint"

    #Рино
    if item.lower() == "рино прайм сет":
        url_name = "rhino_prime_set"
    elif item.lower() == "рино прайм комплект":
        url_name = "rhino_prime_set"
    elif item.lower() == "рино прайм каркас":
        url_name = "rhino_prime_chassis"
    elif item.lower() == "рино прайм система":
        url_name = "rhino_prime_systems"
    elif item.lower() == "рино прайм нейрооптика":
        url_name = "rhino_prime_neuroptics"
    elif item.lower() == "рино прайм чертеж":
        url_name = "rhino_prime_blueprint"

    #Сарина
    if item.lower() == "сарина прайм сет":
        url_name = "saryn_prime_set"
    elif item.lower() == "сарина прайм комплект":
        url_name = "saryn_prime_set"
    elif item.lower() == "сарина прайм каркас":
        url_name = "saryn_prime_chassis"
    elif item.lower() == "сарина прайм система":
        url_name = "saryn_prime_systems"
    elif item.lower() == "сарина прайм нейрооптика":
        url_name = "saryn_prime_neuroptics"
    elif item.lower() == "сарина прайм чертеж":
        url_name = "saryn_prime_blueprint"

    #Титания
    if item.lower() == "титания прайм сет":
        url_name = "titania_prime_set"
    elif item.lower() == "титания прайм комплект":
        url_name = "titania_prime_set"
    elif item.lower() == "титания прайм каркас":
        url_name = "titania_prime_chassis"
    elif item.lower() == "титания прайм система":
        url_name = "titania_prime_systems"
    elif item.lower() == "титания прайм нейрооптика":
        url_name = "titania_prime_neuroptics"
    elif item.lower() == "титания прайм чертеж":
        url_name = "titania_prime_blueprint"

    #Тринити
    if item.lower() == "тринити прайм сет":
        url_name = "trinity_prime_set"
    elif item.lower() == "тринити прайм комплект":
        url_name = "trinity_prime_set"
    elif item.lower() == "тринити прайм каркас":
        url_name = "trinity_prime_chassis"
    elif item.lower() == "тринити прайм система":
        url_name = "trinity_prime_systems"
    elif item.lower() == "тринити прайм нейрооптика":
        url_name = "trinity_prime_neuroptics"
    elif item.lower() == "тринити прайм чертеж":
        url_name = "trinity_prime_blueprint"

    #Фрост
    if item.lower() == "фрост прайм сет":
        url_name = "frost_prime_set"
    elif item.lower() == "фрост прайм комплект":
        url_name = "frost_prime_set"
    elif item.lower() == "фрост прайм каркас":
        url_name = "frost_prime_chassis"
    elif item.lower() == "фрост прайм система":
        url_name = "frost_prime_systems"
    elif item.lower() == "фрост прайм нейрооптика":
        url_name = "frost_prime_neuroptics"
    elif item.lower() == "фрост прайм чертеж":
        url_name = "frost_prime_blueprint"

    #Харроу
    if item.lower() == "харроу прайм сет":
        url_name = "harrow_prime_set"
    elif item.lower() == "харроу прайм комплект":
        url_name = "harrow_prime_set"
    elif item.lower() == "харроу прайм каркас":
        url_name = "harrow_prime_chassis"
    elif item.lower() == "харроу прайм система":
        url_name = "harrow_prime_systems"
    elif item.lower() == "харроу прайм нейрооптика":
        url_name = "harrow_prime_neuroptics"
    elif item.lower() == "харроу прайм чертеж":
        url_name = "harrow_prime_blueprint"

    #Хрома
    if item.lower() == "хрома прайм сет":
        url_name = "chroma_prime_set"
    elif item.lower() == "хрома прайм комплект":
        url_name = "chroma_prime_set"
    elif item.lower() == "хрома прайм каркас":
        url_name = "chroma_prime_chassis"
    elif item.lower() == "хрома прайм система":
        url_name = "chroma_prime_systems"
    elif item.lower() == "хрома прайм нейрооптика":
        url_name = "chroma_prime_neuroptics"
    elif item.lower() == "хрома прайм чертеж":
        url_name = "chroma_prime_blueprint"

    #Эквинокс
    if item.lower() == "эквинокс прайм сет":
        url_name = "equinox_prime_set"
    elif item.lower() == "эквинокс прайм комплект":
        url_name = "equinox_prime_set"
    elif item.lower() == "эквинокс прайм каркас":
        url_name = "equinox_prime_chassis"
    elif item.lower() == "эквинокс прайм система":
        url_name = "equinox_prime_systems"
    elif item.lower() == "эквинокс прайм нейрооптика":
        url_name = "equinox_prime_neuroptics"
    elif item.lower() == "эквинокс прайм чертеж":
        url_name = "equinox_prime_blueprint"

    #Эмбер
    if item.lower() == "эмбер прайм сет":
        url_name = "ember_prime_set"
    elif item.lower() == "эмбер прайм комплект":
        url_name = "ember_prime_set"
    elif item.lower() == "эмбер прайм каркас":
        url_name = "ember_prime_chassis"
    elif item.lower() == "эмбер прайм система":
        url_name = "ember_prime_systems"
    elif item.lower() == "эмбер прайм нейрооптика":
        url_name = "ember_prime_neuroptics"
    elif item.lower() == "эмбер прайм чертеж":
        url_name = "ember_prime_blueprint"

    #Эш
    if item.lower() == "эш прайм сет":
        url_name = "ash_prime_set"
    elif item.lower() == "эш прайм комплект":
        url_name = "ash_prime_set"
    elif item.lower() == "эш прайм каркас":
        url_name = "ash_prime_chassis"
    elif item.lower() == "эш прайм система":
        url_name = "ash_prime_systems"
    elif item.lower() == "эш прайм нейрооптика":
        url_name = "ash_prime_neuroptics"
    elif item.lower() == "эш прайм чертеж":
        url_name = "ash_prime_blueprint"

    # #Акболто
    # if item.lower() == "акболто прайм сет":
    #     url_name = "akbolto_prime_set"
    # elif item.lower() == "акболто прайм комплект":
    #     url_name = "akbolto_prime_set"
    # elif item.lower() == "акболто прайм приемник":
    #     url_name = "akbolto_prime_receiver"
    # elif item.lower() == "акболто прайм связь":
    #     url_name = "akbolto_prime_link"
    # elif item.lower() == "акболто прайм ствол":
    #     url_name = "akbolto_prime_barrel"
    # elif item.lower() == "акболто прайм чертеж":
    #     url_name = "akbolto_prime_blueprint"

    # #Акбронко
    # if item.lower() == "акбронко прайм сет":
    #     url_name = "akbronco_prime_set"
    # elif item.lower() == "акбронко прайм комплект":
    #     url_name = "akbronco_prime_set"
    # elif item.lower() == "акбронко прайм связь":
    #     url_name = "akbronco_prime_link"
    # elif item.lower() == "акбронко прайм чертеж":
    #     url_name = "akbronco_prime_blueprint"

    # #Аквасто
    # if item.lower() == "аквасто прайм сет":
    #     url_name = "akvasto_prime_set"
    # elif item.lower() == "аквасто прайм комплект":
    #     url_name = "akvasto_prime_set"
    # elif item.lower() == "аквасто прайм связь":
    #     url_name = "akvasto_prime_link"
    # elif item.lower() == "аквасто прайм чертеж":
    #     url_name = "akvasto_prime_blueprint"

    # #Акджагара
    # if item.lower() == "акджагара прайм сет":
    #     url_name = "akjagara_prime_set"
    # elif item.lower() == "акджагара прайм комплект":
    #     url_name = "akjagara_prime_set"
    # elif item.lower() == "акджагара прайм приемник":
    #     url_name = "akjagara_prime_receiver"
    # elif item.lower() == "акджагара прайм связь":
    #     url_name = "akjagara_prime_link"
    # elif item.lower() == "акджагара прайм ствол":
    #     url_name = "akjagara_prime_barrel"
    # elif item.lower() == "акджагара прайм чертеж":
    #     url_name = "akjagara_prime_blueprint"

    # #Аклекс
    # if item.lower() == "аклекс прайм сет":
    #     url_name = "aklex_prime_set"
    # elif item.lower() == "аклекс прайм комплект":
    #     url_name = "aklex_prime_set"
    # elif item.lower() == "аклекс прайм связь":
    #     url_name = "aklex_prime_link"
    # elif item.lower() == "аклекс прайм чертеж":
    #     url_name = "aklex_prime_blueprint"

    # #Аксомати
    # if item.lower() == "аксомати прайм сет":
    #     url_name = "aksomati_prime_set"
    # elif item.lower() == "аксомати прайм комплект":
    #     url_name = "aksomati_prime_set"
    # elif item.lower() == "аксомати прайм приемник":
    #     url_name = "aksomati_prime_receiver"
    # elif item.lower() == "аксомати прайм связь":
    #     url_name = "aksomati_prime_link"
    # elif item.lower() == "аксомати прайм ствол":
    #     url_name = "aksomati_prime_barrel"
    # elif item.lower() == "аксомати прайм чертеж":
    #     url_name = "aksomati_prime_blueprint"

    # #Акстилетто
    # if item.lower() == "акстилетто прайм сет":
    #     url_name = "akstiletto_prime_set"
    # elif item.lower() == "акстилетто прайм комплект":
    #     url_name = "akstiletto_prime_set"
    # elif item.lower() == "акстилетто прайм приемник":
    #     url_name = "akstiletto_prime_receiver"
    # elif item.lower() == "акстилетто прайм связь":
    #     url_name = "akstiletto_prime_link"
    # elif item.lower() == "акстилетто прайм ствол":
    #     url_name = "akstiletto_prime_barrel"
    # elif item.lower() == "акстилетто прайм чертеж":
    #     url_name = "akstiletto_prime_blueprint"

    # #Анкирос
    # if item.lower() == "анкирос прайм сет":
    #     url_name = "ankyros_prime_set"
    # elif item.lower() == "анкирос прайм комплект":
    #     url_name = "ankyros_prime_set"
    # elif item.lower() == "анкирос прайм лезвие":
    #     url_name = "ankyros_prime_blade"
    # elif item.lower() == "анкирос прайм перчатка":
    #     url_name = "ankyros_prime_gauntlet"
    # elif item.lower() == "анкирос прайм чертеж":
    #     url_name = "ankyros_prime_blueprint"

    # #Астилла
    # if item.lower() == "астилла прайм сет":
    #     url_name = "astilla_prime_set"
    # elif item.lower() == "астилла прайм комплект":
    #     url_name = "astilla_prime_set"
    # elif item.lower() == "астилла прайм приемник":
    #     url_name = "astilla_prime_receiver"
    # elif item.lower() == "астилла прайм приклад":
    #     url_name = "astilla_prime_stock"
    # elif item.lower() == "астилла прайм ствол":
    #     url_name = "astilla_prime_barrel"
    # elif item.lower() == "астилла прайм чертеж":
    #     url_name = "astilla_prime_blueprint"

    # #Бёрстон
    # if item.lower() == "берстон прайм сет":
    #     url_name = "burston_prime_set"
    # elif item.lower() == "берстон прайм комплект":
    #     url_name = "burston_prime_set"
    # elif item.lower() == "берстон прайм приемник":
    #     url_name = "burston_prime_receiver"
    # elif item.lower() == "берстон прайм приклад":
    #     url_name = "burston_prime_stock"
    # elif item.lower() == "берстон прайм ствол":
    #     url_name = "burston_prime_barrel"
    # elif item.lower() == "берстон прайм чертеж":
    #     url_name = "burston_prime_blueprint"

    # #База
    # if item.lower() == "база прайм сет":
    #     url_name = "baza_prime_stock"
    # elif item.lower() == "база прайм комплект":
    #     url_name = "baza_prime_stock"
    # elif item.lower() == "база прайм приемник":
    #     url_name = "baza_prime_receiver"
    # elif item.lower() == "база прайм приклад":
    #     url_name = "baza_prime_stock"
    # elif item.lower() == "база прайм ствол":
    #     url_name = "baza_prime_barrel"
    # elif item.lower() == "база прайм чертеж":
    #     url_name = "baza_prime_blueprint"

    # #Баллистика
    # if item.lower() == "баллистика прайм сет":
    #     url_name = "ballistica_prime_set"
    # elif item.lower() == "баллистика прайм комплект":
    #     url_name = "ballistica_prime_set"
    # elif item.lower() == "баллистика прайм приемник":
    #     url_name = "ballistica_prime_receiver"
    # elif item.lower() == "баллистика прайм верхнее плечо":
    #     url_name = "ballistica_prime_stock"
    # elif item.lower() == "баллистика прайм нижнее плечо":
    #     url_name = "ballistica_prime_barrel"
    # elif item.lower() == "баллистика прайм тетива":
    #     url_name = "ballistica_prime_barrel"
    # elif item.lower() == "баллистика прайм чертеж":
    #     url_name = "ballistica_prime_blueprint"

    # #Бо
    # if item.lower() == "бо прайм сет":
    #     url_name = "bo_prime_set"
    # elif item.lower() == "бо прайм комплект":
    #     url_name = "bo_prime_set"
    # elif item.lower() == "бо прайм орнамент":
    #     url_name = "bo_prime_ornament"
    # elif item.lower() == "бо прайм рукоять":
    #     url_name = "bo_prime_handle"
    # elif item.lower() == "бо прайм чертеж":
    #     url_name = "bo_prime_blueprint"

    # #Болтор
    # if item.lower() == "болтор прайм сет":
    #     url_name = "boltor_prime_set"
    # elif item.lower() == "болтор прайм комплект":
    #     url_name = "boltor_prime_set"
    # elif item.lower() == "болтор прайм приемник":
    #     url_name = "boltor_prime_receiver"
    # elif item.lower() == "болтор прайм приклад":
    #     url_name = "boltor_prime_stock"
    # elif item.lower() == "болтор прайм ствол":
    #     url_name = "boltor_prime_barrel"
    # elif item.lower() == "болтор прайм чертеж":
    #     url_name = "boltor_prime_blueprint"

    # #Бронко
    # if item.lower() == "бронко прайм сет":
    #     url_name = "bronco_prime_set"
    # elif item.lower() == "бронко прайм комплект":
    #     url_name = "bronco_prime_set"
    # elif item.lower() == "бронко прайм приемник":
    #     url_name = "bronco_prime_receiver"
    # elif item.lower() == "бронко прайм ствол":
    #     url_name = "bronco_prime_barrel"
    # elif item.lower() == "бронко прайм чертеж":
    #     url_name = "bronco_prime_blueprint"

    # #Брэйтон
    # if item.lower() == "брэйтон прайм сет":
    #     url_name = "braton_prime_set"
    # elif item.lower() == "брэйтон прайм комплект":
    #     url_name = "braton_prime_set"
    # elif item.lower() == "брэйтон прайм приемник":
    #     url_name = "braton_prime_receiver"
    # elif item.lower() == "брэйтон прайм приклад":
    #     url_name = "braton_prime_stock"
    # elif item.lower() == "брэйтон прайм ствол":
    #     url_name = "braton_prime_barrel"
    # elif item.lower() == "брэйтон прайм чертеж":
    #     url_name = "braton_prime_blueprint"

    # #Васто
    # if item.lower() == "васто прайм сет":
    #     url_name = "vasto_prime_set"
    # elif item.lower() == "васто прайм комплект":
    #     url_name = "vasto_prime_set"
    # elif item.lower() == "васто прайм приемник":
    #     url_name = "vasto_prime_receiver"
    # elif item.lower() == "васто прайм ствол":
    #     url_name = "vasto_prime_barrel"
    # elif item.lower() == "васто прайм чертеж":
    #     url_name = "vasto_prime_blueprint"

    # #Вектис
    # if item.lower() == "вектис прайм сет":
    #     url_name = "vectis_prime_set"
    # elif item.lower() == "вектис прайм комплект":
    #     url_name = "vectis_prime_set"
    # elif item.lower() == "вектис прайм приемник":
    #     url_name = "vectis_prime_receiver"
    # elif item.lower() == "вектис прайм приклад":
    #     url_name = "vectis_prime_stock"
    # elif item.lower() == "вектис прайм ствол":
    #     url_name = "vectis_prime_barrel"
    # elif item.lower() == "вектис прайм чертеж":
    #     url_name = "vectis_prime_blueprint"

    # #Венка
    # if item.lower() == "венка прайм сет":
    #     url_name = "venka_prime_set"
    # elif item.lower() == "венка прайм комплект":
    #     url_name = "venka_prime_set"
    # elif item.lower() == "венка прайм перчатка":
    #     url_name = "venka_prime_gauntlet"
    # elif item.lower() == "венка прайм лезвия":
    #     url_name = "venka_prime_blades"
    # elif item.lower() == "венка прайм чертеж":
    #     url_name = "venka_prime_blueprint"

    # #Вепрь
    # if item.lower() == "вепрь прайм сет":
    #     url_name = "boar_prime_set"
    # elif item.lower() == "вепрь прайм комплект":
    #     url_name = "boar_prime_set"
    # elif item.lower() == "вепрь прайм приемник":
    #     url_name = "boar_prime_receiver"
    # elif item.lower() == "вепрь прайм приклад":
    #     url_name = "boar_prime_stock"
    # elif item.lower() == "вепрь прайм ствол":
    #     url_name = "boar_prime_barrel"
    # elif item.lower() == "вепрь прайм чертеж":
    #     url_name = "boar_prime_blueprint"

    # #Вольнус
    # if item.lower() == "венка прайм сет":
    #     url_name = "volnus_prime_set"
    # elif item.lower() == "венка прайм комплект":
    #     url_name = "volnus_prime_set"
    # elif item.lower() == "венка прайм рукоять":
    #     url_name = "volnus_prime_handle"
    # elif item.lower() == "венка прайм молот":
    #     url_name = "volnus_prime_head"
    # elif item.lower() == "венка прайм чертеж":
    #     url_name = "volnus_prime_blueprint"

    # #Галатин
    # if item.lower() == "галатин прайм сет":
    #     url_name = "galatine_prime_set"
    # elif item.lower() == "галатин прайм комплект":
    #     url_name = "galatine_prime_set"
    # elif item.lower() == "галатин прайм рукоять":
    #     url_name = "galatine_prime_handle"
    # elif item.lower() == "галатин прайм клинок":
    #     url_name = "galatine_prime_blade"
    # elif item.lower() == "галатин прайм чертеж":
    #     url_name = "galatine_prime_blueprint"

    # #Глефа
    # if item.lower() == "глефа прайм сет":
    #     url_name = "glaive_prime_set"
    # elif item.lower() == "глефа прайм комплект":
    #     url_name = "glaive_prime_set"
    # elif item.lower() == "глефа прайм диск":
    #     url_name = "glaive_prime_disc"
    # elif item.lower() == "глефа прайм лезвие":
    #     url_name = "glaive_prime_blade"
    # elif item.lower() == "глефа прайм чертеж":
    #     url_name = "glaive_prime_blueprint"

    # #Грэм
    # if item.lower() == "грэм прайм сет":
    #     url_name = "gram_prime_set"
    # elif item.lower() == "грэм прайм комплект":
    #     url_name = "gram_prime_set"
    # elif item.lower() == "грэм прайм клинок":
    #     url_name = "gram_prime_blade"
    # elif item.lower() == "грэм прайм рукоять":
    #     url_name = "gram_prime_handle"
    # elif item.lower() == "грэм прайм чертеж":
    #     url_name = "gram_prime_blueprint"

    # #Гуаньдао
    # if item.lower() == "гуаньдао прайм сет":
    #     url_name = "guandao_prime_set"
    # elif item.lower() == "гуаньдао прайм комплект":
    #     url_name = "guandao_prime_set"
    # elif item.lower() == "гуаньдао прайм клинок":
    #     url_name = "guandao_prime_blade"
    # elif item.lower() == "гуаньдао прайм рукоять":
    #     url_name = "guandao_prime_handle"
    # elif item.lower() == "гуаньдао прайм чертеж":
    #     url_name = "guandao_prime_blueprint"

    # #Дакра
    # if item.lower() == "дакра прайм сет":
    #     url_name = "dakra_prime_set"
    # elif item.lower() == "дакра прайм комплект":
    #     url_name = "dakra_prime_set"
    # elif item.lower() == "дакра прайм клинок":
    #     url_name = "dakra_prime_blade"
    # elif item.lower() == "дакра прайм рукоять":
    #     url_name = "dakra_prime_handle"
    # elif item.lower() == "дакра прайм чертеж":
    #     url_name = "dakra_prime_blueprint"

    # #Дестреза
    # if item.lower() == "дестреза прайм сет":
    #     url_name = "destreza_prime_set"
    # elif item.lower() == "дестреза прайм комплект":
    #     url_name = "destreza_prime_set"
    # elif item.lower() == "дестреза прайм клинок":
    #     url_name = "destreza_prime_blade"
    # elif item.lower() == "дестреза прайм рукоять":
    #     url_name = "destreza_prime_handle"
    # elif item.lower() == "дестреза прайм чертеж":
    #     url_name = "destreza_prime_blueprint"

    # #Жнец
    # if item.lower() == "жнец прайм сет":
    #     url_name = "reaper_prime_set"
    # elif item.lower() == "жнец прайм комплект":
    #     url_name = "reaper_prime_set"
    # elif item.lower() == "жнец прайм лезвие":
    #     url_name = "reaper_prime_blade"
    # elif item.lower() == "жнец прайм рукоять":
    #     url_name = "reaper_prime_handle"
    # elif item.lower() == "жнец прайм чертеж":
    #     url_name = "reaper_prime_blueprint"

    # #Закти
    # if item.lower() == "закти прайм сет":
    #     url_name = "zakti_prime_set"
    # elif item.lower() == "закти прайм комплект":
    #     url_name = "zakti_prime_set"
    # elif item.lower() == "закти прайм ствол":
    #     url_name = "zakti_prime_barrel"
    # elif item.lower() == "закти прайм приемник":
    #     url_name = "zakti_prime_receiver"
    # elif item.lower() == "закти прайм чертеж":
    #     url_name = "zakti_prime_blueprint"

    # #Избавитель
    # if item.lower() == "избавитель прайм сет":
    #     url_name = "redeemer_prime_set"
    # elif item.lower() == "избавитель прайм комплект":
    #     url_name = "redeemer_prime_set"
    # elif item.lower() == "избавитель прайм рукоять":
    #     url_name = "redeemer_prime_handle"
    # elif item.lower() == "избавитель прайм лезвие":
    #     url_name = "redeemer_prime_blade"
    # elif item.lower() == "избавитель прайм чертеж":
    #     url_name = "redeemer_prime_blueprint"

    # #Кара
    # if item.lower() == "кара прайм сет":
    #     url_name = "scourge_prime_set"
    # elif item.lower() == "кара прайм комплект":
    #     url_name = "scourge_prime_set"
    # elif item.lower() == "кара прайм рукоять":
    #     url_name = "scourge_prime_handle"
    # elif item.lower() == "кара прайм ствол":
    #     url_name = "scourge_prime_barrel"
    # elif item.lower() == "кара прайм лезвие":
    #     url_name = "scourge_prime_blade"
    # elif item.lower() == "кара прайм чертеж":
    #     url_name = "scourge_prime_blueprint"

    # #Карист
    # if item.lower() == "карист прайм сет":
    #     url_name = "karyst_prime_set"
    # elif item.lower() == "карист прайм комплект":
    #     url_name = "karyst_prime_set"
    # elif item.lower() == "карист прайм рукоять":
    #     url_name = "karyst_prime_handle"
    # elif item.lower() == "карист прайм лезвие":
    #     url_name = "karyst_prime_blade"
    # elif item.lower() == "карист прайм чертеж":
    #     url_name = "karyst_prime_blueprint"

    # #Кернунн
    # if item.lower() == "кернунн прайм сет":
    #     url_name = "cernos_prime_set"
    # elif item.lower() == "кернунн прайм комплект":
    #     url_name = "cernos_prime_set"
    # elif item.lower() == "кернунн прайм нижнее плечо":
    #     url_name = "cernos_prime_handle"
    # elif item.lower() == "кернунн прайм верхнее плечо":
    #     url_name = "cernos_prime_blade"
    # elif item.lower() == "кернунн прайм рукоять":
    #     url_name = "cernos_prime_grip"
    # elif item.lower() == "кернунн прайм тетива":
    #     url_name = "cernos_prime_string"
    # elif item.lower() == "кернунн прайм чертеж":
    #     url_name = "cernos_prime_blueprint"

    # #Клыки
    # if item.lower() == "клыки прайм сет":
    #     url_name = "fang_prime_set"
    # elif item.lower() == "клыки прайм комплект":
    #     url_name = "fang_prime_set"
    # elif item.lower() == "клыки прайм рукоять":
    #     url_name = "fang_prime_handle"
    # elif item.lower() == "клыки прайм клинок":
    #     url_name = "fang_prime_blade"
    # elif item.lower() == "клыки прайм чертеж":
    #     url_name = "fang_prime_blueprint"

    # #Когаке
    # if item.lower() == "когаке прайм сет":
    #     url_name = "kogake_prime_set"
    # elif item.lower() == "когаке прайм комплект":
    #     url_name = "kogake_prime_set"
    # elif item.lower() == "когаке прайм ступня":
    #     url_name = "kogake_prime_boot"
    # elif item.lower() == "когаке прайм перчатка":
    #     url_name = "kogake_prime_gauntlet"
    # elif item.lower() == "когаке прайм чертеж":
    #     url_name = "kogake_prime_blueprint"

    # #Корвас
    # if item.lower() == "корвас прайм сет":
    #     url_name = "corvas_prime_set"
    # elif item.lower() == "корвас прайм комплект":
    #     url_name = "corvas_prime_set"
    # elif item.lower() == "корвас прайм приемник":
    #     url_name = "corvas_prime_receiver"
    # elif item.lower() == "корвас прайм приклад":
    #     url_name = "corvas_prime_stock"
    # elif item.lower() == "корвас прайм ствол":
    #     url_name = "corvas_prime_barrel"
    # elif item.lower() == "корвас прайм чертеж":
    #     url_name = "corvas_prime_blueprint"

    # #Коринф
    # if item.lower() == "коринф прайм сет":
    #     url_name = "corinth_prime_set"
    # elif item.lower() == "коринф прайм комплект":
    #     url_name = "corinth_prime_set"
    # elif item.lower() == "коринф прайм приемник":
    #     url_name = "corinth_prime_receiver"
    # elif item.lower() == "коринф прайм приклад":
    #     url_name = "corinth_prime_stock"
    # elif item.lower() == "коринф прайм ствол":
    #     url_name = "corinth_prime_barrel"
    # elif item.lower() == "коринф прайм чертеж":
    #     url_name = "corinth_prime_blueprint"

    # #Кронен
    # if item.lower() == "кронен прайм сет":
    #     url_name = "kronen_prime_set"
    # elif item.lower() == "кронен прайм комплект":
    #     url_name = "kronen_prime_set"
    # elif item.lower() == "кронен прайм клинок":
    #     url_name = "kronen_prime_blade"
    # elif item.lower() == "кронен прайм рукоять":
    #     url_name = "kronen_prime_handle"
    # elif item.lower() == "кронен прайм чертеж":
    #     url_name = "kronen_prime_blueprint"

    # #Лато Вандал
    # if item.lower() == "кронен прайм сет":
    #     url_name = "lato_vandal_set"
    # elif item.lower() == "кронен прайм комплект":
    #     url_name = "lato_vandal_set"
    # elif item.lower() == "кронен прайм ствол":
    #     url_name = "lato_vandal_barrel"
    # elif item.lower() == "кронен прайм приемник":
    #     url_name = "lato_vandal_receiver"
    # elif item.lower() == "кронен прайм чертеж":
    #     url_name = "lato_vandal_blueprint"

    # #Латрон
    # if item.lower() == "латрон прайм сет":
    #     url_name = "latron_prime_set"
    # elif item.lower() == "латрон прайм комплект":
    #     url_name = "latron_prime_set"
    # elif item.lower() == "латрон прайм ствол":
    #     url_name = "latron_prime_barrel"
    # elif item.lower() == "латрон прайм приемник":
    #     url_name = "latron_prime_receiver"
    # elif item.lower() == "латрон прайм приклад":
    #     url_name = "latron_prime_stock"
    # elif item.lower() == "латрон прайм чертеж":
    #     url_name = "latron_prime_blueprint"

    # #Магнус
    # if item.lower() == "магнус прайм сет":
    #     url_name = "magnus_prime_set"
    # elif item.lower() == "магнус прайм комплект":
    #     url_name = "magnus_prime_set"
    # elif item.lower() == "магнус прайм ствол":
    #     url_name = "magnus_prime_barrel"
    # elif item.lower() == "магнус прайм приемник":
    #     url_name = "magnus_prime_receiver"
    # elif item.lower() == "магнус прайм чертеж":
    #     url_name = "magnus_prime_blueprint"

    # #Нагантака
    # if item.lower() == "нагантака прайм сет":
    #     url_name = "nagantaka_prime_set"
    # elif item.lower() == "нагантака прайм комплект":
    #     url_name = "nagantaka_prime_set"
    # elif item.lower() == "нагантака прайм ствол":
    #     url_name = "nagantaka_prime_barrel"
    # elif item.lower() == "нагантака прайм приемник":
    #     url_name = "nagantaka_prime_receiver"
    # elif item.lower() == "нагантака прайм приклад":
    #     url_name = "nagantaka_prime_stock"
    # elif item.lower() == "нагантака прайм чертеж":
    #     url_name = "nagantaka_prime_blueprint"

    # #Нами Скила
    # if item.lower() == "нами скила прайм сет":
    #     url_name = "nami_skyla_prime_set"
    # elif item.lower() == "нами скила прайм комплект":
    #     url_name = "nami_skyla_prime_set"
    # elif item.lower() == "нами скила прайм клинок":
    #     url_name = "nami_skyla_prime_blade"
    # elif item.lower() == "нами скила прайм рукоять":
    #     url_name = "nami_skyla_prime_handle"
    # elif item.lower() == "нами скила прайм чертеж":
    #     url_name = "nami_skyla_prime_blueprint"

    # #Никана
    # if item.lower() == "никана прайм сет":
    #     url_name = "nikana_prime_set"
    # elif item.lower() == "никана прайм комплект":
    #     url_name = "nikana_prime_set"
    # elif item.lower() == "никана прайм клинок":
    #     url_name = "nikana_prime_blade"
    # elif item.lower() == "никана прайм рукоять":
    #     url_name = "nikana_prime_hilt"
    # elif item.lower() == "никана прайм чертеж":
    #     url_name = "nikana_prime_blueprint"

    # #Нинконди
    # if item.lower() == "нинконди прайм сет":
    #     url_name = "ninkondi_prime_set"
    # elif item.lower() == "нинконди прайм комплект":
    #     url_name = "ninkondi_prime_set"
    # elif item.lower() == "нинконди прайм цепь":
    #     url_name = "ninkondi_prime_chain"
    # elif item.lower() == "нинконди прайм рукоять":
    #     url_name = "ninkondi_prime_handle"
    # elif item.lower() == "нинконди прайм чертеж":
    #     url_name = "ninkondi_prime_blueprint"

    # #Ортос
    # if item.lower() == "ортос прайм сет":
    #     url_name = "orthos_prime_set"
    # elif item.lower() == "ортос прайм комплект":
    #     url_name = "orthos_prime_set"
    # elif item.lower() == "ортос прайм клинок":
    #     url_name = "orthos_prime_blade"
    # elif item.lower() == "ортос прайм рукоять":
    #     url_name = "orthos_prime_handle"
    # elif item.lower() == "ортос прайм чертеж":
    #     url_name = "orthos_prime_blueprint"

    # #Панголин
    # if item.lower() == "панголин прайм сет":
    #     url_name = "pangolin_prime_set"
    # elif item.lower() == "панголин прайм комплект":
    #     url_name = "pangolin_prime_set"
    # elif item.lower() == "панголин прайм лезвие":
    #     url_name = "pangolin_prime_blade"
    # elif item.lower() == "панголин прайм рукоять":
    #     url_name = "pangolin_prime_handle"
    # elif item.lower() == "панголин прайм чертеж":
    #     url_name = "pangolin_prime_blueprint"

    # #Пандеро
    # if item.lower() == "пандеро прайм сет":
    #     url_name = "pandero_prime_set"
    # elif item.lower() == "пандеро прайм комплект":
    #     url_name = "pandero_prime_set"
    # elif item.lower() == "пандеро прайм ствол":
    #     url_name = "pandero_prime_barrel"
    # elif item.lower() == "пандеро прайм приемник":
    #     url_name = "pandero_prime_receiver"
    # elif item.lower() == "пандеро прайм чертеж":
    #     url_name = "pandero_prime_blueprint"

    # #Пантера
    # if item.lower() == "пантера прайм сет":
    #     url_name = "panthera_prime_set"
    # elif item.lower() == "пантера прайм комплект":
    #     url_name = "panthera_prime_set"
    # elif item.lower() == "пантера прайм ствол":
    #     url_name = "panthera_prime_barrel"
    # elif item.lower() == "пантера прайм приемник":
    #     url_name = "panthera_prime_receiver"
    # elif item.lower() == "пантера прайм приклад":
    #     url_name = "panthera_prime_stock"
    # elif item.lower() == "пантера прайм чертеж":
    #     url_name = "panthera_prime_blueprint"

    # #Парис
    # if item.lower() == "парис прайм сет":
    #     url_name = "paris_prime_set"
    # elif item.lower() == "парис прайм комплект":
    #     url_name = "paris_prime_set"
    # elif item.lower() == "парис прайм рукоять":
    #     url_name = "paris_prime_grip"
    # elif item.lower() == "парис прайм верхнее плечо":
    #     url_name = "paris_prime_upper_limb"
    # elif item.lower() == "парис прайм нижнее плечо":
    #     url_name = "paris_prime_lower_limb"
    # elif item.lower() == "парис прайм тетива":
    #     url_name = "paris_prime_string"
    # elif item.lower() == "парис прайм чертеж":
    #     url_name = "paris_prime_blueprint"

    # #Парные Камы
    # if item.lower() == "парные камы прайм сет":
    #     url_name = "dual_kamas_prime_set"
    # elif item.lower() == "парные камы прайм комплект":
    #     url_name = "dual_kamas_prime_set"
    # elif item.lower() == "парные камы прайм лезвие":
    #     url_name = "dual_kamas_prime_blade"
    # elif item.lower() == "парные камы прайм рукоять":
    #     url_name = "dual_kamas_prime_handle"
    # elif item.lower() == "парные камы прайм чертеж":
    #     url_name = "dual_kamas_prime_blueprint"

    # #Парные Кересы
    # if item.lower() == "парные кересы прайм сет":
    #     url_name = "dual_keres_prime_set"
    # elif item.lower() == "парные кересы прайм комплект":
    #     url_name = "dual_keres_prime_set"
    # elif item.lower() == "парные кересы прайм лезвие":
    #     url_name = "dual_keres_prime_blade"
    # elif item.lower() == "парные кересы прайм рукоять":
    #     url_name = "dual_keres_prime_handle"
    # elif item.lower() == "парные кересы прайм чертеж":
    #     url_name = "dual_keres_prime_blueprint"

    # #Пирана
    # if item.lower() == "пирана прайм сет":
    #     url_name = "pyrana_prime_set"
    # elif item.lower() == "пирана прайм комплект":
    #     url_name = "pyrana_prime_set"
    # elif item.lower() == "пирана прайм ствол":
    #     url_name = "pyrana_prime_barrel"
    # elif item.lower() == "пирана прайм приемник":
    #     url_name = "pyrana_prime_receiver"
    # elif item.lower() == "пирана прайм чертеж":
    #     url_name = "pyrana_prime_blueprint"

    # #Предвестник
    # if item.lower() == "предвестник прайм сет":
    #     url_name = "knell_prime_set"
    # elif item.lower() == "предвестник прайм комплект":
    #     url_name = "knell_prime_set"
    # elif item.lower() == "предвестник прайм ствол":
    #     url_name = "knell_prime_barrel"
    # elif item.lower() == "предвестник прайм приемник":
    #     url_name = "knell_prime_receiver"
    # elif item.lower() == "предвестник прайм чертеж":
    #     url_name = "knell_prime_blueprint"

    # #Сибарис
    # if item.lower() == "сибарис прайм сет":
    #     url_name = "sybaris_prime_set"
    # elif item.lower() == "сибарис прайм комплект":
    #     url_name = "sybaris_prime_set"
    # elif item.lower() == "сибарис прайм ствол":
    #     url_name = "sybaris_prime_barrel"
    # elif item.lower() == "сибарис прайм приклад":
    #     url_name = "sybaris_prime_stock"
    # elif item.lower() == "сибарис прайм приемник":
    #     url_name = "sybaris_prime_receiver"
    # elif item.lower() == "сибарис прайм чертеж":
    #     url_name = "sybaris_prime_blueprint"

    # #Сикарус
    # if item.lower() == "сикарус прайм сет":
    #     url_name = "sicarus_prime_set"
    # elif item.lower() == "сикарус прайм комплект":
    #     url_name = "sicarus_prime_set"
    # elif item.lower() == "сикарус прайм ствол":
    #     url_name = "sicarus_prime_barrel"
    # elif item.lower() == "сикарус прайм приемник":
    #     url_name = "sicarus_prime_receiver"
    # elif item.lower() == "сикарус прайм чертеж":
    #     url_name = "sicarus_prime_blueprint"

    # #Сильва и Эгида
    # if item.lower() == "сильва и эгида прайм сет":
    #     url_name = "silva_and_aegis_prime_set"
    # elif item.lower() == "сильва и эгида прайм комплект":
    #     url_name = "silva_and_aegis_prime_set"
    # elif item.lower() == "сильва и эгида прайм рукоять":
    #     url_name = "silva_and_aegis_prime_hilt"
    # elif item.lower() == "сильва и эгида прайм клинок":
    #     url_name = "silva_and_aegis_prime_blade"
    # elif item.lower() == "сильва и эгида прайм щит":
    #     url_name = "silva_and_aegis_prime_guard"
    # elif item.lower() == "сильва и эгида прайм чертеж":
    #     url_name = "silva_and_aegis_prime_blueprint"

    # #Сома
    # if item.lower() == "сома прайм сет":
    #     url_name = "soma_prime_set"
    # elif item.lower() == "сома прайм комплект":
    #     url_name = "soma_prime_set"
    # elif item.lower() == "сома прайм ствол":
    #     url_name = "soma_prime_barrel"
    # elif item.lower() == "сома прайм приемник":
    #     url_name = "soma_prime_receiver"
    # elif item.lower() == "сома прайм приклад":
    #     url_name = "soma_prime_stock"
    # elif item.lower() == "сома прайм чертеж":
    #     url_name = "soma_prime_blueprint"

    # #Спира
    # if item.lower() == "спира прайм сет":
    #     url_name = "spira_prime_set"
    # elif item.lower() == "спира прайм комплект":
    #     url_name = "spira_prime_set"
    # elif item.lower() == "спира прайм лезвие":
    #     url_name = "spira_prime_blade"
    # elif item.lower() == "спира прайм кисет":
    #     url_name = "spira_prime_pouch"
    # elif item.lower() == "спира прайм чертеж":
    #     url_name = "spira_prime_blueprint"

    # #Страдавар
    # if item.lower() == "страдавар прайм сет":
    #     url_name = "stradavar_prime_set"
    # elif item.lower() == "страдавар прайм комплект":
    #     url_name = "stradavar_prime_set"
    # elif item.lower() == "страдавар прайм ствол":
    #     url_name = "stradavar_prime_barrel"
    # elif item.lower() == "страдавар прайм приемник":
    #     url_name = "stradavar_prime_receiver"
    # elif item.lower() == "страдавар прайм приклад":
    #     url_name = "stradavar_prime_stock"
    # elif item.lower() == "страдавар прайм чертеж":
    #     url_name = "stradavar_prime_blueprint"

    # #Стран
    # if item.lower() == "стран прайм сет":
    #     url_name = "strun_prime_set"
    # elif item.lower() == "стран прайм комплект":
    #     url_name = "strun_prime_set"
    # elif item.lower() == "стран прайм ствол":
    #     url_name = "strun_prime_barrel"
    # elif item.lower() == "стран прайм приемник":
    #     url_name = "strun_prime_receiver"
    # elif item.lower() == "стран прайм приклад":
    #     url_name = "strun_prime_stock"
    # elif item.lower() == "стран прайм чертеж":
    #     url_name = "strun_prime_blueprint"

    # #Сциндо
    # if item.lower() == "сциндо прайм сет":
    #     url_name = "scindo_prime_set"
    # elif item.lower() == "сциндо прайм комплект":
    #     url_name = "scindo_prime_set"
    # elif item.lower() == "сциндо прайм клинок":
    #     url_name = "scindo_prime_blade"
    # elif item.lower() == "сциндо прайм рукоять":
    #     url_name = "scindo_prime_handle"
    # elif item.lower() == "сциндо прайм чертеж":
    #     url_name = "scindo_prime_blueprint"

    # #Тайберон
    # if item.lower() == "тайберон прайм сет":
    #     url_name = "tiberon_prime_set"
    # elif item.lower() == "тайберон прайм комплект":
    #     url_name = "tiberon_prime_set"
    # elif item.lower() == "тайберон прайм ствол":
    #     url_name = "tiberon_prime_barrel"
    # elif item.lower() == "тайберон прайм приемник":
    #     url_name = "tiberon_prime_receiver"
    # elif item.lower() == "тайберон прайм приклад":
    #     url_name = "tiberon_prime_stock"
    # elif item.lower() == "тайберон прайм чертеж":
    #     url_name = "tiberon_prime_blueprint"

    # #Татсу
    # if item.lower() == "татсу прайм сет":
    #     url_name = "tatsu_prime_set"
    # elif item.lower() == "татсу прайм комплект":
    #     url_name = "tatsu_prime_set"
    # elif item.lower() == "татсу прайм лезвие":
    #     url_name = "tatsu_prime_blade"
    # elif item.lower() == "татсу прайм рукоять":
    #     url_name = "tatsu_prime_handle"
    # elif item.lower() == "татсу прайм чертеж":
    #     url_name = "tatsu_prime_blade"

    # #Тенора
    # if item.lower() == "тенора прайм сет":
    #     url_name = "tenora_prime_set"
    # elif item.lower() == "тенора прайм комплект":
    #     url_name = "tenora_prime_set"
    # elif item.lower() == "тенора прайм ствол":
    #     url_name = "tenora_prime_barrel"
    # elif item.lower() == "тенора прайм приемник":
    #     url_name = "tenora_prime_receiver"
    # elif item.lower() == "тенора прайм приклад":
    #     url_name = "tenora_prime_stock"
    # elif item.lower() == "тенора прайм чертеж":
    #     url_name = "tenora_prime_blueprint"

    # #Тигрис
    # if item.lower() == "тигрис прайм сет":
    #     url_name = "tigris_prime_set"
    # elif item.lower() == "тигрис прайм комплект":
    #     url_name = "tigris_prime_set"
    # elif item.lower() == "тигрис прайм ствол":
    #     url_name = "tigris_prime_barrel"
    # elif item.lower() == "тигрис прайм приемник":
    #     url_name = "tigris_prime_receiver"
    # elif item.lower() == "тигрис прайм приклад":
    #     url_name = "tigris_prime_stock"
    # elif item.lower() == "тигрис прайм чертеж":
    #     url_name = "tigris_prime_blueprint"

    # #Тэкко
    # if item.lower() == "тэкко прайм сет":
    #     url_name = "tekko_prime_set"
    # elif item.lower() == "тэкко прайм комплект":
    #     url_name = "tekko_prime_set"
    # elif item.lower() == "тэкко прайм лезвие":
    #     url_name = "tekko_prime_blade"
    # elif item.lower() == "тэкко прайм перчатка":
    #     url_name = "tekko_prime_gauntlet"
    # elif item.lower() == "тэкко прайм чертеж":
    #     url_name = "tekko_prime_blueprint"

    # #Фантазма
    # if item.lower() == "фантазма прайм сет":
    #     url_name = "phantasma_prime_set"
    # elif item.lower() == "фантазма прайм комплект":
    #     url_name = "phantasma_prime_set"
    # elif item.lower() == "фантазма прайм ствол":
    #     url_name = "phantasma_prime_barrel"
    # elif item.lower() == "фантазма прайм приемник":
    #     url_name = "phantasma_prime_receiver"
    # elif item.lower() == "фантазма прайм приклад":
    #     url_name = "phantasma_prime_stock"
    # elif item.lower() == "фантазма прайм чертеж":
    #     url_name = "phantasma_prime_blueprint"

    # #Фрагор
    # if item.lower() == "фрагор прайм сет":
    #     url_name = "fragor_prime_set"
    # elif item.lower() == "фрагор прайм комплект":
    #     url_name = "fragor_prime_set"
    # elif item.lower() == "фрагор прайм рукоять":
    #     url_name = "fragor_prime_handle"
    # elif item.lower() == "фрагор прайм молот":
    #     url_name = "fragor_prime_head"
    # elif item.lower() == "фрагор прайм чертеж":
    #     url_name = "fragor_prime_blueprint"

    # #Хико
    # if item.lower() == "хико прайм сет":
    #     url_name = "hikou_prime_set"
    # elif item.lower() == "хико прайм комплект":
    #     url_name = "hikou_prime_set"
    # elif item.lower() == "хико прайм сюрикены":
    #     url_name = "hikou_prime_stars"
    # elif item.lower() == "хико прайм кисет":
    #     url_name = "hikou_prime_pouch"
    # elif item.lower() == "хико прайм чертеж":
    #     url_name = "hikou_prime_blueprint"

    # #Хистрикс
    # if item.lower() == "хистрикс прайм сет":
    #     url_name = "hystrix_prime_set"
    # elif item.lower() == "хистрикс прайм комплект":
    #     url_name = "hystrix_prime_set"
    # elif item.lower() == "хистрикс прайм ствол":
    #     url_name = "hystrix_prime_barrel"
    # elif item.lower() == "хистрикс прайм приемник":
    #     url_name = "hystrix_prime_receiver"
    # elif item.lower() == "хистрикс прайм чертеж":
    #     url_name = "hystrix_prime_blueprint"

    # #Чжугэ
    # if item.lower() == "чжугэ прайм сет":
    #     url_name = "zhuge_prime_set"
    # elif item.lower() == "чжугэ прайм комплект":
    #     url_name = "zhuge_prime_set"
    # elif item.lower() == "чжугэ прайм приемник":
    #     url_name = "zhuge_prime_receiver"
    # elif item.lower() == "чжугэ прайм ствол":
    #     url_name = "zhuge_prime_barrel"
    # elif item.lower() == "чжугэ прайм рукоять":
    #     url_name = "zhuge_prime_grip"
    # elif item.lower() == "чжугэ прайм тетива":
    #     url_name = "zhuge_prime_string"
    # elif item.lower() == "чжугэ прайм чертеж":
    #     url_name = "zhuge_prime_blueprint"

    # #Юфона
    # if item.lower() == "юфона прайм сет":
    #     url_name = "euphona_prime_set"
    # elif item.lower() == "юфона прайм комплект":
    #     url_name = "euphona_prime_set"
    # elif item.lower() == "юфона прайм ствол":
    #     url_name = "euphona_prime_barrel"
    # elif item.lower() == "юфона прайм приемник":
    #     url_name = "euphona_prime_receiver"
    # elif item.lower() == "юфона прайм чертеж":
    #     url_name = "euphona_prime_blueprint"


    return url_name


def collect_titles_of_item(item):
    url_name = warframes_to_url(item)
    r = requests.get(f"https://api.warframe.market/v1/items/{url_name}")
    r_json = r.json()

    # with open('data.json', 'w') as file:
    #     json.dump(r_json, file, indent=4, ensure_ascii=True)

    #Атлас
    if item.lower() == "атлас прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "атлас прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "атлас прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "атлас прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "атлас прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "атлас прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]

    #Банши
    if item.lower() == "банши прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "банши прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "банши прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "банши прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "банши прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "банши прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Валькирия
    if item.lower() == "валькирия прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "валькирия прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "валькирия прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "валькирия прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "валькирия прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "валькирия прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Вобан
    if item.lower() == "вобан прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "вобан прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "вобан прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "вобан прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "вобан прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "вобан прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Вольт
    if item.lower() == "вольт прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "вольт прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "вольт прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "вольт прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "вольт прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "вольт прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]

    #Вуконг
    if item.lower() == "вуконг прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "вуконг прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "вуконг прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "вуконг прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "вуконг прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "вуконг прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]

    #Гара
    if item.lower() == "гара прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "гара прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "гара прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "гара прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "гара прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "гара прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Гаруда
    if item.lower() == "гаруда прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "гаруда прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "гаруда прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "гаруда прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "гаруда прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "гаруда прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]

    #Гидроид
    if item.lower() == "гидроид прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "гидроид прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "гидроид прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "гидроид прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "гидроид прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "гидроид прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Зефир
    if item.lower() == "зефир прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "зефир прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "зефир прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "зефир прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "зефир прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "зефир прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]


    #Ивара
    if item.lower() == "ивара прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "ивара прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "ивара прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "ивара прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "ивара прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "ивара прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Инарос
    if item.lower() == "инарос прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "инарос прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "инарос прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "инарос прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "инарос прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "инарос прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]

    #Кора
    if item.lower() == "кора прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "кора прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "кора прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "кора прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "кора прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "кора прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]

    #Лимбо
    if item.lower() == "лимбо прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "лимбо прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "лимбо прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "лимбо прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "лимбо прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "лимбо прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Локи
    if item.lower() == "локи прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "локи прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "локи прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "локи прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "локи прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "локи прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]

    #Мираж
    if item.lower() == "мираж прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "мираж прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "мираж прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "мираж прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "мираж прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "мираж прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]

    #Миса
    if item.lower() == "миса прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "миса прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "миса прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "миса прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "миса прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "миса прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]

    #Мэг
    if item.lower() == "мэг прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "мэг прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "мэг прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "мэг прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "мэг прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "мэг прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]

    #Некрос
    if item.lower() == "некрос прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "некрос прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "некрос прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "некрос прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "некрос прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "некрос прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]

    #Нидус
    if item.lower() == "нидус прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "нидус прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "нидус прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "нидус прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "нидус прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "нидус прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Никс
    if item.lower() == "никс прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "никс прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "никс прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "никс прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "никс прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "никс прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]

    #Нова
    if item.lower() == "нова прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "нова прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "нова прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "нова прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "нова прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "нова прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]

    #Нэчжа
    if item.lower() == "нэчжа прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "нэчжа прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "нэчжа прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "нэчжа прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "нэчжа прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "нэчжа прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Оберон
    if item.lower() == "оберон прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "оберон прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "оберон прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "оберон прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "оберон прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "оберон прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Октавия
    if item.lower() == "октавия прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "октавия прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "октавия прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "октавия прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "октавия прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "октавия прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Ревенант
    if item.lower() == "ревенант прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "ревенант прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "ревенант прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "ревенант прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "ревенант прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "ревенант прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]

    #Рино
    if item.lower() == "рино прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "рино прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "рино прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "рино прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "рино прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "рино прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]

    #Сарина
    if item.lower() == "сарина прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "сарина прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "сарина прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "сарина прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "сарина прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "сарина прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Титания
    if item.lower() == "титания прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "титания прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "титания прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "титания прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "титания прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "титания прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]

    #Тринити
    if item.lower() == "тринити прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "тринити прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "тринити прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "тринити прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "тринити прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "тринити прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Фрост
    if item.lower() == "фрост прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "фрост прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "фрост прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "фрост прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "фрост прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "фрост прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]

    #Харроу
    if item.lower() == "харроу прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "харроу прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "харроу прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "харроу прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "харроу прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "харроу прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    #Хрома
    if item.lower() == "хрома прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "хрома прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "хрома прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "хрома прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "хрома прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "хрома прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]

    #Эквинокс
    if item.lower() == "эквинокс прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "эквинокс прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "эквинокс прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "эквинокс прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "эквинокс прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "эквинокс прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]

    #Эмбер
    if item.lower() == "эмбер прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "эмбер прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "эмбер прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "эмбер прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "эмбер прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]
    elif item.lower() == "эмбер прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]

    #Эш
    if item.lower() == "эш прайм сет":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "эш прайм комплект":
        item_name = r_json["payload"]["item"]["items_in_set"][4]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][4]["en"]["item_name"]
    elif item.lower() == "эш прайм каркас":
        item_name = r_json["payload"]["item"]["items_in_set"][1]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][1]["en"]["item_name"]
    elif item.lower() == "эш прайм система":
        item_name = r_json["payload"]["item"]["items_in_set"][2]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][2]["en"]["item_name"]
    elif item.lower() == "эш прайм нейрооптика":
        item_name = r_json["payload"]["item"]["items_in_set"][3]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][3]["en"]["item_name"]
    elif item.lower() == "эш прайм чертеж":
        item_name = r_json["payload"]["item"]["items_in_set"][0]["ru"]["item_name"]
        item_name_en = r_json["payload"]["item"]["items_in_set"][0]["en"]["item_name"]

    print(item_name)
    return item_name, item_name_en