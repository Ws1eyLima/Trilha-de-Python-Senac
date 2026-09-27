print("Tabela Verdade AND")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

print("\nTabela Verdade OR")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

print("\nTabela Verdade NOT")
print(f"not True = {not True}")
print(f"not False = {not False}")

is_active = True
is_admin = True

if (is_active and is_admin):
    print("Usuário ativo")
else:
    print("Usuário inativo")