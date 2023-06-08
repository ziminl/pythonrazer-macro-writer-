








import xml.etree.ElementTree as ET
import keyboard

def generate_synapse_macro(key_combo, macro_text):
    macro_element = ET.Element("Macro")
    macro_element.set("name", "Macro")
    
    key_combo_element = ET.SubElement(macro_element, "KeyCombo")
    key_combo_element.text = key_combo
    
    action_element = ET.SubElement(macro_element, "Action")
    action_element.set("type", "Key")
    action_element.text = macro_text
    
    macro_tree = ET.ElementTree(macro_element)
    return ET.tostring(macro_element).decode()

def execute_macro():
    key_combo = "CTRL+SHIFT+M"
    macro_text = "Hello, World!"
    
    synapse_macro = generate_synapse_macro(key_combo, macro_text)
    print("Razer Synapse Macro:")
    print(synapse_macro)

    while True:
        if keyboard.is_pressed("CTRL") and keyboard.is_pressed("SHIFT") and keyboard.is_pressed("M"):
            print("Executing Macro...")
            #your macro execution code here
            break

execute_macro()




