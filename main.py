from datetime import datetime

def read_csv_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

def write_csv_file(file_path, lines):
    with open(file_path, 'w') as f:
        f.writelines(lines)

def process_line(line):
    line = line.strip()
    cols = line.split(",")
    
    if len(cols) < 23:
        return None
    
    try:
        date_str = cols[5].replace('"', '').split(" ")[0]
        date_obj = datetime.strptime(date_str, '%m/%d/%y')
        formatted_date = date_obj.strftime('%d/%m/%Y')
    except:
        formatted_date = ""
    
    # Exclude columns "s,l,mza,consec,cred,folio,nac" by slicing
    new_cols = cols[:5] + [f'"{formatted_date}"'] + cols[6:13] + [cols[18]] + [cols[-1]]
    return ",".join(new_cols) + "\n"

def main():
    csv1_lines = read_csv_file("1.csv")
    csv2_lines = read_csv_file("2.csv")
    
    processed_lines = set()
    for line in csv1_lines[1:] + csv2_lines[1:]:
        processed_line = process_line(line)
        if processed_line:
            processed_lines.add(processed_line)
    
    processed_lines = sorted(list(processed_lines))
    write_csv_file("merged.csv", ["cve,edad,nombre,paterno,materno,fecnac,sexo,calle,int,ext,colonia,cp,e,d,m,cred,curp\n"] + processed_lines)

if __name__ == "__main__":
    main()
