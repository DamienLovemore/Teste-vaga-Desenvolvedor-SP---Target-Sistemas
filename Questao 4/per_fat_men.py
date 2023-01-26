def calc_perc_fat(nome_estado: str,fat_est: float, fat_total: float):
    perc_rep = fat_est * 100 / fat_total
    print(f"O estado {nome_estado} faturou a quantia de {perc_rep:.2f}% do faturamento total desse mes.")

fat_sp = 67836.43
fat_rj = 36678.66
fat_mj = 29229.88
fat_es = 27165.48
fat_out = 19849.53
fat_tot = fat_sp + fat_rj + fat_mj + fat_es + fat_out

calc_perc_fat("SP", fat_sp, fat_tot)
calc_perc_fat("RJ", fat_rj, fat_tot)
calc_perc_fat("MJ", fat_mj, fat_tot)
calc_perc_fat("ES", fat_es, fat_tot)
calc_perc_fat("OUTROS", fat_out, fat_tot)
