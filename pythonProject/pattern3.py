height=5
for i in range(height):

        print(' ' * (height - i - 1), end=' ')

        for j in range(1, i + 2):
            print(j, end=' ')
        print()  # Move to the next line

