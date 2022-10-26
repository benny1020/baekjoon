"""
+, - *
만으로 이루어진 연산 수식
우선순위 새로 정의
동일한 순위 불가
음수라면 절댓값 반환

"""
import itertools

def cal(ex, num1, num2):
    if ex == '+':
        return num1 + num2
    elif ex == '-':
        return num1 - num2
    else:
        return num1 * num2

def solution(expression):
    operators = ['-', '+', '*']
    expression_list = []
    number = ""
    for i in range(len(expression)):
        if expression[i] in operators:
            expression_list.append(int(number))
            expression_list.append(expression[i])
            number = ""
        else:
            number += expression[i]
    expression_list.append(int(number))
    

    # --------
    operator_list = list(itertools.permutations(operators,3))
    maxx = 0
    for op in operator_list:
        flag = False
        tmp_ex = []

        tmp_expression_list = expression_list
        for o in op:
            tmp_ex = []
            for i in range(len(tmp_expression_list)):
                if flag:
                    flag = False
                    continue
                if tmp_expression_list[i] == o:
                    num = cal(tmp_expression_list[i], tmp_ex.pop(),tmp_expression_list[i+1])
                    tmp_ex.append(num)

                    flag = True
                else:
                    tmp_ex.append(tmp_expression_list[i])
            tmp_expression_list = tmp_ex
        maxx = max(maxx,abs(tmp_expression_list[0]))

                    
    return maxx

    