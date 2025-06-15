from fpdf import FPDF

def solicitar_datos_proyecto():
    descripcion = input("Digita la descripción del proyecto: ")
    horas_estimadas = int(input("Digita las horas estimadas: "))
    valor_hora = int(input("Digita el valor por hora: "))
    tiempo_estimado = int(input("Digita el tiempo estimado en días: "))
    valor_total = horas_estimadas * valor_hora
    return descripcion, horas_estimadas, valor_hora, tiempo_estimado, valor_total

def crear_pdf(descripcion, horas, valor_hora, tiempo, valor_total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    try:
        pdf.image("template.png", x=0, y=0, w=210)  # Ajuste a tamaño A4 si es necesario
    except RuntimeError:
        print("No se pudo cargar la imagen 'template.png'. Verifica que exista en el directorio.")
    
    # Posiciones ajustables
    pdf.text(115, 145, descripcion)
    pdf.text(115, 160, str(horas))
    pdf.text(115, 175, str(valor_hora))
    pdf.text(115, 190, str(tiempo))
    pdf.text(115, 205, str(valor_total))

    pdf.output("presupuesto.pdf")
    print("✅ Presupuesto generado con éxito.")

if __name__ == "__main__":
    descripcion, horas, valor_hora, tiempo, valor_total = solicitar_datos_proyecto()
    print(f"""
Resumen del Proyecto:
📌 Proyecto: {descripcion}
⏱ Horas estimadas: {horas}
💰 Valor por hora: {valor_hora}
📅 Tiempo estimado: {tiempo} días
💵 Valor total: {valor_total}
""")
    crear_pdf(descripcion, horas, valor_hora, tiempo, valor_total)
