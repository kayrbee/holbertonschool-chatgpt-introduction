### Prompt
This time, the code I was given prints all argv items including the file name. It should skip the file name. Could you review the code, and tell me where you think the errors are?

```
#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])    
```

#### Diagnosis

#### Suggested fixes