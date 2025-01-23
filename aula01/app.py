import customtkinter as ctk #Importando a biblioteca

janela = ctk.CTk() #Criar a nossa janela

# janela._set_appearance_mode("light") #Ativa o modo claro

btn = ctk.CTkButton(janela, text="Botão") #Cria o botão
btn.pack() #mostra o botão na interface gráfica

janela.mainloop()