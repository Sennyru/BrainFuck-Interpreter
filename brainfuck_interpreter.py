class BrainFuckInterpreter:
    def __init__(self, memory_size: int = 32768):
        self.reset(memory_size)
    
    def interpret(self, code: str):
        c = 0
        while c < len(code):
            match code[c]:
                case '>':
                    if self._p < self.memory_size - 1:
                        self._p += 1
                
                case '<':
                    if self._p > 0:
                        self._p -= 1
                
                case '+':
                    self._mem[self._p] = (self._mem[self._p] + 1) % 256
                
                case '-':
                    self._mem[self._p] = (self._mem[self._p] - 1) % 256
                
                case '.':
                    print(chr(self._mem[self._p]), end='')
                
                case ',':
                    self._mem[self._p] = ord(input())
                
                case '[':
                    if self._mem[self._p] == 0:
                        while code[c] != ']':
                            c += 1
                
                case ']':
                    if self._mem[self._p] != 0:
                        while code[c] != '[':
                            c -= 1
                        continue
            
            c += 1
    
    def reset(self, memory_size):
        self.memory_size = memory_size
        self._mem = bytearray(self.memory_size)
        self._p = 0
    
    @property
    def pointer(self) -> int:
        return self._p
    
    @property
    def memory(self) -> bytes:
        return self._mem
    
