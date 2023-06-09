



def calculate_adjusted_timing(in_game_dpi, mouse_dpi):
    original_timing = 0.25  ## script dev's ingame dpi, 800 is mouse
    adjusted_timing = original_timing * (mouse_dpi / 800) / (in_game_dpi / 0.25)
    return adjusted_timing

def main():
    in_game_dpi = 0.6 #ur
    mouse_dpi = 1000  #ur

    adjusted_timing = calculate_adjusted_timing(in_game_dpi, mouse_dpi)
    print("Adjusted Timing: ", adjusted_timing)

if __name__ == "__main__":
    main()



