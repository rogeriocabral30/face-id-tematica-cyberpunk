import cv2
from deepface import DeepFace
import os
import time

# --- CONFIGURAÇÃO ---
ARQUIVO_FOTO = "meu_rosto.jpg"

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal
    print("="*40)
    print("      CONFIGURAÇÃO DA SESSÃO")
    print("="*40)
    print("O que você deseja abrir ao ser reconhecido?")
    print("\n[1] Spotify 🎵")
    print("[2] Google 🔎")
    print("[3] YouTube 📺")
    print("[4] Email 📧")
    print("[5] TODOS OS ITENS ACIMA 🚀")
    print("="*40)
    
    escolha = input("Digite os números desejados (ex: 1 3): ")
    return escolha

def executar_tarefas(opcoes):
    print("\n✅ ROSTO RECONHECIDO! Executando tarefas escolhidas...")
    
    # Verifica o que o usuário digitou e abre os apps correspondentes
    
    # Opção 1 ou 5 (Todos): Abre Spotify
    if '1' in opcoes or '5' in opcoes:
        print("- Abrindo Spotify...")
        os.system("start spotify")
        time.sleep(1)

    # Opção 2 ou 5: Abre Google
    if '2' in opcoes or '5' in opcoes:
        print("- Abrindo Google...")
        os.system("start https://www.google.com")

    # Opção 3 ou 5: Abre YouTube
    if '3' in opcoes or '5' in opcoes:
        print("- Abrindo YouTube...")
        os.system("start https://www.youtube.com")

    # Opção 4 ou 5: Abre Email
    if '4' in opcoes or '5' in opcoes:
        print("- Abrindo Email...")
        os.system("start https://mail.google.com") # Mude para outlook.live.com se preferir
    
    print("\n>> TAREFAS CONCLUÍDAS! <<")

def iniciar_automacao():
    # Pergunta as opções ANTES de ligar a câmera
    opcoes_usuario = mostrar_menu()

    print("\n--- INICIANDO VIGILÂNCIA... ---")
    print("Olhe para a câmera...")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    contador = 0
    ja_executou = False 

    while True:
        ret, frame = cap.read()
        if not ret: break

        if contador % 30 == 0 and not ja_executou:
            try:
                cv2.imwrite("temp_verify.jpg", frame)

                resultado = DeepFace.verify(
                    img1_path = "temp_verify.jpg", 
                    img2_path = ARQUIVO_FOTO, 
                    model_name = "VGG-Face",
                    enforce_detection = False 
                )

                if resultado['verified']:
                    # Passamos as escolhas do usuário para a função de execução
                    executar_tarefas(opcoes_usuario)
                    ja_executou = True 
                else:
                    print("Rosto não compatível...")

            except Exception as e:
                pass 

        contador += 1
        cv2.imshow('SISTEMA DE AUTOMACAO (Q para sair)', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    if os.path.exists("temp_verify.jpg"):
        os.remove("temp_verify.jpg")

if __name__ == "__main__":
    iniciar_automacao()