def classify_user(name, gender, age):
    
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

    result = classify_user(name, gender, age)
    print(result)

if __name__ == "__main__":
    main()
def choose_herb(symptom, choice):
    herbs = {
        "睏不好": "魚腥草",
        "半暝還在嗨": ["白鶴靈芝(不苦)", "蒲公英(苦)"],
        "早上哈啾": "金銀花",
        "癢癢": "忍冬",
        "胃生氣": "積雪草",
        "厭世生理期": ["鴨舌黃", "益母草"]
    }

    dosage = {
        "1": "0.5g",
        "2": "1.0g",
        "3": "1.5g",
        "4": "2.0g",
        "5": "2.5g"
    }

    if symptom in herbs:
        herb = herbs[symptom]
        if isinstance(herb, list):
            herb = "or".join(herb)
        if choice in dosage:
            return f"{herb} {dosage[choice]}"
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
    for symptom in symptoms:
        choice = input(f"{symptom} 的程度(1-5): ")
        result.append(choose_herb(symptom, choice))

    print("\n結果:")
    for item in result:
        print(item)

if __name__ == "__main__":
    main()