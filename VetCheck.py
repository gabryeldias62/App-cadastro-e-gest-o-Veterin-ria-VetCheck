import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import datetime
from fpdf import FPDF

class CadastroPaciente(tk.Tk):
    def __init__(self):
        super().__init__()

        self.configure(bg="#7B91B8")
        self.title("Cadastro de Paciente")
        self.geometry("650x600")

        self.label = tk.Label(self, text="Escolha uma opção:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 14, "bold"))
        self.label.pack(pady=10)

        self.login_button = tk.Button(self, text="Login", command=self.login, bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12))
        self.login_button.pack(pady=5)

        self.cadastrar_button = tk.Button(self, text="Cadastrar paciente", command=self.cadastrar, bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12))
        self.cadastrar_button.pack(pady=5)

        # Criar a tabela historico_pdfs se não existir
        conn = sqlite3.connect('pacientes.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS pacientes
                     (medico text, crmv text, nome text, peso real, sexo text, castrado text, historico text, tutor text, email text)''')
        conn.commit()
        conn.close()

    def cadastrar(self):
        self.withdraw()
        cadastro_form = CadastroForm(self)

    def login(self):
        self.withdraw()
        login_form = LoginForm(self)


class CadastroForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.configure(bg="#7B91B8")
        self.title("Cadastro de Paciente")
        self.geometry("650x600")

        self.label = tk.Label(self, text="Preencha os dados do paciente:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 14, "bold"))
        self.label.pack(pady=10)

        self.medico_label = tk.Label(self, text="Médico Veterinário:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.medico_label.pack()
        self.medico_entry = tk.Entry(self)
        self.medico_entry.pack()

        self.crmv_label = tk.Label(self, text="CRMV:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.crmv_label.pack()
        self.crmv_entry = tk.Entry(self)
        self.crmv_entry.pack()

        self.nome_label = tk.Label(self, text="Nome do paciente:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        self.peso_label = tk.Label(self, text="Peso:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.peso_label.pack()
        self.peso_entry = tk.Entry(self)
        self.peso_entry.pack()

        self.sexo_label = tk.Label(self, text="Sexo:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.sexo_label.pack()
        self.sexo_entry = tk.Entry(self)
        self.sexo_entry.pack()

        self.castrado_label = tk.Label(self, text="Castrado?", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.castrado_label.pack()
        self.castrado_entry = tk.Entry(self)
        self.castrado_entry.pack()

        self.historico_label = tk.Label(self, text="Histórico de cirurgia:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.historico_label.pack()
        self.historico_entry = tk.Entry(self)
        self.historico_entry.pack()

        self.tutor_label = tk.Label(self, text="Nome do Tutor:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.tutor_label.pack()
        self.tutor_entry = tk.Entry(self)
        self.tutor_entry.pack()

        self.email_label = tk.Label(self, text="Email do tutor:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.submit_button = tk.Button(self, text="Cadastrar", command=self.submit, bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
        self.submit_button.pack(pady=10)

        self.voltar_button = tk.Button(self, text="Voltar para login", command=self.voltar, bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
        self.voltar_button.pack(pady=10)

    def submit(self):
        medico = self.medico_entry.get()
        crmv = self.crmv_entry.get()
        nome = self.nome_entry.get()
        peso = self.peso_entry.get()
        sexo = self.sexo_entry.get()
        castrado = self.castrado_entry.get()
        historico_cirurgia = self.historico_entry.get()
        tutor = self.tutor_entry.get()
        email = self.email_entry.get()

        conn = sqlite3.connect('pacientes.db')
        c = conn.cursor()
        c.execute("INSERT INTO pacientes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (medico, crmv, nome, peso, sexo, castrado, historico_cirurgia, tutor, email))
        conn.commit()
        conn.close()

        messagebox.showinfo("Cadastro", "Paciente cadastrado com sucesso!")

    def voltar(self):
        self.destroy()
        self.master.deiconify()


class LoginForm(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.configure(bg="#7B91B8")
        self.title("Login")
        self.geometry("600x500")

        self.label = tk.Label(self, text="Faça o login:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 14, "bold"))
        self.label.pack(pady=10)

        self.medico_label = tk.Label(self, text="Nome do Médico Veterinário:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.medico_label.pack()
        self.medico_entry = tk.Entry(self)
        self.medico_entry.pack()

        self.nome_label = tk.Label(self, text="Nome do paciente:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.nome_label.pack()
        self.nome_entry = tk.Entry(self)
        self.nome_entry.pack()

        self.tutor_label = tk.Label(self, text="Nome do Tutor:", bg="#7B91B8", fg="black", font=("Petrobras Sans", 12))
        self.tutor_label.pack()
        self.tutor_entry = tk.Entry(self)
        self.tutor_entry.pack()

        self.submit_button = tk.Button(self, text="Login", command=self.submit, bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
        self.submit_button.pack(pady=10)

    def submit(self):
        medico = self.medico_entry.get()
        nome = self.nome_entry.get()
        tutor = self.tutor_entry.get()

        conn = sqlite3.connect('pacientes.db')
        c = conn.cursor()
        c.execute("SELECT * FROM pacientes WHERE medico=? AND nome=? AND tutor=?", (medico, nome, tutor))
        paciente = c.fetchone()
        conn.close()

        if paciente:
            self.destroy()
            tela_principal = TelaPrincipal(medico, paciente, tutor)
        else:
            messagebox.showerror("Erro", "Paciente não encontrado.")


class TelaPrincipal(tk.Toplevel):
    def __init__(self, medico, paciente, tutor):
        super().__init__()

        self.configure(bg="#7B91B8")
        self.title("Tela Principal")
        self.geometry("600x500")

        self.medico = medico
        self.paciente = paciente
        self.tutor = tutor


        # Criar a tabela historico_pacientes se não existir
        conn = sqlite3.connect('pacientes_historico.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS historico_pacientes
                     (data TEXT, nome_paciente TEXT, tutor TEXT, historico TEXT)''')
        conn.commit()
        conn.close()



        self.cabecalho_label = tk.Label(self, text=f"Medico: {medico}      Paciente: {paciente[2]}      Tutor: {tutor}", bg="#7B91B8", fg="black", font=("Petrobras Sans XBold", 14))
        self.cabecalho_label.pack(pady=10)

        self.separador = tk.Frame(self, height=2, width=400, bg="black")
        self.separador.pack(fill="x", pady=5)

        self.frame_botoes = tk.Frame(self, bg="#7B91B8")
        self.frame_botoes.pack(pady=10)

        # Dicionário para mapear botões aos modelos de texto
        self.modelos_texto = {
            "Receitas": "\nTel()\n\nData:\n\nNome:          Peso:\nIdade:         Espécie:     ",
            "Documentos": "\nEncaminhamento para exames :\n\nEncaminhamento paciente xxxx para  exame xxxxx\nSuspeita clínica:\nHistórico do paciente:",
            "Vacina": "\nVacinas:\n\nAplicação:\n\nData:\n\nPróxima aplicação:",
            "Vendas": "Modelo de venda:\n\n[Adicione aqui os detalhes da venda]",
            "Ficha Técnica": lambda: f"Nome: {paciente[2]}\nMédico: {medico}\nCRMV: {paciente[1]}\nPeso: {paciente[3]}\nSexo: {paciente[4]}\nCastrado: {paciente[5]}\nHistórico de cirurgia: {paciente[6]}\nTutor: {tutor}\nEmail do Tutor: {paciente[8]}"
        }

        # Botões com base nos modelos de texto
        row_counter = 0
        col_counter = 0
        for texto, modelo in self.modelos_texto.items():
            botao = tk.Button(self.frame_botoes, text=texto, command=lambda modelo=modelo: self.exibir_modelo_texto_editavel(texto, modelo), bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
            botao.grid(row=row_counter, column=col_counter, padx=10, pady=5)
            row_counter += 1
            if row_counter > 2:
                row_counter = 0
                col_counter += 1

        self.botao_historico_paciente = tk.Button(self.frame_botoes, text="Histórico Paciente", command=self.exibir_historico_paciente, bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
        self.botao_historico_paciente.grid(row=3, column=0, padx=10, pady=5)

        self.botao_voltar = tk.Button(self, text="Voltar", command=self.voltar, bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
        self.botao_voltar.pack(pady=10)

    def exibir_modelo_texto_editavel(self, titulo, modelo):
        popup = tk.Toplevel(self)
        popup.title(f"Editar Modelo de Texto - {titulo}")
        popup.geometry("600x500")
        popup.configure(bg="#7B91B8")

        if callable(modelo):
            modelo_texto = modelo()
        else:
            modelo_texto = modelo

        texto_editavel = tk.Text(popup, wrap="word", width=60, height=20)
        texto_editavel.insert("1.0", modelo_texto)
        texto_editavel.pack(padx=10, pady=10)

        salvar_button = tk.Button(popup, text="Salvar Alterações", command=lambda: self.salvar_alteracoes(titulo, texto_editavel.get("1.0", "end-1c")), bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
        salvar_button.pack(pady=10)

        exportar_pdf_button = tk.Button(popup, text="Exportar PDF", command=lambda: self.exportar_pdf(titulo, texto_editavel.get("1.0", "end-1c")), bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
        exportar_pdf_button.pack(pady=10)

    def salvar_alteracoes(self, titulo, texto):
        messagebox.showinfo("Sucesso", "Alterações salvas com sucesso!")
        # Aqui você pode implementar o código para salvar as alterações no modelo de texto
        # Por exemplo, pode atualizar o dicionário de modelos de texto com o novo texto.

    def exportar_pdf(self, titulo, texto):
        filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if filename:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=titulo, ln=True, align='C')
            pdf.cell(200, 10, txt="", ln=True)
            pdf.multi_cell(0, 10, txt=texto)
            pdf.output(filename)
            messagebox.showinfo("PDF Exportado", "PDF exportado com sucesso!")

    def exibir_historico_paciente(self):
        if hasattr(self, 'popup'):  # Verifica se já existe uma janela popup
            self.popup.destroy()  # Destroi a janela popup se já existe

        self.popup = tk.Toplevel(self)
        self.popup.title("Histórico do Paciente")
        self.popup.geometry("600x500")
        self.popup.configure(bg="#7B91B8")
   
    # Carregar histórico do paciente do banco de dados
        conn = sqlite3.connect('pacientes_historico.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS historico_pacientes (historico TEXT)")
        c.execute("SELECT historico FROM historico_pacientes")
        historico = c.fetchone()
        conn.close()

        if historico:
            historico = historico[0]
            

            historico_texto = tk.Text(self.popup, wrap="word", width=60, height=20)
            historico_texto.insert("1.0", historico)
            historico_texto.pack(padx=10, pady=10)

            salvar_button = tk.Button(self.popup, text="Salvar Alterações", command=lambda: self.salvar_historico(historico_texto.get("1.0", "end-1c")), bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
            salvar_button.pack(pady=10)
        else:
            print("Histórico do Paciente vazio.")

            historico_texto = tk.Text(self.popup, wrap="word", width=60, height=20)
            historico_texto.insert("1.0", "Histórico vazio.")
            historico_texto.pack(padx=10, pady=10)

            salvar_button = tk.Button(self.popup, text="Salvar Alterações", command=lambda: self.salvar_historico(historico_texto.get("1.0", "end-1c")), bg="#BCD1E5", fg="black", font=("Petrobras Sans", 12), width=20, height=2)
            salvar_button.pack(pady=10)


    def salvar_historico(self, novo_historico):
        conn = sqlite3.connect('pacientes_historico.db')
        c = conn.cursor()
        
        # Atualizar o histórico do paciente no banco de dados
        c.execute("CREATE TABLE IF NOT EXISTS historico_pacientes (historico TEXT)")
        c.execute("DELETE FROM historico_pacientes")  # Limpa a tabela antes de inserir o novo histórico
        c.execute("INSERT INTO historico_pacientes (historico) VALUES (?)", (novo_historico,))
        conn.commit()

    # Fechar a conexão com o banco de dados
        conn.close()

        messagebox.showinfo("Sucesso", "Histórico do paciente atualizado com sucesso!")

    # Atualizar o conteúdo da caixa de texto
        self.exibir_historico_paciente()
    
    
    def voltar(self):
        self.destroy()
        self.master.deiconify()


if __name__ == "__main__":
    app = CadastroPaciente()
    app.mainloop()