# simplified-c-compiler

## Python

### unix/mac
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
```

### windows
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pip install --upgrade pip
```

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