import os

def sep_cat(main, sub):
    sep_main = main.split('_')
    sep_sub = sub.split('_')
    prob_cat = {"main_first":sep_main[0],
                 "main_second":sep_main[1],
                 "main_third":sep_main[2],
                 "main_final":sep_main[3],
                 "sub_first": sep_sub[0],
                 "sub_second": sep_sub[1],
                 "sub_third": sep_sub[2],
                 "sub_final": sep_sub[3]}
    return prob_cat

def similarity(prob,file_list):
    for i in range(len(prob)):
        score = dict()
        for j in range(len(prob)):
            if i==j: continue
            main_score = 0
            sub_score = 0
            if prob[i]["main_second"] == prob[j]["main_second"]:
                main_score += 0.1
                if prob[i]["main_third"] == prob[j]["main_third"]:
                    main_score += 0.25
                    if prob[i]["main_final"] == prob[j]["main_final"]:
                        main_score += 0.35
            if prob[i]["sub_second"] == prob[j]["sub_second"]:
                sub_score += 0.1
                if prob[i]["sub_third"] == prob[j]["sub_third"]:
                    sub_score += 0.25
                    if prob[i]["sub_final"] == prob[j]["sub_final"]:
                        sub_score += 0.35
            sub_score *= 3/7
            total_score = main_score+sub_score
            score[j]=int(total_score*100)
        score_sort = sorted(score.items(),
                              reverse=True,
                              key=lambda item: item[1])
        print(file_list[i] + "와/과 유사도 높은 문제 5문항")
        print_dict(prob[i])
        print()
        for key, value in score_sort[:5]:
            print("문제: "+file_list[key])
            print("유사도 점수:",value)
            print_dict(prob[key])
            print()
        print("=================================================================")

def print_dict(dict_val):
    for key, value in dict_val.items():
        print(key+": "+str(value))


datapath = "./TextData(Hangeul)"
file_list = os.listdir(datapath)

index = 0
prob_sep = list()
for file in file_list:
    with open(datapath+"/"+file, "r", encoding='utf-8') as f:
        main, sub = tuple(f.readlines())
        prob_sep.append(sep_cat(main.strip(),sub.strip()))
        index += 1

similarity(prob_sep,file_list)


