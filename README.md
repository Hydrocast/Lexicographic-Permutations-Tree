# Lexicographic Permutations Tree

**Author:** Giannis Loizou  
**Description:** Generates all permutations of the set {1, 2, ..., n} using a **tree-based approach**.

---

## Overview

This project implements an original approach to generating permutations in **lexicographic order** using a **linked tree structure**.  

- Each node represents an element of the set.  
- Children represent subsequent elements in the permutation.  
- The `mixer` function recursively swaps root elements to generate all permutations.  

This implementation demonstrates:

- Custom tree data structures
- Breadth-first traversal
- Lexicographic permutation generation without using Python's built-in `itertools.permutations`

---

## Features

- Construct a tree with all possible permutation paths
- Print each permutation in lexicographic order
- Interactive command-line program
- Modular, object-oriented design (abstract `Tree` class and concrete `LinkedTree` class)

---

## Usage

1. Clone the repository: git clone https://github.com/Hydrocast/Lexicographic-Permutations-Tree.git

2. cd LexicographicPermutationsTree

3. Run the program: python3 permutations_tree.py

4. Enter a positive integer n when prompted. The program will display all permutations of {1, 2, ..., n} in lexicographic order.

---

## Example:
Enter a positive integer n: 3

{ 1, 2, 3 }
{ 1, 3, 2 }
{ 2, 1, 3 }
{ 2, 3, 1 }
{ 3, 1, 2 }
{ 3, 2, 1 }
