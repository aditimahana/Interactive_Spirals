# Interactive Turtle Spirals 🎨

## 📖 Introduction

This repository contains two creative Python Turtle graphics exercises from Section 3 of *Teach Your Kids to Code*.

The programs explore how user input can be combined with loops, mathematical expressions, and Turtle graphics to generate personalised visual designs.

One program allows users to customise a geometric spiral by selecting its number of sides, while the other transforms the user's name into a colourful spiral animation.

## 📂 Programs

### 1. ColorSpiralInput.py

An interactive geometric spiral generator that allows users to choose the number of sides for their design.

**What it does:**
- Opens a black Turtle graphics window.
- Displays a numerical input prompt asking the user to choose between 1 and 8 sides.
- Generates a colourful spiral based on the selected number.
- Alternates between eight different colours.
- Gradually increases the pen width as the spiral develops.

**What it should look like:**

A colourful geometric spiral drawn against a black background. The pattern changes depending on the number of sides selected, creating different polygon-inspired shapes.

### 2. SpiralMyName.py

A personalised Turtle graphics animation that writes the user's name repeatedly in a spiral formation.

**What it does:**
- Opens a black Turtle graphics window.
- Asks the user to enter their name through a pop-up input window.
- Writes the name 100 times around a spiral.
- Alternates between four different pen colours.
- Gradually increases the font size.
- Changes the Turtle's position and direction after each repetition.

**What it should look like:**

A colourful spiral made up of repeated instances of the user's name. Each repetition appears further along the spiral, with the text gradually increasing in size.

## 🛠️ What I Learned

- **Turtle graphics:** Creating visual patterns using Python's Turtle module.
- **User input:** Using `turtle.numinput()` and `turtle.textinput()` to collect information through pop-up windows.
- **For loops:** Repeating drawing and writing instructions.
- **Lists:** Storing multiple colours and accessing them by index.
- **Modulo operator:** Using `%` to cycle through colours.
- **Mathematical expressions:** Calculating movement distances, rotation angles, and font sizes.
- **Pen controls:** Using `penup()` and `pendown()` to control when the Turtle draws.
- **Customisation:** Changing background colours, pen colours, and font properties.

## 🚀 How to Run

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in your Python IDE.
4. Run either program:

```bash
python ColorSpiralInput.py
```

Or:

```bash
python SpiralMyName.py
```

Follow the pop-up prompts to customise your spiral or enter your name.

## 📚 Credits

These exercises are based on Section 3 of *Teach Your Kids to Code* by Bryson Payne.

The programs were completed as part of my Python learning journey.

---

**Course:** *Teach Your Kids to Code*  
**Section:** 3  
**Language:** Python  
**Module:** Turtle Graphics
