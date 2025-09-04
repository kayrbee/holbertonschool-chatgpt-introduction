### Prompt
I have been given a debugging challenge. The assignment is to use ChatGPT to help diagnose, debug and refactor the code in the exercise. This code should print the factorial of the argument. Could you review the code, and tell me where you think the errors are? 

```
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)
```

#### Diagnosis
![debugging](https://github.com/kayrbee/holbertonschool-chatgpt-introduction/blob/master/debugging/images/Task-0-diagnosed-issues.png)

#### MVP fix
![suggested minimal fix](https://github.com/kayrbee/holbertonschool-chatgpt-introduction/blob/master/debugging/images/Task-0-minimal-fix.png)

#### Recommended fix
![suggested full fix](https://github.com/kayrbee/holbertonschool-chatgpt-introduction/blob/master/debugging/images/Task-0-recommended-fix.png)
