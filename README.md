# Evaluating-and-Improving-Large-Language-Models-for-Competitive-Program-Generation


If you want to generate programs in batches using code, 


You can upload txt documents for batch generation of the program.

The requirements in the txt document: The title description of each program needs to be separated by ###_###



The final result will also generate a result.txt file

This file will contain three parts: the title, the program and the explanation

The generated program will be placed in |||... In |||, explanations and clarifications will be separated by ###

Each question is separated by ###_###




Prompt Templates for Multi-turn Dialogue-based Repair
Strategy I: Full Algorithm Regeneration
Objective: Correct fundamental misunderstandings of the problem or inappropriate algorithm choices.
Mechanism: Prompt the model to reanalyze the problem statement, select a correct algorithmic paradigm, and regenerate a completely new solution from scratch.
Prompt Example: "You selected an inappropriate algorithm. Re-read the statement, pick a suitable paradigm, and write a brand-new solution."

Strategy II: Logic Completion
Objective: Complete missing branches, edge case handling, or unimplemented transitions in otherwise sound algorithm structures.
Mechanism: Guide the model to detect incomplete logic (i.e., boundary cases, missing recursive base cases), and add the necessary conditional branches or logic structures.
Prompt Example: "Your DP misses a base state; list all dp[i] meanings and add the absent transitions."

Strategy III: Prompt-Level Clarification
Objective: Improve model planning and problem comprehension before any code is generated.
Mechanism: Require the model to explain the algorithm, define state variables (especially for DP), and list core steps before generating code.
Prompt Example: "Before writing code, please explain the main logic, define all key states and transitions, and outline your algorithm plan in bullet points."

Strategy IV: I/O Format Fix
Objective: Ensure the generated program strictly conforms to the input/output format specified by the problem.
Mechanism: Prompt the model to revise I/O handling logic, fix spacing, ordering, and precision, and remove extraneous outputs.
Prompt Example: "Your current output does not match the required format. Failed test is as follows: [failed test case] Please revise the input/output logic to follow the problem description exactly."

Strategy V: Syntax-Level Repair
Objective: Fix low-level code defects such as syntax errors or invalid parameters.
Mechanism: Use compiler or interpreter messages to guide line-level corrections to function calls, syntax, and structural statements.
Prompt Example: "The code cannot compile due to [algorithm-specific error message]. Please identify and correct the corresponding syntax issue."

Strategy VI: Calculation Precision / Memory Safety Enhancement
Objective: Prevent failure to pass the test cases or runtime crashes by ensuring safe memory access, selection of high-precision data types, and proper variable initialization.
Mechanism: Add bounds checks, switch to wider types (i.e., long long instead of int), and optimize memory usage.
Prompt Example: "Your code crashes due to calculation precision/memory issues. Below is the failed test case: [test case]."

Strategy VII: Termination Assurance
Objective: Ensure that loops and recursive calls terminate properly in all cases.
Mechanism: Analyze loop conditions and base cases, fix progress variables, and add safeguards against infinite execution.
Prompt Example: "Your program runs indefinitely or crashes due to infinite recursion. Please ensure all loop and recursive conditions lead to termination."


Table 1. Mapping between General Error Categories and Automatic Repair Strategies (GE)
|---------------|-------------------------------------------------------------------------|--------------------------------------------------------------------|
| Error Type ID | Error Type                                                              | Recommended Repair Strategies                                      |
|---------------|-------------------------------------------------------------------------|--------------------------------------------------------------------|
| GE1.1         | Incorrect Algorithm                                                     | Strategy 1 (Full Algorithm Regeneration)                           |
| GE1.2         | Misunderstanding Problem Requirements                                   | Strategy 1 + Strategy 3 (Prompt-Level Clarification)               |
| GE1.3         | Overly Complex or Inefficient Design                                    | Strategy 1 (Full Algorithm Regeneration)                           |
| GE2.1         | Compilation Errors                                                      | Strategy 5 (Syntax Repair)                                         |
| GE2.2         | Language-specific Syntax Misuse                                         | Strategy 5 (Syntax Repair)                                         |
| GE3.1         | Incorrect Input Format Handling                                         | Strategy 4 (I/O Format Fix)                                        |
| GE3.2         | Output Format Mismatches                                                | Strategy 4 (I/O Format Fix)                                        |
| GE4.1         | Incorrect Handling of Edge Cases or Input Boundaries                    | Strategy 2 (Logic Completion)                                      |
| GE4.2         | Off-by-one Errors in Loops or Indexing                                  | Strategy 2 (Logic Completion)                                      |
| GE5.1         | Faulty Condition Expressions in Control Statements                      | Strategy 2 (Logic Completion)                                      |
| GE5.2         | Incorrect Logical Operators or Precedence                               | Strategy 2 (Logic Completion)                                      |
| GE6.1         | Overflow or Precision Loss Due to Improper Data Type Selection          | Strategy 6 (Calculation Precision / Memory Safety Enhancement)     |
| GE6.2         | Implicit Type Conversions Causing Unexpected Behavior                   | Strategy 6 (Calculation Precision / Memory Safety Enhancement)     |
|---------------|-------------------------------------------------------------------------|--------------------------------------------------------------------|





