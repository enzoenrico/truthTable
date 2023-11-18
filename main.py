# ---------------------------------------------------------------------------------------------------------------
# |                                    Link para o vídeo:                                                       |
# |                                        https://youtu.be/hUEsUNhBSUk                                         |
# |                                                                                                             |
# |                                    Link para o repositório GitHub:                                          |
# |                                        https://github.com/enzoenrico/truthTable                             |
# ---------------------------------------------------------------------------------------------------------------



import ttg
import os

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

        # self.getVariables()
        self.getOperations()
        self.createTable()
        self.countStats()

    # def getVariables(self):
    #     active = True
    #     while (active):
    #         tempVar = input(
    #             "[✏] Escreva uma variavél para ser usada na tabela veradade \nAperte Enter para inserir uma nova variavél, 'Q' para seguir para a próxima etapa\n")

    #         if (tempVar.lower() != "q"):
    #             if (tempVar.lower() in self.variables):
    #                 print("[❌] Variavél já existente!")
    #             else:
    #                 self.variables.append(tempVar)
    #         else:
    #             active = False
    #             return

    # def getOperations(self) -> []:
    #     active = True
    #     while (active):
    #         # Variaveis sorted by alfabeto
    #         print('Suas variavéis:', sorted(Interpreter.variables))
    #         if (len(self.operations) > 0):
    #             print(f"Suas operações: {self.operations}")
    #         newCommand = input(
    #             "[✏] Escreva uma fórmula para interpretação\n Aperte Enter para inserir uma nova fórmula, 'Q' para seguir para a próxima etapa\n")
    #         if (newCommand.lower() != "q"):
    #             if (newCommand.lower() in self.operations):
    #                 print("[❌] Comando já existente!")
    #             else:
    #                 self.operations.append(newCommand)

    #         else:
    #             active = False
    #             return

    def getOperations(self):
        active = True
        tmpIdx = 0
        ops: [[str]] = []
        while active:
            # pegar operações do usuário
            tmp = input("[+]Escreva as operações. Pressione Enter para uma nova operação, e Q para seguir para o próximo passo:\n")
            
            if tmp == "q":
                # ops.pop()
                active = False
                break
            
            ops.append(tmp.split())
            print(ops)
            
        
        for opIdx, op in enumerate(ops):
            print(f"op: {op} - {opIdx}")
            for valIdx, val in enumerate(op):
                print(f"val : {val} - {valIdx}")

                if (val.isalpha() or val.isnumeric()) and val != " " and val not in safeCommands and val not in self.variables:
                    self.variables.append(val)    
                # if val in safeCommands:
                #     self.operations.append(val)
            self.operations.append(" ".join(op))
            print(f"SelfOperations: {self.operations}")
            
            


    
    def countVars(self, ops:[str], varsList: [str]) -> [str, int]:
        # Retorna apenas uma lista com o elemento mais comum e quantas vezes ele aparece
        hashmap = {}
        for j in range(len(ops)):
            for i in ops[j].split():
                if(i in hashmap and i in varsList):
                    hashmap[i] += 1
                if(i in varsList and i not in hashmap):
                    hashmap[i] = 1
        return [max(hashmap, key=hashmap.get), max(hashmap.values())]

    
    def getOpCount(self) -> dict:
        # Retorna o hashmap completo com a contagem das operações
        hashmap = {}
        ops = self.operations
        for j in range(len(ops)):
            for i in ops[j].split():
                if(i in hashmap and i in safeCommands):
                    hashmap[i] += 1
                if(i not in hashmap and i in safeCommands):
                    hashmap[i] = 1
        return hashmap

    def createTable(self):
        try:
            table = ttg.Truths(self.variables, self.operations)
            print("[✅] Sua tabela verdade está pronta!")
            print(table)
        except:
            print("[!]Algo deu errado, por favor tente novamente")
            os.abort()
            

    def countStats(self):
        # Show n of variables and number of results
        print(f"[👾] Você inseriu {len(self.variables)} variavéis!")
        print(self.variables)
        # TODO add counter de variaveis
        print(f"[👀] Sua variavél favorita foi: {self.countVars(self.operations, self.variables)[0]}! Ela apareceu {self.countVars(self.operations, self.variables)[1]} vezes em todas as operações!")

        # TODO Inserir identificador de fórmulas da lista 'operations'
        print(
            f"[🐱‍💻] Você realizou {len(self.operations)} operações! Elas foram: ")
        for i in self.operations:
            print(f"\t🎉 {i}")
        
        
        print("[😎] Em todas as operações, você realizou:")
        opList = self.getOpCount()
        for i in opList:
            print(f"\t[👁️] '{i}' apareceu {opList[i]} vezes!")

        cont = input(
            "[🍙] Deseja continuar o programa? Pressione Enter para reiniciar e 'Q' para fechar o programa\n")
        if (cont.lower() == 'q'):
            return
        else:
            Interpreter.processRunner(self)
        

if __name__ == "__main__":
    Interpreter()
    # print(countVars(['a and a', 'a or b', 'a => a'], ['a', 'b']))



