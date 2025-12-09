def write_file(message = None, binary = False, output_file = None):
        try:
            if not output_file:
                raise ValueError("No output file specified")
        except ValueError as e: 
            print(f"Error: {e}")
        else:
            mode = "wb" if binary else "w"
            with open(output_file, mode) as f:
                if binary and isinstance(message, str):
                    f.write(message.encode('utf-8'))
                else:
                    f.write(message)
        finally:
            print("Write to file completed.")

def read_file(binary=False, input_file=None):
    try:
        if not input_file:
            raise ValueError("No input file specified")
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    else:
        mode = "rb" if binary else "r"
        with open(input_file, mode) as f:
            return f.read()
    finally:
        print("Read file completed.")
        