from faker import Faker
fake = Faker()

nome = fake.name()
fastname = fake.first_name_female()
usuario = fake.user_name()
senha = fake.password()
mes = fake.month()
print(f'Nome:{nome}')
print(f'Sobre nome:{fastname}')
print(f'Usuario:{usuario}')
print(f'Senha:{senha}')
print(f'mes:{mes}')



