def remove_extra_consecutive(input_str, max_consecutive_chars):
    output, prev_char, current_char_seen = '', None, 0
    for current_char in input_str:
        if current_char == prev_char:
            current_char_seen += 1
        else:
            current_char_seen = 0
            prev_char = current_char
        if current_char_seen < max_consecutive_chars:
            output += current_char
    return output

print remove_extra_consecutive('aaabbbb', 2)