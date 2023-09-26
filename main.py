import os
from datetime import datetime

def process_line(line):
    line = line.strip()
    cols = line.split(",")

    if len(cols) < 23:
        return None, None

    try:
        date_str = cols[5].replace('"', '').split(" ")[0]
        date_obj = datetime.strptime(date_str, '%m/%d/%y')
        
        # Adjust year to be in the 20th century
        if date_obj.year >= 2000:
            date_obj = date_obj.replace(year=date_obj.year - 100)
        
        formatted_date = date_obj.strftime('%d/%m/%Y')
    except:
        formatted_date = ""

    # Include "l" and "s" (indexed as 15 and 16) while skipping the "edad" (indexed as 1) and second-to-last columns (indexed as -2)
    new_cols = [cols[0]] + cols[2:5] + [f'"{formatted_date}"'] + cols[6:15] + cols[15:17] + [cols[-1]]
    return cols[0].replace('"', ''), ",".join(new_cols) + "\n"

def main():
    seen_cves = set()
    with open("merged.csv", 'w', encoding='utf-8') as f_out:
        f_out.write("clave_elector,nombre,apellido_paterno,apellido_materno,fecha_nacimiento,sexo,calle,numero_interior,numero_exterior,colonia,codigo_postal,id_estado,d,numero_municipio,seccion,localidad,curp\n")
        
        for filename in os.listdir("input"):
            if filename.endswith(".csv"):
                with open(os.path.join("input", filename), 'r', encoding='utf-8') as f_in:
                    # Skip headers
                    next(f_in)
                    for line in f_in:
                        cve, processed_line = process_line(line)
                        if processed_line and cve not in seen_cves:
                            seen_cves.add(cve)
                            f_out.write(processed_line)

if __name__ == "__main__":
    main()
