# classe
class Pessoa:
    # atributos
    nome = "Max Muller"
    idade = 35
    telefone = "(61) 99999-9999"
    cpf = "123.456.789-12"
    email = "max@gmail.com"

    # método
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos, meu telefone é {self.telefone}, meu CPF é {self.cpf} e meu e-mail é {self.email}.")
    
# programa principal
if __name__ == "__main__":
    # instanciar classe
    usuario = Pessoa()

    # objeto se apresenta
    usuario.apresentar()