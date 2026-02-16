laura = set(input("Lista da Laura: ").split(", "))
ana = set(input("Lista da Ana: ").split(", "))

comuns = laura.intersection(ana)

exclusivos_laura = laura.difference(ana)
exclusivos_ana = ana.difference(laura)

print(f"Itens em ambas as listas: {', '.join(comuns)}")
print(f"Itens exclusivos da Laura: {', '.join(exclusivos_laura)}")
print(f"Itens exclusivos da Ana: {', '.join(exclusivos_ana)}")


