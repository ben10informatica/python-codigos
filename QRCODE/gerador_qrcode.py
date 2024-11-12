import qrcode

# Dados para o QR Code
data = "https://www.epicgames.com"

# Criar instância do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Adicionar dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Criar imagem do QR Code
img = qr.make_image(fill_color="blue", back_color="red")

# Salvar imagem
img.save("qrcode.png")

print("QR Code gerado com sucesso!")
