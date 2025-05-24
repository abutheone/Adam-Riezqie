## Type of Analysis

- Static Analysis (Before Execution)
- Dynamic Analysis (Controlled Execution)

| **Aspect**             | **Static Analysis**                          | **Dynamic Analysis**                             |
| ---------------------- | -------------------------------------------- | ------------------------------------------------ |
| **Definition**         | Analyzing the malware **without running it** | Observing behavior by **executing the malware**  |
| **Environment Safety** | Very safe (no execution involved)            | Requires isolated and controlled environment     |
| **Goal**               | Understand structure, strings, imports, etc. | Observe runtime behavior, file/network activity  |
| **Information Gained** | Indicators, obfuscation, file metadata       | Real behavior, persistence methods, payload drop |
| **Risk Level**         | Low                                          | Medium–High (if not properly isolated)           |