import sqlite3

def query_weather_data(station_name, data_category):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    categories = {
        "溫度": ["avg_temp", "max_temp", "max_temp_date", "min_temp", "min_temp_date"],
        "雨量": ["rainfall"],
        "風速與風向": ["max_10min_wind", "max_10min_wind_dir", "max_10min_wind_date", "max_instant_wind", "max_instant_wind_dir", "max_instant_wind_date"],
        "相對濕度": ["avg_humidity", "min_humidity", "min_humidity_date"],
        "氣壓": ["pressure"],
        "降水日數": ["rain_days"],
        "日照時數": ["sunshine_hours"]
    }

    if data_category not in categories:
        print("無效的數據分類，請選擇以下之一:", list(categories.keys()))
        conn.close()
        return

    columns = ", ".join(categories[data_category])
    query = f"SELECT station, {columns} FROM weather_data WHERE station = ?"
    cursor.execute(query, (station_name,))
    result = cursor.fetchone()

    if result:
        print(f"測站: {result[0]}")
        
        if data_category == "溫度":
            print(f"平均溫度: {result[1]}°C")
            print(f"最高溫度: {result[2]}°C (日期: {result[3]})")
            print(f"最低溫度: {result[4]}°C (日期: {result[5]})")
        
        elif data_category == "雨量":
            print(f"降雨量: {result[1]} 毫米")
        
        elif data_category == "風速與風向":
            print(f"最大十分鐘風速: {result[1]} 公尺/秒 (風向: {result[2]}°, 日期: {result[3]})")
            print(f"最大瞬間風速: {result[4]} 公尺/秒 (風向: {result[5]}°, 日期: {result[6]})")
        
        elif data_category == "相對濕度":
            print(f"平均相對濕度: {result[1]}%")
            print(f"最低相對濕度: {result[2]}% (日期: {result[3]})")
        
        elif data_category == "氣壓":
            print(f"氣壓: {result[1]} 百帕")
        
        elif data_category == "降水日數":
            print(f"降水日數 (>=0.1毫米): {result[1]} 天")
        
        elif data_category == "日照時數":
            print(f"日照時數: {result[1]} 小時")
    
    else:
        print(f"未找到測站 '{station_name}' 的數據")

    conn.close()

if __name__ == "__main__":
    station = input("請輸入要查詢的測站名稱: ")
    category = input("請選擇查詢分類 (溫度, 雨量, 風速與風向, 相對濕度, 氣壓, 降水日數, 日照時數): ")
    query_weather_data(station, category)
