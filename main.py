import ttg
import re

# Variavel de keywords / comandos safe-to-use para o ttg
safeCommands: [str] = ["not", "-", "~", "or", "||", "nor",
                       "xor", "!=", "and", "&&", "nand", "=>", "implies", "="]


class Interpreter:
    variables: [str] = []
    operations: [str] = []

    def __init__(self):
        self.processRunner()

    def processRunner(self):
        self.variables = []
        self.operations = []

        self.getVariables()
        self.getOperations()
        self.createTable()
        self.countStats()

    def getVariables(self):
        active = True
        while (active):
            tempVar = input(
                "[✏] Escreva uma variavél para ser usada na tabela veradade \nAperte Enter para inserir uma nova variavél, 'Q' para seguir para a próxima etapa\n")

            if (tempVar.lower() != "q"):
                if (tempVar.lower() in self.variables):
                    print("[❌] Variavél já existente!")
                else:
                    self.variables.append(tempVar)
            else:
                active = False
                return

    def getOperations(self) -> []:
        active = True
        while (active):
            # Variaveis sorted by alfabeto
            print('Suas variavéis:', sorted(Interpreter.variables))
            if (len(self.operations) > 0):
                print(f"Suas operações: {self.operations}")
            newCommand = input(
                "[✏] Escreva uma fórmula para interpretação\n Aperte Enter para inserir uma nova fórmula, 'Q' para seguir para a próxima etapa\n")
            if (newCommand.lower() != "q"):
                if (newCommand.lower() in self.operations):
                    print("[❌] Comando já existente!")
                else:
                    self.operations.append(newCommand)

            else:
                active = False
                return

    def countVars(self, var: str):
        # TODO Regex ou loop para achar quantas vezes a mesma variavel aparece em todas as operações
        #retornar qual variavel é e quantas vezes aparece
        return
    
    def countOps(self, op: str):
        # TODO Regex ou loop para achar quantas vezes a mesma operação aparece 
        #retornar qual operação é e quantas vezes aparece
        #talvez retornar as operações com seus nomes, não sei sei la
        return

    def createTable(self):
        table = ttg.Truths(self.variables, self.operations)
        print("[✅] Sua tabela verdade está pronta!")
        print(table)

    def countStats(self):
        # Show n of variables and number of results
        print(f"[👾] Você inseriu {len(self.variables)} variavéis!")
        # TODO add counter de variaveis
        print(f"[👀] Sua variavél favorita foi: self.countVars() ! Ela apareceu self.countVars() vezes em todas as operações!")

        # TODO Inserir identificador de fórmulas da lista 'operations'
        print(
            f"[🐱‍💻] Você realizou {len(self.operations)} operações! Elas foram: ")

        for i in self.operations:
            print(f"🎉 {i}")

        cont = input(
            "[🍙] Deseja continuar o programa? Pressione Enter para reiniciar e 'Q' para fechar o programa\n")
        if (cont.lower() == 'q'):
            return
        else:
            Interpreter.processRunner(self)


if __name__ == "__main__":
    Interpreter()
