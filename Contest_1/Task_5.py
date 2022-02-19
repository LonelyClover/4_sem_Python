def draw_square(n):
  draw_rect(n, n)

def draw_rect(n, m):
  if n <= 0:
    return
  else:
    draw_row(m)
    draw_rect(n - 1, m)

def draw_row(n):
  if n <= 0:
    print()
  else:
    print("*", end='')
    draw_row(n - 1)

draw_square(int(input()))
