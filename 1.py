import random

# 樂透開獎
numbers = random.sample(range(1, 50), 6)
print('樂透號碼: '+' '.join(map(str, sorted(numbers))))
print(f'特別號{random.randint(1, 50)}')
