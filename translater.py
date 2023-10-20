import json
import requests

from langcodes import Language


DEEPL_LANGUAGES = [
    "BG",
    "CS",
    "DA",
    "DE",
    "EL",
    "EN",
    "ES",
    "ET",
    "FI",
    "FR",
    "HU",
    "ID",
    "IT",
    "JA",
    "LT",
    "LV",
    "NB",
    "NL",
    "PL",
    "PT",
    "RO",
    "RU",
    "SK",
    "SL",
    "SV",
    "TR",
    "UK",
    "ZH",
]


def DeepL(text, source, target, API_KEY):
    URL = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"DeepL-Auth-Key {API_KEY}",
    }
    data = {
        "text": [text] if type(text) == str else text,
        "source_lang": source,
        "target_lang": target,
    }
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    return response.json()["translations"][0]["text"]


def DeepL_to_i18n(lang_code: str):
    language = Language.get(lang_code)
    return str(Language.find(language.display_name()))


def need():
    with open("i18n/_default.json", "r", encoding="UTF-8") as f:
        default_lang = json.loads(f.read())
    
    for lang in DEEPL_LANGUAGES:
        target_lang = DeepL_to_i18n(lang)

        try:
            with open(f"i18n/{target_lang}.json", "r", encoding="UTF-8") as f:
                target_lang = json.loads(f.read())
        except Exception:
            return True

        if (
            sorted(default_lang.keys()) == sorted(target_lang.keys())
        ):
            return False
        else:
            return True


def main(API_KEY):
    with open("i18n/_default.json", "r", encoding="UTF-8") as f:
        default_lang = json.loads(f.read())

    for lang in DEEPL_LANGUAGES:
        translated = {}
        target_lang = DeepL_to_i18n(lang)

        print(f"{target_lang} - DeepL로 번역 중...")

        for key, vaule in default_lang.items():
            translated[key] = DeepL(vaule, "KO", target_lang, API_KEY)
            print(f"{target_lang}: {vaule} -> {translated[key]}")

        with open(f"i18n/{target_lang}.json", "w", encoding="UTF-8") as f:
            json.dump(translated, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main("API_KEY HERE")
