def calc_seq_fib(num_proc: int) -> bool:
    num_enc = False
    num_seq = []

    num_ant = 0
    num_atu = 1
    num_seq.append(num_ant)
    print(num_ant)
    num_seq.append(num_atu)
    print(num_atu)

    for cont in range(0, 100):
        num_nov = num_ant + num_atu
        num_seq.append(num_nov)
        print(num_nov)

        if num_nov == num_proc:
            num_enc = True
            break

        num_ant = num_atu
        num_atu = num_nov
    print("")

    return num_enc

user_input = input("Digite o numero a ser indentificado na sequencia de Fibonacci\n")
print()
num_proc = int(user_input)

ret = calc_seq_fib(num_proc)
print("Numero pertence a Fibonacci") if ret else print("Numero nao pertence a Fibonacci")
