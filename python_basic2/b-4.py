def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
        {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
        {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

        {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
        {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
        {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

        {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
        {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
    ]
    # 平均気温を求める関数

    # average_temperature(temperature, number_of_data):

    # temperature / number_of_data

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    temperature = 0

    for temp in weather_information:
        temperature += temp["temperature"]
        average_temperature = temperature / len(weather_information)

    print(f"全国の平均気温は、{average_temperature}度です。")

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    # リスト形式の出力ではないってこと？→join()で解決！

    osaka_station = []

    for station in weather_information[3:6]:
        osaka_station.append(station["station"])
    display_osaka_station = ",".join(osaka_station)
    print(display_osaka_station)

    # """
    # リスト形式でprintするタイプ
    # stations = []
    # stations.append(station["station"])

    # # print(stations)
    # """
    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    temperature_of_fukuoka = 0

    for ftemp in weather_information[6:8]:
        temperature_of_fukuoka += ftemp["temperature"]
        faverage_temperature = temperature_of_fukuoka / len(weather_information[6:8])

    print(f"福岡の平均気温は、{faverage_temperature}度です。")


if __name__ == '__main__':
    main()

# """
# Q2 リストの値を取り出し、,を間につける方法を検討
# Q3 平均気温を求めていることは同じなので、関数内で平均気温を求める関数を作成
