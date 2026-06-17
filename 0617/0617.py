orgstr = '''
國立中興大學（簡稱興大、NCHU）是一所校本部位於台灣臺中市南區的國立研究型綜合大學，
起源自臺灣總督府創辦的農林專門學校，
臺北帝國大學設立後併入為附屬農林專門部，而後於1943年獨立設校並遷址台中。
中興大學以農業科學、農業經濟學、獸醫學、生命科學、轉譯醫學、材料科學、生醫工程、生物科技、綠色科技等研究領域見長，
校友共有7位中央研究院院士，皆為生命科學組。[7]興大目前共有12個學院與興大附農、興大附中兩所附屬中學。
近年與臺中榮民總醫院、彰化師範大學、中國醫藥大學等機構合作，2022年學士後醫學系設立，為台灣中部第一所國立大學醫學系。
興大醫學院並未設置教學醫院而採用美國哈佛醫學院模式與鄰近醫院合作培養醫學人才。[8]興大也與臺中市政府合作，簽訂合作意向書，共同推動數位文化、智慧城市帶動區域發展[9]。
'''
# st = set(orgstr)
# dt = dict()
# for c in st:
#     print(c)
#     dt[c] = orgstr.count(c)
# print(dt)


# 利用user_list名單，搭配隨機功能，
# 為每一位user產生一個介於1~100的成績，
# 再從中找出最高分的user
# import random
# user_list = ["Aaric", "Abbot", "Ace", "Ackerley", "Adam", "Adney", 
#             "Bab", "Bamboo", "Ben", "Bunny", "Betty", "Baha", 
#             "Cindy", "Candy", "Cathy", "Cakra", "Carin", "Caroline",
#             "Deny", "Dacy", "Danna", "Debbi", "Devon", "Diza","Dob"]
# result = {}
# for item in user_list:
#     random_number = random.randint(1, 100)
#     result[item] = random_number

# winner_result = {}
# max_score = max(result.values())
# for key, value in result.items():
#     if value == max_score:
#         winner_result[key] = value

# print(winner_result)

products = {
    "apple":{
        "price":30,
        "stock":50
    },
    "banana":{
        "price":20,
        "stock":80
    },
    "orange":{
        "price":10,
        "stock":100
    },
    "grape":{
        "price":30,
        "stock":60
    },
    "mango":{
        "price": 40,
        "stock":150
    },
    "lemon":{
        "price":50,
        "stock":80
    }
}