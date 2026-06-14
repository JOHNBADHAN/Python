def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
        
    except Exception as e:
        print(e) 
        return

    finally:  # Executed regardless of error
        print("Hey I am inside of finally")

main()