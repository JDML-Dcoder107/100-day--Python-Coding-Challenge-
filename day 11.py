def summary (*args, **kwargs):
    """
    This function takes any number of positional and keyword arguments and prints a summary of them.
    
    Args:
        *args: Variable length positional arguments.
        **kwargs: Variable length keyword arguments.
    """
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)


collected_args = []
collected_kwargs = {}
count = 0

while True:
    user_input = input(f'Please enter element {count + 1} (or "exit" to stop): ')
    if user_input == "exit":
        break
    if "=" in user_input:
        key, value = user_input.split("=", 1)  # split on first "=" only
        collected_kwargs[key.strip()] = value.strip()
    else:
        collected_args.append(user_input)
    count += 1

summary(*collected_args, **collected_kwargs)