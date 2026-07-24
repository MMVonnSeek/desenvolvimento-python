import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Max", idade=35)

    print(usuario)
    print(f"Idade: {len(usuario)}")
    del(usuario)

if __name__ == "__main__":
    main()