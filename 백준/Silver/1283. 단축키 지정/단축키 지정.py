n = int(input())
keyboard_shortcut = set()

for _ in range(n):
    option = input().split()
    
    save_key = False
    save_option = ""
    for word in option:
        key = word[0].lower()
        if key not in keyboard_shortcut and not save_key:
            keyboard_shortcut.add(key)
            save_key = True
            save_option += "[" + word[0] + "]" + word[1:]
        else:
            save_option += word
        save_option += " "

    if not save_key:
        save_option = ""
        save_word = False
        for word in option:
            for w in word:
                lower_w = w.lower()
                if lower_w not in keyboard_shortcut and not save_word:
                    keyboard_shortcut.add(lower_w)
                    save_word = True
                    save_option += "[" + w + "]"
                else:
                    save_option += w
            save_option += " "
    print(save_option.rstrip())