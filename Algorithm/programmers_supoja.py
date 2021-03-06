import numpy as np

def solution(answers):
    answer = 0
    supoja = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    correct = []
        
    for spj in supoja:    
        quot = len(answers) // len(spj) # 정수배 
        # print(len(answers), len(spj), "=>", quot)

        # answers 길이 < spj 길이  
        if quot == 0:
            extnd_spj = spj[:len(answers)]    
        # answers 길이 >= spj 길이  
        else:
            extnd_spj = spj + (quot-1)*spj # 배수만큼 연장
            remain = len(answers) % len(extnd_spj)
            if remain != 0:
                extnd_spj = extnd_spj + spj[:remain] # 나머지만큼 연장
        # print("spj: ", extnd_spj, len(extnd_spj))
        # print()
                    
        # 각 원소끼리 정답 원소와 비교       
        ans_arr = np.array(answers)  
        ans_arr = ans_arr[np.array(extnd_spj) == ans_arr]
        correct.append(len(ans_arr))
        # print(correct)

    correct_arr = np.array(correct)
    correct_arr = np.where((correct_arr == max(correct_arr)))[0] + np.array(1) # tuple
    # print(correct_arr)
    
    answer = correct_arr.tolist()
    
    return answer

if __name__ == '__main__':
    ans = [[1,2,3,4,5], [1,3,2,4,2], [1,1,1,1], [5,4,4,2,1], [1,2,3,4,5,6,7], [1,2,3], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    # [1], [1,2,3], [3], [1,2,3], [1], [1], [1,3]

    for a in ans:
        print('answer: ', solution(a)) 