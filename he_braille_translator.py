import re

def process_braille(text):
    # Mapping for Hebrew letters and punctuation
    he_to_br = {
        'א': '⠁', 'ב': '⠃', 'ג': '⠛', 'ד': '⠙', 'ה': '⠑', 'ו': '⠺', 'ז': '⠵', 'ח': '⠭', 'ט': '⠞', 'י': '⠊',
        'כ': '⠌', 'ך': '⠌', 'ל': '⠇', 'מ': '⠍', 'ם': '⠍', 'נ': '⠝', 'ן': '⠝', 'ס': '⠎', 'ע': '⠯', 'פ': '⠏',
        'ף': '⠏', 'צ': '⠿', 'ץ': '⠿', 'ק': '⠟', 'ר': '⠗', 'ש': '⠱', 'ת': '⠾', ' ': ' ',
        '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖', ':': '⠒', '-': '⠤', "'": '⠈', '"': '⠜'
    }
    br_to_he = {v: k for k, v in he_to_br.items() if k not in 'ךםןףץ'}
    
    num_map = {'1': '⠁', '2': '⠃', '3': '⠛', '4': '⠙', '5': '⠑', '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚'}
    rev_num = {v: k for k, v in num_map.items()}

    # Auto-detection for Braille Unicode range
    if re.search(r'[\u2800-\u28FF]', text):
        res, is_num = [], False
        for char in text:
            if char == '⠼': is_num = True
            elif char == ' ': 
                is_num = False
                res.append(' ')
            elif is_num: res.append(rev_num.get(char, ''))
            else: res.append(br_to_he.get(char, '?'))
        return "".join(res)
    
    # Hebrew to Braille
    res, is_num = [], False
    for char in text:
        if char.isdigit():
            if not is_num: 
                res.append('⠼')
                is_num = True
            res.append(num_map[char])
        else:
            is_num = False
            res.append(he_to_br.get(char, ''))
    return "".join(res)

if __name__ == "__main__":
    print("Hebrew Braille Translator (type 'exit' to quit)")
    while True:
        user_input = input("\nInput: ").strip()
        if user_input.lower() in ['exit', 'quit', 'יציאה']:
            break
        if not user_input:
            continue
        print(f"Result: {process_braille(user_input)}")