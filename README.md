<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FaceID - Cyberpunk Edition</title>
    <style>
        :root {
            --bg-color: #0d0d0d;
            --card-bg: #1a1a1a;
            --text-color: #e0e0e0;
            --accent-color: #00ff9d; /* Verde Neon */
            --secondary-color: #bd00ff; /* Roxo Neon */
            --code-bg: #2d2d2d;
        }

        body {
            font-family: 'Courier New', Courier, monospace; /* Fonte estilo terminal */
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background-color: var(--card-bg);
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 255, 157, 0.1);
            border: 1px solid #333;
        }

        h1, h2, h3 {
            color: var(--accent-color);
            text-transform: uppercase;
            letter-spacing: 2px;
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 10px;
            margin-top: 30px;
        }

        h1 { font-size: 2.5em; text-align: center; border-bottom: none; }

        .badges { text-align: center; margin-bottom: 30px; }
        .badges img { margin: 5px; }

        blockquote {
            background: rgba(189, 0, 255, 0.1);
            border-left: 5px solid var(--secondary-color);
            margin: 20px 0;
            padding: 15px;
            font-style: italic;
            color: #fff;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: #111;
        }

        th, td {
            padding: 12px;
            border: 1px solid #333;
            text-align: left;
        }

        th { background-color: var(--secondary-color); color: white; }
        tr:nth-child(even) { background-color: #1a1a1a; }
        tr:hover { background-color: #222; }

        code, pre {
            background-color: var(--code-bg);
            color: var(--accent-color);
            font-family: 'Consolas', monospace;
            padding: 2px 5px;
            border-radius: 4px;
        }

        pre {
            padding: 15px;
            overflow-x: auto;
            border-left: 3px solid var(--accent-color);
        }

        .author-section {
            margin-top: 50px;
            text-align: center;
            border-top: 1px solid #333;
            padding-top: 20px;
        }

        a { color: var(--accent-color); text-decoration: none; font-weight: bold; }
        a:hover { text-decoration: underline; color: var(--secondary-color); }

        .cmd-example {
            background-color: #000;
            border: 1px solid var(--accent-color);
            padding: 10px;
            color: var(--accent-color);
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Título -->
        <h1>🔐 FaceID Cyberpunk</h1>
        
        <!-- Badges -->
        <div class="badges">
            <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
            <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
            <img src="https://img.shields.io/badge/AI-DeepFace-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="DeepFace">
            <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows">
        </div>

        <blockquote>
            "A senha é o seu rosto. O resto é obsoleto."
        </blockquote>

        <h2>🌐 Sobre o Projeto</h2>
        <p>
            Este projeto é uma aplicação de <strong>Segurança Biométrica</strong> e <strong>Automação</strong> com estética Dark/Cyberpunk. 
            Utilizando algoritmos de Deep Learning (modelo <strong>VGG-Face</strong>), o sistema captura a imagem da webcam, verifica a identidade do usuário com alta precisão e libera um terminal de comando para execução de tarefas automatizadas.
        </p>
        <p>É a união perfeita entre segurança (Reconhecimento Facial) e produtividade (Automação de Apps).</p>

        <h2>⚡ Funcionalidades</h2>
        <ul>
            <li><strong>👁️ Biometria Facial:</strong> Comparação em tempo real usando a biblioteca <code>DeepFace</code>.</li>
            <li><strong>📸 Cadastro Automático:</strong> Captura e salva a "Face de Referência" automaticamente se não existir.</li>
            <li><strong>🚀 Launcher de Apps:</strong> Abra múltiplos softwares e sites com uma única linha de comando.</li>
            <li><strong>💻 Interface Dark:</strong> UI construída em Tkinter com tema escuro (#1e1e1e) para conforto visual.</li>
        </ul>

        <h2>🛠️ Comandos de Automação</h2>
        <p>Após o reconhecimento facial ser <strong>validado</strong>, o sistema libera o acesso. Você pode digitar os seguintes comandos (separados por vírgula para abrir vários de uma vez):</p>

        <table>
            <thead>
                <tr>
                    <th>Comando</th>
                    <th>Ação</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>spotify</td><td>Abre o Spotify</td></tr>
                <tr><td>whatsapp</td><td>Abre o WhatsApp Web</td></tr>
                <tr><td>chatgpt</td><td>Acessa o ChatGPT</td></tr>
                <tr><td>netflix</td><td>Abre a Netflix</td></tr>
                <tr><td>youtube</td><td>Abre o YouTube</td></tr>
                <tr><td>google</td><td>Abre a pesquisa Google</td></tr>
                <tr><td>email</td><td>Abre o Gmail</td></tr>
                <tr><td>drive</td><td>Acessa o Google Drive</td></tr>
                <tr><td>maps</td><td>Abre o Google Maps</td></tr>
                <tr><td>tradutor</td><td>Abre o Google Tradutor</td></tr>
                <tr><td>notepad</td><td>Abre o Bloco de Notas (Windows)</td></tr>
                <tr><td>calculadora</td><td>Abre a Calculadora (Windows)</td></tr>
                <tr><td>agenda</td><td>Abre o Google Calendar</td></tr>
            </tbody>
        </table>

        <p><strong>Exemplo de uso:</strong></p>
        <div class="cmd-example">
            > Digite: spotify, chatgpt, notepad<br>
            <span style="color: #888;">// Resultado: O sistema abrirá os três aplicativos simultaneamente.</span>
        </div>

        <h2>📦 Instalação e Uso</h2>
        <p>Este projeto requer bibliotecas robustas de visão computacional.</p>

        <h3>1. Pré-requisitos</h3>
        <p>Certifique-se de ter o Python instalado e rode:</p>
        <pre><code>pip install opencv-python deepface tf-keras tk</code></pre>

        <h3>2. Como Rodar</h3>
        <p>Clone o repositório e execute o script principal:</p>
        <pre><code>git clone https://github.com/rogeriocabral30/face-id-tematica-cyberpunk.git
cd face-id-tematica-cyberpunk
python app.py</code></pre>
        <p><em>Nota: Na primeira execução, o DeepFace fará o download dos pesos do modelo VGG-Face (aprox. 500MB). Isso é normal.</em></p>

        <div class="author-section">
            <h2>👤 Autor</h2>
            <p><strong>Rogério Cabral</strong></p>
            <p>
                <a href="https://github.com/rogeriocabral30" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
                </a>
                <a href="https://www.linkedin.com/in/rog%C3%A9rio-cabral-609072397/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
                </a>
            </p>
        </div>
    </div>

</body>
</html>