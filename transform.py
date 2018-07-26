from flask import Flask, request, send_file, send_from_directory
from PyPDF2 import PdfFileMerger
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def pdftransform():
    if request.method == 'POST':

        pdfs = request.files.getlist("pdf[]")

        nombre_archivo_salida = "salida.pdf"
        fusionador = PdfFileMerger()

        for pdf in pdfs:
            #PRIMERO DEBO SUBIR LOS ARCHIVOS
            pdf.save(secure_filename(pdf.filename))
            #LUEGO DEBO UNIRLOS
            fusionador.append(open(pdf.filename, 'rb'))

        with open(nombre_archivo_salida, 'wb') as salida:
            fusionador.write(salida)
        
        return send_file('salida.pdf', as_attachment=True)


  
if __name__ == "__main__":
    app.run(debug=True)
