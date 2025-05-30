#!/usr/bin/python3
"""Function that indents text"""


def text_indentation(text):
   """String validation"""
   if not isinstance(text, str):
       raise TypeError("text must be a string")

   sep = [".", "?", ":"]
   idx_prev = 0

   for i in range(len(text)):
       if i == len(text) - 1:
           print(text[idx_prev:i + 1], end="")
       elif text[i] in sep:
           print(text[idx_prev:i + 1] + '\n')
           idx_prev = i + 1

           while text[idx_prev] == " ":
               idx_prev += 1