Table 2. Mapping between Algorithm-Specific Error Categories and Automatic Repair Strategies (AE)
|---------------|-------------------------------------------------------------------------|---------------------------------------------------------------------|
| Error Type ID | Error Type                                                              | Recommended Repair Strategies                                       |
|---------------|-------------------------------------------------------------------------|---------------------------------------------------------------------|
| AE1.1         | Misuse or Derivation Error of Mathematical Formulas or Conclusions      | Strategy 3 + Strategy 6 (Mathematical Reasoning Enhancement)        |
| AE1.2         | Special Mathematical Structures Handle Errors                           | Strategy 3 + Strategy 6 (Mathematical Reasoning Enhancement)        |
| AE2.1         | Incorrect Local Decision-making Leading to Suboptimal Solutions         | Strategy 2 + Strategy 4 (Greedy Strategy Validation)                |
| AE2.2         | Lack of Proof/Validation for Greedy Choice Correctness                  | Strategy 3 + Strategy 4 (Greedy Strategy Validation)                |
| AE3.1         | Incorrect State Definition                                              | Strategy 2 (Logic Completion)                                       |
| AE3.2         | Errors in State Transition Logic                                        | Strategy 2 (Logic Completion)                                       |
| AE3.3         | Improper Initialization of Base States                                  | Strategy 2 (Logic Completion)                                       |
| AE4.1         | Incorrect Base Cases                                                    | Strategy 2 (Logic Completion)                                       |
| AE4.2         | Faulty Merging of Subproblems                                           | Strategy 2 (Logic Completion)                                       |
| AE4.3         | Missing Recursive Calls or Incorrect Recursion Depth                    | Strategy 2 + Strategy 7 (Termination Assurance)                     |
| AE5.1         | Incorrect Base Cases                                                    | Strategy 2 (Logic Completion)                                       |
| AE5.2         | Faulty Merging of Subproblems                                           | Strategy 2 (Logic Completion)                                       |
| AE5.3         | Missing Recursive Calls or Incorrect Recursion Depth                    | Strategy 2 + Strategy 7 (Termination Assurance)                     |
| AE5.4         | Overlapping Subproblems Not Identified Properly                         | Strategy 2 (Logic Completion)                                       |
| AE6.1         | Incomplete State Space Traversal                                        | Strategy 2 (Logic Completion)                                       |
| AE6.2         | Over-pruning or Missing Transitions                                     | Strategy 2 (Logic Completion)                                       |
| AE6.3         | Incorrect Use of BFS, DFS, or Heuristic Pruning                         | Strategy 2 (Logic Completion)                                       |
| AE6.4         | Infinite Loops or Cycles in Graph Traversal                             | Strategy 7 (Termination Assurance)                                  |
|---------------|-------------------------------------------------------------------------|---------------------------------------------------------------------|



Prompt Templates for Information-Augmented Regeneration


The user can replace ``..." part with the corresponding content according to the subject:
    

You're a veteran algorithm player. Write a program in C++ with the following information:

[Problem Modeling] : (Concisely describe the idea of the problem, transform the problem into a formal algorithm model, define the core variables, operations, and goals)
...

[Algorithm goal] : (Specify the performance goal of the algorithm, including time complexity, space complexity, maintainability, or reusability)
...

[Algorithm ideas] : (Provide the core ideas or design framework for solving the problem. If the classical algorithm template can be reused, it should be indicated.)
...

[Implementation details] : (Explain the key technical details in the implementation process.)
...

[Constraints] : (Specify input and output specifications, data ranges, boundary cases, legal input guarantees, whether there are specially constructed inputs, etc.)
...



