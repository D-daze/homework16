def generate_password(n):
    if n < 3 or n > 20:
        raise ValueError("Число n должно быть в диапазоне от 3 до 20")

    result = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if pair_sum % n == 0:
                result.append(f"{i}{j}")
    return ''.join(result)
for num in range(3, 21):
    print(f"{num} - {generate_password(num)}")
