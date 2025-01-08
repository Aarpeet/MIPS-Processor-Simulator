# MIPS Processor Simulator  

This project is a Python-based MIPS processor simulator designed to interpret and execute MIPS assembly instructions. It provides a way to convert MIPS assembly language into machine code, enabling deeper insights into instruction processing and execution in a simulated environment.  

## Features  
- Converts MIPS assembly instructions to binary machine code.  
- Supports multiple operations, including `LOAD`, `STOR`, `SUB`, `ADD`, `JUMP`, and more.  
- Includes a set of predefined opcodes for common MIPS operations.  
- Outputs the resulting machine code to a file for further analysis.  

## Assembly Instructions Supported  
The simulator supports the following instructions with their respective opcodes:  
| Instruction | Opcode       | Description                  |  
|-------------|--------------|------------------------------|  
| `LOAD`      | `00000001`   | Load from memory.            |  
| `STOR`      | `00010010`   | Store to memory.             |  
| `SUB`       | `00000110`   | Subtract.                    |  
| `ADD`       | `00000101`   | Add.                         |  
| `JUMP`      | `00001101`   | Jump to address.             |  
| `DIV`       | `00001100`   | Divide.                      |  
| `INR`       | `11111111`   | Increment.                   |  
| ...         | ...          | Other supported instructions. |  

## How It Works  
1. **Input File**: The simulator reads MIPS assembly instructions from an input file (`code1.txt`).  
2. **Instruction Parsing**: Each line is parsed to extract the opcode, memory addresses, and additional parameters.  
3. **Machine Code Generation**: The parsed instructions are converted into binary machine code.  
4. **Output File**: The generated machine code is written to an output file (`test.txt`).    
