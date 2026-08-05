# Mistakes — 030

## Wrong Idea #1

Add more linear layers. Depth increases, but expressive power does not. Use a hard yes-or-no threshold; it creates decisions but supplies almost no useful gradient.

## Why it fails

A deep learner needs a simple nonlinearity that changes which paths respond while remaining trainable.

## Correct idea

Place an activation after a linear transformation. ReLU opens positive paths; smoother gates such as GELU vary them gradually.
