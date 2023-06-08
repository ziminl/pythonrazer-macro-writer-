


def generate_razer_macro(macro_name, macro_commands):
    macro_file = f"{macro_name}.macro"

    with open(macro_file, 'w') as file:
        file.write("[MACRO]\n")
        file.write(f"Name={macro_name}\n")
        file.write("Enabled=1\n")
        file.write("Sequence=\n")

        for command in macro_commands:
            file.write(f"{command}\n")

    print(f"Macro '{macro_name}' generated")

# Usage example
macro_name = "MyMacro"
macro_commands = [
    "LeftMouseButton",
    "Delay=1000",
    "RightMouseButton",
    "Delay=500",
    "MouseMoveRelativeX=100",
    "MouseMoveRelativeY=50",
    "Delay=200",
    "KeyPress=Space",
]

generate_razer_macro(macro_name, macro_commands)


