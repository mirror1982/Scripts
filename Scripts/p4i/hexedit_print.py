def hexedit_print(buf, line_size = 0x10):
    heading = "Offset(h) " + " ".join(format(n, '02x') for n in range(line_size))
    print heading

    for i in range(len(buf) / line_size):
        line = format(i*line_size, '08x') + "  "
        for j in range(line_size):
            line += buf[i*line_size+j].encode("hex") + " "
        line += " " + my_esc(buf[i*line_size:(i+1)*line_size])
        print line
    
    finel_line_start = len(buf) / line_size * line_size	
    final_line_len = len(buf) - finel_line_start

    if final_line_len > 0:
        line = format(finel_line_start, '08x') + "  "
        for j in range(final_line_len):
            line += buf[finel_line_start+j].encode("hex") + " "
        line = line.ljust(8 + 2 + 3*line_size, " ")
        line += " " + my_esc(buf[finel_line_start:len(buf)])
        print line