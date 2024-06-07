# simplified-c-compiler

## requirements
* python 3.7

## usage
```bash
python src/syntax_analyzer.py <token_input_file>
```

Input: 
* A sequence of tokens (terminals) written in the input file (see the [example inputs](#example-input) section for more details)

Output
* accept: parse tree for the input sequence
* reject: error report


## example input

### [basic variable declaration](input/basic_variable_declaration.txt) 
```c
int x;
```

### [variable assignment](input/variable_assignment.txt)
equivalent code;
```c
int x = 10;
```

### [function declaration no args](input/function_declaration_no_args.txt)
```c
int main() {
    return 0;
}
```

### [function declaration args and statements](input/function_declaration_statement.txt)
```c
int func(int a, int b, int c) {
    int x;
    return 0;
}
```

### [if statement](input/if_statement.txt)
```c
int main() {
    if (true == true) {
        x = 10;
    }
    return x;
}
```

### [if else statement](input/if_else_statement.txt)
```c
int main() {
    if (true == true) {
        x = 10;
    } else {
        x = 20;
    }
    return x;
}
```

### [while loop assignment](input/while_loop_assignment.txt)
```c
int main() {
    while (true) {
        x = 10;    
    }
    return x;
}
```