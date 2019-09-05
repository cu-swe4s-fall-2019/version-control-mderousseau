def div(a, b):
    if b == 0:
        print("Error, cannot divide by zero")
    else:
        return a/b
    
def add(a, b):
    return a + b

# Example calculation
def main():
    c = ml.add(2, 5)
    d = ml.div(10, 5)
    print(c)
    print(d)
    
if __name__ == '__main__':
    main()
