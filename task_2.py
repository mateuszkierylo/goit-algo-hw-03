import turtle

def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)

def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    # Set up the turtle graphics environment
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    
    # Get the level of recursion from the user
    level = int(input("Enter the level of recursion (e.g., 3): "))
    
    # Draw the Koch snowflake
    draw_koch_snowflake(t, 400, level)
    
    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
