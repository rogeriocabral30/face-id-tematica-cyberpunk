import cv2
from deepface import DeepFace
import os
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

# Caminho da imagem de referência
ARQUIVO_FOTO = "meu_rosto.jpg"

# Lista de comandos disponíveis
servicos_disponiveis = {
    "spotify": "start spotify",
    "google": "start https://www.google.com",
    "youtube": "start https://www.youtube.com",
    "email": "start https://mail.google.com",
    "whatsapp": "start https://web.whatsapp.com",
    "drive": "start https://drive.google.com",
    "netflix": "start https://www.netflix.com",
    "chatgpt": "start https://chat.openai.com",
    "notepad": "notepad",
    "calculadora": "calc",
    "agenda": "start https://calendar.google.com",
    "maps": "start https://www.google.com/maps",
    "tradutor": "start https://translate.google.com"
}

# Captura uma nova imagem de referência
def tirar_foto_referencia():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    time.sleep(1)
    ret, frame = cap.read()
    if ret and frame is not None:
        cv2.imwrite(ARQUIVO_FOTO, frame)
        messagebox.showinfo("Foto Atualizada", "Nova foto de referência salva com sucesso!")
    else:
        messagebox.showerror("Erro", "Não foi possível capturar a imagem.")
    cap.release()

# Verifica se a imagem de referência existe
def verificar_ou_criar_foto_referencia():
    if not os.path.exists(ARQUIVO_FOTO):
        messagebox.showinfo("Foto de Referência", "Vamos tirar uma foto sua para usar como referência.")
        tirar_foto_referencia()

# Executa os serviços solicitados
def executar_tarefas(comandos):
    status_label.config(text="✅ ROSTO RECONHECIDO! Executando tarefas...")
    root.update()

    for comando in comandos:
        if comando in servicos_disponiveis:
            os.system(servicos_disponiveis[comando])
            time.sleep(1)

    status_label.config(text="✅ Tarefas concluídas!")

# Solicita os serviços desejados via caixa de diálogo
def solicitar_comandos():
    entrada = simpledialog.askstring("O que você quer abrir?", 
        "Digite os serviços ou apps separados por vírgula:\n\nEx: spotify, google, youtube, email, whatsapp, drive, netflix, chatgpt, notepad, calculadora, agenda, maps, tradutor")
    if entrada:
        comandos = [c.strip().lower() for c in entrada.split(",")]
        return comandos
    return []

# Inicia o reconhecimento facial
def iniciar_reconhecimento():
    verificar_ou_criar_foto_referencia()
    status_label.config(text="🎥 Iniciando reconhecimento... Olhe para a câmera.")
    root.update()

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    contador = 0
    ja_executou = False

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            continue

        if contador % 30 == 0 and not ja_executou:
            try:
                cv2.imwrite("temp_verify.jpg", frame)

                if not os.path.exists("temp_verify.jpg") or os.path.getsize("temp_verify.jpg") == 0:
                    print("❌ Imagem capturada está vazia ou inválida.")
                    continue

                resultado = DeepFace.verify(
                    img1_path="temp_verify.jpg",
                    img2_path=ARQUIVO_FOTO,
                    model_name="VGG-Face",
                    enforce_detection=True
                )
                print("Resultado:", resultado)

                if resultado['verified']:
                    comandos = solicitar_comandos()
                    if comandos:
                        executar_tarefas(comandos)
                    ja_executou = True
                else:
                    status_label.config(text="❌ Rosto não reconhecido.")
                    root.update()

            except Exception as e:
                print("Erro durante verificação:", e)

        contador += 1
        cv2.imshow('Reconhecimento Facial (pressione Q para sair)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or ja_executou:
            break

    cap.release()
    cv2.destroyAllWindows()
    if os.path.exists("temp_verify.jpg"):
        os.remove("temp_verify.jpg")

# --- INTERFACE TKINTER COM MODO ESCURO ---
root = tk.Tk()
root.title("Automação com Reconhecimento Facial")
root.geometry("520x420")
root.configure(bg="#1e1e1e")

tk.Label(root, text="Reconhecimento Facial Automático", font=("Arial", 14, "bold"), fg="white", bg="#1e1e1e").pack(pady=10)

tk.Button(root, text="Iniciar Reconhecimento", command=iniciar_reconhecimento, bg="#2e8b57", fg="white", font=("Arial", 11)).pack(pady=10)

tk.Button(root, text="Atualizar Foto de Referência", command=tirar_foto_referencia, bg="#444", fg="white", font=("Arial", 10)).pack(pady=5)

status_label = tk.Label(root, text="Aguardando...", fg="lightblue", bg="#1e1e1e", font=("Arial", 10))
status_label.pack(pady=20)

tk.Label(root, text="Dica: digite nomes como 'spotify', 'youtube', 'email', etc.", fg="gray", bg="#1e1e1e", font=("Arial", 9)).pack()

root.mainloop()