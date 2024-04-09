# 定義 classify_user 函數，接受 name, gender, age 三個參數
def classify_user(name, gender, age):
    # 判斷性別是否為 '男'，如果是，返回以先生稱呼的問候語句
    if gender == '男':
        return f"{name} 先生您好，"
    # 判斷性別是否為 '女'，如果是，返回以女士稱呼的問候語句
    elif gender == '女':
        return f"{name} 女士您好，"
    # 如果性別未知，返回“未知性别。”
    else:
        return "未知性别。"

# 定義 choose_herb 函數，接受 symptom 和 choice 兩個參數
def choose_herb(symptom, choice):
    # 定義草藥字典，對應症狀與草藥名稱
    herbs = {
        "睏不好": "魚腥草",
        "半暝還在嗨": ["白鶴靈芝(不苦)", "蒲公英(苦)"],
        "早上哈啾": "金銀花",
        "癢癢": "忍冬",
        "胃生氣": "積雪草",
        "厭世生理期": ["鴨舌黃", "益母草"]
    }

    # 定義劑量字典，對應程度與劑量
    dosage = {
        "1": 0.5,
        "2": 1.0,
        "3": 1.5,
        "4": 2.0,
        "5": 2.5
    }

    # 判斷症狀是否在草藥字典中
    if symptom in herbs:
        # 如果是列表，則用 "or" 連接列表內的草藥名稱
        herb = herbs[symptom]
        if isinstance(herb, list):
            herb = "or".join(herb)
        # 判斷選擇的劑量是否在劑量字典中，如果是，返回對應的草藥名稱和劑量
        if choice in dosage:
            return herb, dosage[choice]
        # 如果劑量不在劑量字典中，返回 "Invalid choice!"
        else:
            return "Invalid choice!"
    # 如果症狀不在草藥字典中，返回 "Invalid symptom!"
    else:
        return "Invalid symptom!"

# 定義 main 函數
def main():
    # 請求用戶輸入姓名
    name = input("請輸入您的姓名: ")
    # 請求用戶輸入性別
    gender = input("請輸入您的性別(男/女): ")
    # 請求用戶輸入年齡
    age = int(input("請輸入您的年齡: "))
    # 請求用戶輸入密碼
    password = input("請輸入您的密碼: ")

    # 調用 classify_user 函數，根據輸入的性別生成問候語句
    result = classify_user(name, gender, age)
    # 印問候語句
    print(result)

    # 定義症狀列表
    symptoms = [
        "睏不好",
        "半暝還在嗨",
        "早上哈啾",
        "癢癢",
        "胃生氣",
        "厭世生理期"
    ]

    # 定義用於存儲用戶選擇的草藥和劑量的列表
    chosen_herbs = []
    # 定義總劑量變量，用於存儲所有草藥劑量的總和
    total_dosage = 0

    # 印出選擇項目中的提示訊息
    print("\n選擇項目中...")
    # 遍歷症狀列表
    # 選擇最高的五個症狀，並記錄用戶輸入的程度
    symptom_choices = {symptom: int(input(f"{symptom} 的程度(1-5): ")) for symptom in symptoms}
    # 將症狀按程度進行排序，降序排列
    sorted_symptoms = sorted(symptoms, key=lambda x: symptom_choices[x], reverse=True)
    
    # 計算總權重和
    weight_sum = sum(symptom_choices.values())
    # 選擇最高的五個症狀
    for symptom in sorted_symptoms[:5]:
        # 獲取用戶選擇的程度
        choice = str(symptom_choices[symptom])
        # 調用 choose_herb 函數，根據症狀和程度選擇草藥和劑量
        herb, dosage = choose_herb(symptom, choice)
        # 計算調整後的劑量，以保證總和為5克
        weight = symptom_choices[symptom] / weight_sum
        adjusted_dosage = 5 * weight
        # 將選擇的草藥和劑量添加到列表中
        chosen_herbs.append((herb, adjusted_dosage))
        # 計算總劑量
        total_dosage += adjusted_dosage

    # 如果總劑量大於5克，對每個草藥的劑量進行縮放，以確保總劑量為5克
    if total_dosage > 5:
        scale_factor = 5 / total_dosage
        chosen_herbs = [(herb, dosage * scale_factor) for herb, dosage in chosen_herbs]

    # 印出用戶選擇的草藥及其用量
    print("\n您選擇的草藥及其用量為:")
    for herb, dosage in chosen_herbs:
        print(f"{herb}: {dosage:.2f}g")

# 如果是直接運行此文件，則執行 main 函數
if __name__ == "__main__":
    main()
