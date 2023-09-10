import os
import json

from typing import Union

from langcodes import Language, standardize_tag


langs = []


def _get_name_from_code(language_code: str, target_code: str = "ko") -> tuple:
    """언어 코드를 기반으로 언어 이름을 가져옵니다.

    Args:
        language_code (str): 언어 코드

    Returns:
        tuple: (현지 이름, 번역 이름)
    """
    language = Language.make(language_code)
    language_local = language.display_name(language_code)
    language_translated = language.display_name(target_code)
    return (language_local, language_translated)


def _get_code_from_name(language_name: str) -> str:
    """언어 이름을 기반으로 언어 코드를 가져옵니다.

    Args:
        language_name (str): 언어 이름

    Returns:
        str: 언어 코드
    """
    language = Language.find(language_name)
    return str(language)


def _get_code_from_tag(language_tag: str) -> str:
    """언어 태그를 기반으로 언어 코드를 가져옵니다.

    Args:
        language_get_code_from_tag (str): 언어 태그

    Returns:
        str: 언어 코드
    """
    language = Language.get(language_tag)
    return language.language


def _load(language_code: str) -> dict:
    """언어 코드를 기반으로 언어 파일을 불러옵니다.

    Args:
        language_code (str): 언어 코드

    Returns:
        dict: 언어 파일 데이터
    """
    languages_folder = os.path.dirname(__file__)
    target_file = f"{language_code}.json"
    path = os.path.join(languages_folder, target_file)

    assert os.path.exists(path), f"File {target_file} not found"

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def DisplayLang(lang_code: str) -> str:
    """언어 코드를 기반으로 표시될 언어 이름을 불러옵니다.

    Args:
        lang_code (str): 언어 코드

    Returns:
        str: 표시될 언어 이름
    """
    local, translated = _get_name_from_code(lang_code)
    return f"{local} ({translated})"


def FindLangByName(lang_name: str) -> str:
    """언어 이름을 기반으로 언어 코드를 불러옵니다.

    Args:
        lang_name (str): 언어 이름

    Returns:
        str: 언어 코드
    """
    return _get_code_from_name(lang_name)


def FindLangByTag(lang_tag: str) -> str:
    """언어 태그를 기반으로 언어 코드를 불러옵니다.

    Args:
        lang_name (str): 언어 태그

    Returns:
        str: 언어 코드
    """
    return _get_code_from_tag(lang_tag)


def LoadLangByName(lang_name: str) -> dict:
    """언어 이름을 기반으로 언어 파일을 불러옵니다.

    Args:
        lang_name (str): 언어 이름

    Returns:
        dict: 언어 파일 데이터
    """
    return _load(FindLangByName(lang_name))


def LoadLangByCode(lang_name: str) -> dict:
    """언어 코드를 기반으로 언어 파일을 불러옵니다.

    Args:
        lang_name (str): 언어 코드

    Returns:
        dict: 언어 파일 데이터
    """
    return _load(lang_name)


def LangList(value: Union[str, None] = None) -> dict:
    """언어 목록을 불러옵니다.

    Args:
        value (Union[str, None], optional): 언어 코드. 기본값은 None.

    Returns:
        dict: 언어 목록
    """
    langlist = {}
    for language in langs:
        code = language["code"]
        langlist[DisplayLang(code)] = code

    if value is not None:
        return langlist[value]
    return langlist


def main() -> None:
    global langs
    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith(".json") and not file.startswith("_"):
            lang = file[:-5]
            langs.append(
                {
                    "code": lang,
                    "local": _get_name_from_code(lang)[0],
                    "translated": _get_name_from_code(lang)[1],
                }
            )


main()
