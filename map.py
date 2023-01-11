# ターミナルでfoliumのインポート
# 参考ULR：https://welovepython.net/streamlit-folium/
import streamlit as st                      # streamlit
from streamlit_folium import st_folium      # streamlitでfoliumを使う
import folium                               # folium
from folium import FeatureGroup             # FeatureGrop
import pandas as pd                         # CSVをデータフレームとして読み込む

# 表示するデータを読み込み
df = pd.read_csv("221218-2025_hotpepper_beer.csv")

# 必要なデータのみに絞り込む
df = df[["menu", "price", "genre", "name", "lat", "lng", "url"]]

# 銘柄ごとのデータを抽出
_all_data = df.loc[df.groupby("name")["price"].idxmin()]
all_data = (_all_data[_all_data["menu"].str.contains("モルツ|アサヒ|ヱビス|キリン|ヒューガルデン|コロナ|ギネス")]) #全銘柄
mlts_data = df[df["menu"].str.contains("モルツ")]
asahi_data = df[df["menu"].str.contains("アサヒ")]
ebis_data = df[df["menu"].str.contains("ヱビス")]
kirin_data = df[df["menu"].str.contains("キリン")]
hoeg_data = df[df["menu"].str.contains("ヒューガルデン")]
corona_data = df[df["menu"].str.contains("コロナ")]
guinness_data = df[df["menu"].str.contains("ギネス")]

# 最安値
all_min_price = df["price"].min()
mlts_min_price = mlts_data["price"].min()
asahi_min_price = df["price"].min()
ebis_min_price = ebis_data["price"].min()
kirin_min_price = kirin_data["price"].min()
hoeg_min_price = hoeg_data["price"].min()
corona_min_price = corona_data["price"].min()
guinness_min_price = guinness_data["price"].min()

# 平均価格
all_mean_price = int(df["price"].mean())
mlts_mean_price = int(mlts_data["price"].mean())
asahi_mean_price = int(asahi_data["price"].mean())
ebis_mean_price = int(ebis_data["price"].mean())
kirin_mean_price = int(kirin_data["price"].mean())
hoeg_mean_price = int(hoeg_data["price"].mean())
corona_mean_price = int(corona_data["price"].mean())
guinness_mean_price = int(guinness_data["price"].mean())

# >>> Streamlit タイトル >>>
st.header("梅田駅の近くでビールを飲もう！:beers:")
st.text("""
        左に表示されているプルダウンから好きな銘柄を選んでください。
        選んだ銘柄を提供しているお店が地図上に表示されます。
        """)
# <<< Streamlit タイトル <<<

# >>> Streamlit サイドバー >>>
# セレクトボックス
bland_options = st.sidebar.selectbox(
    "ご希望のビール銘柄をお選びください。",
    ["全銘柄", "モルツ", "アサヒ", "ヱビス", "キリン", "ヒューガルデン", "コロナ", "ギネス"])
st.sidebar.write("現在の選択:", bland_options)

# スライダー
# price_slider = st.sidebar.slider(
#     "1杯の値段で絞り込みができます",
#     min_value = 100,
#     max_value = 1000,
#     value = 500,
#     step = 10,
#     )
# st.sidebar.write("希望価格：100円～", price_slider, "円です。")

if bland_options == "全銘柄":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = all_min_price,
        max_value = 1000,
        value = 500,
        step = 10,
        )
    st.sidebar.write("希望価格：",all_min_price,"円～", price_slider, "円です。")

if bland_options == "モルツ":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = mlts_min_price,
        max_value = 1000,
        value = 500,
        step = 10,
        )
    st.sidebar.write("希望価格：",mlts_min_price,"円～", price_slider, "円です。")

if bland_options == "アサヒ":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = asahi_min_price,
        max_value = 1000,
        value = 500,
        step = 10,
        )
    st.sidebar.write("希望価格：",asahi_min_price,"円～", price_slider, "円です。")

if bland_options == "ヱビス":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = ebis_min_price,
        max_value = 1000,
        value = 500,
        step = 10,
        )
    st.sidebar.write("希望価格：",ebis_min_price,"円～", price_slider, "円です。")
    
if bland_options == "キリン":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = kirin_min_price,
        max_value = 1000,
        value = 500,
        step = 10,
        )
    st.sidebar.write("希望価格：",kirin_min_price,"円～", price_slider, "円です。")

