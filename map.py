# ターミナルでfoliumのインポート
# 参考ULR：https://welovepython.net/streamlit-folium/
import streamlit as st                      # streamlit
from streamlit_folium import st_folium      # streamlitでfoliumを使う
import folium                               # folium
from folium import FeatureGroup             # FeatureGrop
import pandas as pd                         # CSVをデータフレームとして読み込む


#  表示するデータを読み込み
df = pd.read_csv("221218-2025_hotpepper_beer.csv")

# >>> Streamlit サイドバー >>>
# セレクトボックス
bland_options = st.sidebar.selectbox(
    "ご希望のビール銘柄をお選びください。",
    # ["モルツ", "アサヒ", "ヱビス", "キリン", "ヒューガルデン", "コロナ", "ギネス" ,"全銘柄", "プレミアム"])
    ["モルツ", "アサヒ", "ヱビス", "キリン", "ヒューガルデン", "コロナ", "ギネス" ,"全銘柄"])
st.sidebar.write("現在の選択:", bland_options)

# スライダー
price_slider = st.sidebar.slider(
    "1杯の値段で絞り込みができます",
    min_value = 100,
    max_value = 1000,
    value = 500,
    step = 10,
    )
st.sidebar.write("希望価格：100円～", price_slider, "円です。")
# <<< Streamlit サイドバー <<<

# 銘柄でのデータを抽出
# all_data = (df[df["menu"].str.contains("モルツ|アサヒ|ヱビス|キリン|ヒューガルデン|コロナ|ギネス|プレミアム")]) #全銘柄
all_data = (df[df["menu"].str.contains("モルツ|アサヒ|ヱビス|キリン|ヒューガルデン|コロナ|ギネス")]) #全銘柄
mlts_data = df[df["menu"].str.contains("モルツ")]
asahi_data = df[df["menu"].str.contains("アサヒ")]
ebis_data = df[df["menu"].str.contains("ヱビス")]
kirin_data = df[df["menu"].str.contains("キリン")]
hoeg_data = df[df["menu"].str.contains("ヒューガルデン")]
corona_data = df[df["menu"].str.contains("コロナ")]
guinness_data = df[df["menu"].str.contains("ギネス")]
# premium_data = df[df["menu"].str.contains("プレミアム")]

# 銘柄の価格のデータを抽出
all_prices = all_data[all_data["price"] <= price_slider]
mlts_prices = mlts_data[mlts_data["price"] <= price_slider]
asahi_prices = asahi_data[asahi_data["price"] <= price_slider]
ebis_prices = ebis_data[ebis_data["price"] <= price_slider]
kirin_prices = kirin_data[kirin_data["price"] <= price_slider]
hoeg_prices = hoeg_data[hoeg_data["price"] <= price_slider]
corona_prices = corona_data[corona_data["price"] <= price_slider]
guinness_prices = guinness_data[guinness_data["price"] <= price_slider]
# premium_prices = premium_data[premium_data["price"] <= price_slider]

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
for i, row in all_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="darkblue")
    ).add_to(all_group)
# <<< 全店舗（all_map) <<<

# >>> モルツマップ（mlts_map) >>>
mlts_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
mlts_group = FeatureGroup(name="モルツ")

for i, row in mlts_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="blue")
    ).add_to(mlts_group)
# <<< モルツマップ（mlts_map) <<<

# >>> アサヒマップ(asahi_map) >>>
asahi_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
asahi_group = FeatureGroup(name="アサヒ")

for i, row in asahi_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="gray")
    ).add_to(asahi_group)
# <<< アサヒマップ(asahi_map) <<<

# >>> キリン（kirin_map) >>>
kirin_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
kirin_group = FeatureGroup(name="キリン")

for i, row in kirin_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="lightred")
    ).add_to(kirin_group)
# <<< キリン（kirin_map) <<<

# >>> ヱビスマップ（ebis_map) >>>
ebis_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
ebis_group = FeatureGroup(name="ヱビス")

for i, row in ebis_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="orange")
    ).add_to(ebis_group)
# <<< ヱビスマップ（ebis_map) <<<

# >>> ヒューガルデンマップ（hoeg_map) >>>
hoeg_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
hoeg_group = FeatureGroup(name="ヒューガルデン")

for i, row in hoeg_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="gray", color="white")
    ).add_to(hoeg_group)
# <<< ヒューガルデンマップ（hoeg_map) <<<

# >>> コロナマップ（corona_map) >>>
corona_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
corona_group = FeatureGroup(name="コロナ")

for i, row in corona_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="beige")
    ).add_to(corona_group)
# <<< コロナマップ（corona_map) <<<

# >>> ギネスマップ（guinness_map) >>>
guinness_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
guinness_group = FeatureGroup(name="ギネス")

for i, row in guinness_prices.iterrows():
    folium.Marker(
        location=[row["lat"], row["lng"]],
        popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
        icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="black")
    ).add_to(guinness_group)
# <<< ギネスマップ（guinness_map) <<<

# # >>> プレミアムマップ（premium_map) >>>
# premium_map = folium.Map(location=[34.7055051, 135.4983028], tiles="OpenStreetMap", zoom_start=15)
# premium_group = FeatureGroup(name="プレミアム")

# for i, row in premium_prices.iterrows():
#     folium.Marker(
#         location=[row["lat"], row["lng"]],
#         popup=row["name"] + "<br>【ジャンル】" + row["genre"] + "</br>" + row["url"],
#         icon=folium.Icon(icon="beer", prefix="fa", icon_color="white", color="darkred")
#     ).add_to(premium_group)
# # <<< プレミアムマップ（premium_map) <<<



# 各銘柄を地図に追加
all_group.add_to(all_map)
mlts_group.add_to(mlts_map)
asahi_group.add_to(asahi_map)
ebis_group.add_to(ebis_map)
kirin_group.add_to(kirin_map)
hoeg_group.add_to(hoeg_map)
corona_group.add_to(corona_map)
guinness_group.add_to(guinness_map)
# premium_group.add_to(premium_map)



#追記 最安値
all_min_price = df["price"].min()
all_mean_price = int(df["price"].mean())

mlts_min_price = mlts_data["price"].min()
mlts_mean_price = int(mlts_data["price"].mean())

asahi_min_price = df["price"].min()
asahi_mean_price = int(asahi_data["price"].mean())

ebis_min_price = ebis_data["price"].min()
ebis_mean_price = int(ebis_data["price"].mean())

kirin_min_price = kirin_data["price"].min()
kirin_mean_price = int(kirin_data["price"].mean())

hoeg_min_price = hoeg_data["price"].min()
hoeg_mean_price = int(hoeg_data["price"].mean())

corona_min_price = corona_data["price"].min()
corona_mean_price = int(corona_data["price"].mean())

guinness_min_price = guinness_data["price"].min()
guinness_mean_price = int(guinness_data["price"].mean())

# premium_min_price = premium_data["price"].min()
# premium_mean_price = int(premium_data["price"].mean())


st.header("大阪梅田駅周辺でビールを提供している店舗")
st.text("左に表示されている～～～")

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

# if bland_options == "プレミアム":
#     st.subheader(":beer: プレミアム` が飲めるお店")
#     st_folium(premium_map, width=700, height=700)
#     st.sidebar.write("大阪市北区のプレミアム1杯の最安値は、", premium_min_price, "円です")
#     st.sidebar.write("大阪市北区のプレミアム1杯の平均価格は、", premium_mean_price, "円です")
