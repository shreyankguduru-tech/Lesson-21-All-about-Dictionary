StudentData = {     
    "id1": {"name":"Sara","class":"V","Subject_intergration": "Maths, English, Science"},
    "id2": {"name":"David","class":"V","Subject_intergration":"Maths, English, Science"},
    "id3": {"name":"Sara","class":"V","Subject_intergration": "Maths, English, Science"},
    "id4": {"name":"Surya","class":"V","Subject_intergration":"Maths, English, Science"},
    }

result = {}

seen_keys = []

for studentId, details in StudentData.items():
    unique_key = (details["name"],details["class"],details["Subject_intergration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[studentId] = details


for K,V in result.items():
    print(K,":",V)
