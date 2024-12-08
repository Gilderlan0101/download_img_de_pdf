from flask import Blueprint, render_template, request, send_file, redirect, url_for, flash
from io import BytesIO
from zipfile import ZipFile
from PyPDF2 import PdfReader
from PIL import Image
import io
import asyncio

home_ = Blueprint('home', __name__, template_folder='../templates', static_folder='../static')

@home_.route('/', methods=['GET', 'POST'])
async def home_page():
    if request.method == 'POST':
        try:
            # Obter o arquivo PDF enviado pelo usuário
            pdf_file = request.files['pdfFile']
            if not pdf_file.filename.endswith('.pdf'):
                flash('Somente arquivos PDF são suportados.', 'warning')
                return redirect(url_for('home.home_page'))

            # Ler o PDF
            reader = PdfReader(pdf_file)

            # Criar um arquivo ZIP em memória
            zip_buffer = BytesIO()
            with ZipFile(zip_buffer, 'w') as zip_file:
                # Iterar sobre todas as páginas e imagens
                tasks = []
                for page_index, page in enumerate(reader.pages):
                    if hasattr(page, 'images'):
                        for img_index, img_Pdf in enumerate(page.images):
                            tasks.append(process_image(img_Pdf, page_index, img_index, zip_file))

                # Esperar as tarefas de processamento serem concluídas
                await asyncio.gather(*tasks)

            # Preparar o arquivo ZIP para download
            zip_buffer.seek(0)
            return send_file(
                zip_buffer,
                download_name='images_from_pdf.zip',
                mimetype='application/zip'
            )

        except Exception as e:
            print(f"Erro ao processar o arquivo PDF: {e}")
            flash('Ocorreu um erro ao processar o arquivo enviado. Certifique-se de que é um PDF válido com imagens.', 'error')
            return redirect(url_for('home.home_page'))

    return render_template('home.html')


async def process_image(img_Pdf, page_index, img_index, zip_file):
    try:
        # Nomear cada imagem no ZIP
        image_name = f"page{page_index + 1}_image{img_index + 1}.png"
        img_data = io.BytesIO(img_Pdf.data)
        img_pil = Image.open(img_data)

        # Verificar e converter modos de cores
        if img_pil.mode == "P":
            if img_pil.palette and len(img_pil.palette.palette) % 3 != 0:
                raise ValueError(f"Tamanho da paleta inválido na página {page_index + 1}, imagem {img_index + 1}")
            img_pil = img_pil.convert("RGB")
        elif img_pil.mode not in ["RGB", "L"]:
            img_pil = img_pil.convert("RGB")

        # Adicionar a imagem ao ZIP
        img_bytes_io = BytesIO()
        img_pil.save(img_bytes_io, format="PNG")
        img_bytes_io.seek(0)
        zip_file.writestr(image_name, img_bytes_io.getvalue())
    except Exception as e:
        print(f"Erro ao processar imagem (page={page_index + 1}, img={img_index + 1}): {e}")
        raise
