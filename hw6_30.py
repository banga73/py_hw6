def progr(a1, r, n):
    progr_pr = []
    progr_pr.append(a1)
    for i in range(2, n + 1):
        progr_pr.append(a1 + (i - 1) * r)
    return(progr_pr)

a1_pr = int(input ("Введите первый член прогрессии: "))
r_pr = int(input ("Введите разность прогрессии: "))
N_pr = int(input ("Введите количество членов прогрессии: "))
print(progr(a1_pr, r_pr, N_pr))