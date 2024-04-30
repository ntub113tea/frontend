def classify_user(name, gender, age,password):
    
    if gender == '男':
        return f"{name} 先生您好，"
    elif gender == '女':
        return f"{name} 女士您好，"
    else:
        return "未知性别。"

def main():
    name = input("請輸入您的姓名: ")
    gender = input("請輸入您的性別(男/女): ")
    age = int(input("請輸入您的年齡: "))
    password = int(input("請輸入您的密碼: "))

    result = classify_user(name, gender, age,password)
    print(result)

if __name__ == "__main__":
    main()

def choose_herb(symptom, choice, total_weight):
    herbs = {
        "睏不好": "魚腥草",
        "半暝還在嗨": ["白鶴靈芝(不苦)", "蒲公英(苦)"],
        "早上哈啾": "金銀花",
        "癢癢": "忍冬",
        "胃生氣": "積雪草",
        "厭世生理期": ["鴨舌黃", "益母草"]
    }

    dosage = {
        "1": 0.5,
        "2": 1.0,
        "3": 1.5,
        "4": 2.0,
        "5": 2.5
    }

    if symptom in herbs:
        herb = herbs[symptom]
        if isinstance(herb, list):
            herb = "or".join(herb)
        if choice in dosage:
            # 計算每個症狀所需的藥材克數
            required_dosage = dosage[choice]
            # 計算調整比例，以確保所有藥材的總和為 total_weight
            adjustment_factor = total_weight / sum(dosage.values())
            # 調整每個症狀所需的藥材克數
            adjusted_dosage = required_dosage * adjustment_factor
            # 限制小數位數最多為兩位
            adjusted_dosage = round(adjusted_dosage, 2)
            return f"{herb} {adjusted_dosage:.2f}g"
        else:
            return "Invalid choice!"
    else:
        return "Invalid symptom!"

def main():
    symptoms = [
        "睏不好",
        "半暝還在嗨",
        "早上哈啾",
        "癢癢",
        "胃生氣",
        "厭世生理期"
    ]

    result = []
    print("請依序回答以下症狀的程度，1 表示最輕微，5 表示最嚴重：")
    total_weight = 5  # 定義藥材克數的總和
    for symptom in symptoms:
        choice = input(f"{symptom} 的程度(1-5): ")
        result.append(choose_herb(symptom, choice, total_weight))

    # 如果六種藥材的克數加總超過5，則進行額外調整
    total_sum = sum(float(item.split()[1][:-1]) for item in result)
    if total_sum > 5:
        adjustment_factor = 5 / total_sum
        for i in range(len(result)):
            dosage = float(result[i].split()[1][:-1]) * adjustment_factor
            result[i] = result[i].split()[0] + f" {dosage:.2f}g"

    print("\n結果:")
    for item in result:
        print(item)

if __name__ == "__main__":
    main()