if bland_options == "ヒューガルデン":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = hoeg_min_price,
        max_value = 1500,
        value = 900,
        step = 10,
        )
    st.sidebar.write("希望価格：",hoeg_min_price,"円～", price_slider, "円です。")

if bland_options == "コロナ":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = corona_min_price,
        max_value = 1500,
        value = 900,
        step = 10,
        )
    st.sidebar.write("希望価格：",corona_min_price,"円～", price_slider, "円です。")

if bland_options == "ギネス":
    price_slider = st.sidebar.slider(
        "1杯の値段で絞り込みができます",
        min_value = guinness_min_price,
        max_value = 1200,
        value = 800,
        step = 10,
        )
    st.sidebar.write("希望価格：",guinness_min_price,"円～", price_slider, "円です。")


# 銘柄の価格のデータを抽出
all_prices = all_data[all_data["price"] <= price_slider]
mlts_prices = mlts_data[mlts_data["price"] <= price_slider]
asahi_prices = asahi_data[asahi_data["price"] <= price_slider]
ebis_prices = ebis_data[ebis_data["price"] <= price_slider]
kirin_prices = kirin_data[kirin_data["price"] <= price_slider]
hoeg_prices = hoeg_data[hoeg_data["price"] <= price_slider]
corona_prices = corona_data[corona_data["price"] <= price_slider]
guinness_prices = guinness_data[guinness_data["price"] <= price_slider]
# <<< Streamlit サイドバー <<<

# >>> 全店舗（all_map) >>>
# 全銘柄（all_map)：地図の中心の緯度/経度、タイル、初期のズームサイズを指定
all_map = folium.Map(
    # 地図の中心位置の指定(今回は大梅田駅を指定)
    location=[34.7055051, 135.4983028],
    # タイル（デフォルトはOpenStreetMap)、アトリビュート(attr:右下の出典情報はデフォルト指定時は不要)指定
    tiles="OpenStreetMap",
    # ズームを指定
    # 参考URL：https://maps.gsi.go.jp/development/ichiran.html#pale
    zoom_start=15
)

#全銘柄の層を作成
all_group = FeatureGroup(name="全銘柄")

# darkblueのマーカーを全銘柄の座標に差し、グループに追加
all_markers = []

for i, row in all_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="darkblue"))
    all_markers.append(marker)

for marker in all_markers:
    marker.add_to(all_group)
# <<< 全店舗（all_map) <<<

# >>> モルツマップ（mlts_map) >>>
mlts_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
mlts_group = FeatureGroup(name="モルツ")

mlts_markers = []

for i, row in mlts_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="blue"))
    mlts_markers.append(marker)

for marker in mlts_markers:
    marker.add_to(mlts_group)
# <<< モルツマップ（mlts_map) <<<

# >>> アサヒマップ(asahi_map) >>>
asahi_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
asahi_group = FeatureGroup(name="アサヒ")

asahi_markers = []

for i, row in asahi_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="gray"))
    asahi_markers.append(marker)

for marker in asahi_markers:
    marker.add_to(asahi_group)
# <<< アサヒマップ(asahi_map) <<<

# >>> ヱビスマップ（ebis_map) >>>
ebis_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
ebis_group = FeatureGroup(name="ヱビス")

ebis_markers = []

for i, row in ebis_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="orange"))
    ebis_markers.append(marker)

for marker in ebis_markers:
    marker.add_to(ebis_group)
# <<< ヱビスマップ（ebis_map) <<<

# >>> キリン（kirin_map) >>>
kirin_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
kirin_group = FeatureGroup(name="キリン")

kirin_markers = []

for i, row in kirin_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="lightred"))
    kirin_markers.append(marker)

for marker in kirin_markers:
    marker.add_to(kirin_group)
# <<< キリン（kirin_map) <<<

# >>> ヒューガルデンマップ（hoeg_map) >>>
hoeg_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
hoeg_group = FeatureGroup(name="ヒューガルデン")

hoeg_markers = []

for i, row in hoeg_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="gray", color="white"))
    hoeg_markers.append(marker)

for marker in hoeg_markers:
    marker.add_to(hoeg_group)
# <<< ヒューガルデンマップ（hoeg_map) <<<

# >>> コロナマップ（corona_map) >>>
corona_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
corona_group = FeatureGroup(name="コロナ")

corona_markers = []

for i, row in corona_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="beige"))
    corona_markers.append(marker)

for marker in corona_markers:
    marker.add_to(corona_group)
