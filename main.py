from brainfuck_interpreter import BrainFuckInterpreter


def main():
    bf = BrainFuckInterpreter(10)
    while True:
        print(' ' * (bf.pointer * 3) + '▼')
        for m in bf.memory:
            print(f"{m:02X}", end=' ')
        
        code = input("\n$ ")
        
        match code:
            case "exit":
                break
            case "reset":
                bf.reset()
        
        bf.interpret(code)
        
        print()


if __name__ == '__main__':
    main()
