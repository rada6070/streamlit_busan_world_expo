import os
import types

from PIL import Image


assets = {}


def import_assets(exist: str, st: types.ModuleType) -> None:
    if not os.path.exists(exist):
        raise FileNotFoundError(f"File {exist} not found")

    with open(exist, "r", encoding="UTF-8") as f:
        asset_data = f.read()

    html = "<{tag}>{content}</{tag}>"

    extension = exist.split(".")[-1]
    if extension == "css":
        html = html.format(tag="style", content=asset_data)
    if extension == "js":
        html = html.format(tag="script", content=asset_data)

    st.markdown(
        html,
        unsafe_allow_html=True,
    )


__assets = os.path.dirname(__file__)
for file in os.listdir(os.path.dirname(__file__)):
    path = os.path.join(__assets, file)
    if file[:-3] in ["jpg", "png"]:
        with open(path, "rb") as f:
            assets[file[:-4]] = Image.open(path)
