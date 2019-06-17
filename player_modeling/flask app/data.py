from os import listdir

def get_notebook_files():
    notebooks_names=[]
    for notebook_name in listdir("templates//notebooks"):
        notebooks_names.append(notebook_name)

    return notebooks_names

def load_about():
    about_files=["Questões a serem respondidas.html","Sobre o jogo.html","Dataset.html","Modelagem.html","Aspectos modelados.html","Possíveis Aplicações.html","Progresso.html"]
    return about_files
