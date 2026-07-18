import time
def typing_effect(text, duration, delay):
    """
    Display text with a typing animation.

    Parameters:
        text (str): Text to display.
        duration (float): Total text typing duration.
        delay (float): Pause before the next line.
    """
    if not text:
        print()
        time.sleep(delay)
    else:
        speed = duration / len(text)
        for i in range(1, len(text) + 1):
            print(text[:i], end="\r", flush=True)
            time.sleep(speed)
        print()
        time.sleep(delay)

# Usage Example
typing_effect("willson andre simamora", 5, 2)
typing_effect("STEI-R ITB 26", 3, 0)
