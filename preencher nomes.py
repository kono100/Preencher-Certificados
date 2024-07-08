from PIL import Image, ImageDraw, ImageFont

nomes = ["Thiago Campos", "Ana Silva", "Carlos Souza", "Fernanda Lima", "Paula Fernandes", "Thiago Campos"]
fonte = ImageFont.truetype("arial.ttf", 90)
diploma_base = "Certificado-em-Branco.png"
coordenada_y_texto = 700

for nome in nomes:
    imagem = Image.open(diploma_base)
    draw = ImageDraw.Draw(imagem)
    largura_texto, altura_texto = draw.textbbox((0, 0), nome, font=fonte)[2:4]
    largura_imagem = imagem.width
    coordenada_x_texto = (largura_imagem - largura_texto) // 2
    draw.text((coordenada_x_texto, coordenada_y_texto), nome, font=fonte, fill="black")
    imagem.save(f"Certificados Preenchidos/{nome}.png")

print("Diplomas gerados com sucesso!")
