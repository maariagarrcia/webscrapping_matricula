from bs4 import BeautifulSoup

def parse_emails_from_html(html_content):
    with open(html_content, 'r') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')
    emails = []
    for div in soup.find_all('div', {'class': 'moz-cite-prefix'}):
        email = {}
        email['date'] = div.get_text(strip=True).replace('El ', '').replace(' de agosto de 2017', '').strip()
        # Extracción de la información de la matrícula
        matricula_info = div.find_next('p').get_text(strip=True)
        # Dividir la información de la matrícula en líneas y asignar los valores correspondientes
        lines = matricula_info.split('\n')
        if len(lines) >= 5:  # Verificar si hay suficientes líneas para dividir
            email['Matricula:'] = lines[0].split(':')[1].strip()
            email['Fecha de matriculación:'] = lines[1].split(':')[1].strip()
            email['Color:'] = lines[2].split(':')[1].strip()
            email['Marca:'] = lines[3].split(':')[1].strip()
            email['Modelo:'] = lines[4].split(':')[1].strip()
            emails.append(email)
        else:
            print("No se pudo extraer la información de la matrícula correctamente.")

    return emails

if __name__ == '__main__':
    # Reemplaza "matricula.html" con la ruta correcta de tu archivo HTML
    emails = parse_emails_from_html("matricula.html")
    for email in emails:
        print('Matricula:', email.get('Matricula', 'No disponible'))
        print('Fecha de matriculación:', email.get('Fecha de matriculación', 'No disponible'))
        print('Color:', email.get('Color', 'No disponible'))
        print('Marca:', email.get('Marca', 'No disponible'))
        print('Modelo:', email.get('Modelo', 'No disponible'))
        print('---')
