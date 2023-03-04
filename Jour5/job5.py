def la_suite_de_fibonacci(n):
    if n <= 1:
        return n
    else:
        return la_suite_de_fibonacci(n-1) + la_suite_de_fibonacci(n-2)

n = int(input("Entrez la taille de la suite de Fibonacci:"))
print("le dernier nombre est : ",la_suite_de_fibonacci(n))
print("-----------------")

#Pour vérifier que le code fonctionne
for i in range(n):
    print(la_suite_de_fibonacci(i+1))