# <<< コロナマップ（corona_map) <<<

# >>> ギネスマップ（guinness_map) >>>
guinness_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
guinness_group = FeatureGroup(name="ギネス")

guinness_markers = []

for i, row in guinness_prices.iterrows():
    lat = row["lat"]
    lng = row["lng"]
    genre = row["genre"]
    name = row["name"]
    url = row["url"]
    menu = row["menu"]
    price = row["price"]
    popup = f"<div style='width:300px'>【{genre}】<br><b>{name}</b><br>{menu}: <b>{price}円</b><br><a href='{url}' target='_blank'>&#x1f37a; ホットペッパーグルメで確認 &#x1f37a;</a></div>"
    marker = folium.Marker([lat, lng], tooltip=name, popup=popup, icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="black"))
    guinness_markers.append(marker)

for marker in guinness_markers:
    marker.add_to(guinness_group)
# <<< ギネスマップ（guinness_map) <<<

# 各銘柄を地図に追加
all_group.add_to(all_map)
mlts_group.add_to(mlts_map)
asahi_group.add_to(asahi_map)
ebis_group.add_to(ebis_map)
kirin_group.add_to(kirin_map)
hoeg_group.add_to(hoeg_map)
corona_group.add_to(corona_map)
guinness_group.add_to(guinness_map)

# >>> Streamlit サイドバー & Map >>>
if bland_options == "全銘柄":
    st.subheader(":beer: ビール が飲めるお店")
    st_folium(all_map, width=700, height=700)
    st.sidebar.write("大阪市北区のビール1杯の最安値は、", all_min_price, "円です")
    st.sidebar.write("大阪市北区のビール1杯の平均価格は、", all_mean_price, "円です")

if bland_options == "モルツ":
    st.subheader(":beer: モルツ が飲めるお店")
    st_folium(mlts_map, width=700, height=700)
    st.sidebar.write("大阪市北区のモルツビール1杯の最安値は、", mlts_min_price, "円です")
    st.sidebar.write("大阪市北区のモルツビール1杯の平均価格は、", mlts_mean_price, "円です")

if bland_options == "アサヒ":
    st.subheader(":beer: アサヒ が飲めるお店")
    st_folium(asahi_map, width=700, height=700)
    st.sidebar.write("大阪市北区のアサヒビール1杯の最安値は、", asahi_min_price, "円です")
    st.sidebar.write("大阪市北区のアサヒビール1杯の平均価格は、", asahi_mean_price, "円です")

if bland_options == "ヱビス":
    st.subheader(":beer: ヱビス が飲めるお店")
    st_folium(ebis_map, width=700, height=700)
    st.sidebar.write("大阪市北区のヱビス1杯の最安値は、", ebis_min_price, "円です")
    st.sidebar.write("大阪市北区のヱビスビール1杯の平均価格は、", ebis_mean_price, "円です")

if bland_options == "キリン":
    st.subheader(":beer: キリン が飲めるお店")
    st_folium(kirin_map, width=700, height=700)
    st.sidebar.write("大阪市北区のキリン1杯の最安値は、", kirin_min_price, "円です")
    st.sidebar.write("大阪市北区のキリン1杯の平均価格は、", kirin_mean_price, "円です")

if bland_options == "ヒューガルデン":
    st.subheader(":beer: ヒューガルデン が飲めるお店")
    st_folium(hoeg_map, width=700, height=700)
    st.sidebar.write("大阪市北区のヒューガルデン1杯の最安値は、", hoeg_min_price, "円です")
    st.sidebar.write("大阪市北区のヒューガルデン1杯の平均価格は、", hoeg_mean_price, "円です")

if bland_options == "コロナ":
    st.subheader(":beer: コロナビール が飲めるお店")
    st_folium(corona_map, width=700, height=700)
    st.sidebar.write("大阪市北区のコロナビール1杯の最安値は、", corona_min_price, "円です")
    st.sidebar.write("大阪市北区のコロナビール1杯の平均価格は、", corona_mean_price, "円です")

if bland_options == "ギネス":
    st.subheader(":beer: ギネスビール が飲めるお店")
    st_folium(guinness_map, width=700, height=700)
    st.sidebar.write("大阪市北区のギネスビール1杯の最安値は、", guinness_min_price, "円です")
    st.sidebar.write("大阪市北区のギネスビール1杯の平均価格は、", guinness_mean_price, "円です")
# <<< Streamlit サイドバー & Map <<<
