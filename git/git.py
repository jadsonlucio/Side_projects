import cmd

GLOBAL_CMD="--global"

logs=[]

#comandos git
comando={
    "iniciar_repositorio_local":"git init",
    "configuracoes":"git config",
    "status":"git status",
    "adicionar_commit":"git add",
    "fazer_commit":"git commit",
    "adicionar_local_remoto":"git remote add origin",
    "add_commits_repo_remoto":"git push -u origin master"
}

sub_comandos_config={
    "nome_usuario":"user.name",
    "email":"user.email"
}

def run_command(command):
    codigo_resultado,texto_resultado=cmd.run_command(command)
    logs.append([command,codigo_resultado,texto_resultado])
    return codigo_resultado,texto_resultado

def juntar_comandos(array_comandos):
    comando_final=""
    for comando in array_comandos:
        if(comando!=array_comandos[len(array_comandos)-1]):
            comando_final=comando_final+comando+" && "
        else:
            comando_final=comando_final+comando
    return comando_final

class git_class():
    #gets e sets

    def get_comando_abrir_diretorio(self):
        return "cd "+self.endereco_repositorio_local

    def get_arquivos_modificados(self):
        status=self.get_status()
        linhas=status.split("\n")
        for cont_linha_1 in range(0,len(linhas)):
            if("git add <file>" in linhas[cont_linha_1]):
                for cont_linha_2 in range(cont_linha_1+2,len(linhas)):
                    if(len(linhas[cont_linha_2])==0):
                        return [linha.replace("\t","") for linha in linhas[cont_linha_1+2:cont_linha_2]]

        return "Nada encontrado"

    def get_status(self):
        codigo_resultado, texto_resultado = run_command(comando["status"])
        if(codigo_resultado==0):
            return "Um erro aconteceu"
        else:
            return texto_resultado

    def __init__(self,endereco_repositorio_local,endereco_repositorio_online,nome_contribuidor,email_contribuidor):
        self.endereco_repositorio_local=endereco_repositorio_local
        self.endereco_repositorio_online=endereco_repositorio_online
        self.nome_contribuidor=nome_contribuidor
        self.email_contribuidor=email_contribuidor

    def adicionar_commits_repositorio_remoto(self):
        comando_abrir_diretorio = self.get_comando_abrir_diretorio()
        comando_adicionar_commits=comando["add_commits_repo_remoto"]
        comando_final=juntar_comandos([comando_abrir_diretorio,comando_adicionar_commits])
        codigo_resultado, texto_resultado = run_command(comando_final)

        return codigo_resultado,texto_resultado

    def adicionar_repositorio_remoto(self,endereco_repositorio=None):
        if(endereco_repositorio!=None):
            self.endereco_repositorio_online=endereco_repositorio
        comando_abrir_diretorio = self.get_comando_abrir_diretorio()
        comando_adicionar_repositorio_remoto = comando["adicionar_local_remoto"]+" "+self.endereco_repositorio_online
        comando_final=juntar_comandos([comando_abrir_diretorio,comando_adicionar_repositorio_remoto])
        codigo_resultado, texto_resultado=run_command(comando_final)

        return codigo_resultado, texto_resultado

    def adicionar_arquivo_commit(self,endereco_arquivo):
        comando_abrir_diretorio = self.get_comando_abrir_diretorio()
        comando_add_commit=comando["adicionar_commit"]+" "+endereco_arquivo
        comando_final=juntar_comandos([comando_abrir_diretorio,comando_add_commit])
        codigo_resultado, texto_resultado = run_command(comando_final)

        return codigo_resultado, texto_resultado

    def fazer_comit_arquivo(self,endereco_arquivo,mensagem=None):
        comando_abrir_diretorio = self.get_comando_abrir_diretorio()
        comando_fazer_commit=comando["fazer_commit"]
        if(mensagem!=None):
            comando_fazer_commit=comando_fazer_commit+" -m"+" "+"\""+str(mensagem)+"\""
        comando_fazer_commit=comando_fazer_commit+" "+endereco_arquivo
        comando_final=juntar_comandos([comando_abrir_diretorio,comando_fazer_commit])
        codigo_resultado, texto_resultado = run_command(comando_final)

        if(codigo_resultado==1 and len(texto_resultado.split("\n"))<=2):
            texto_resultado=texto_resultado.split("\n")
            texto_resultado=texto_resultado[-1].split(",")
        else:
            texto_resultado=0

        return codigo_resultado, texto_resultado


    def iniciar_repositorio_local(self):
        comando_abrir_diretorio=self.get_comando_abrir_diretorio()
        return run_command(juntar_comandos([comando_abrir_diretorio,comando["iniciar_repositorio_local"]]))

    def iniciar_credenciais(self,nome=None,email=None,credenciais_globais=True):
        if(nome!=None):
            self.nome_contribuidor=nome
        if(email!=None):
            self.email_contribuidor=email

        if(credenciais_globais==True):
            comando_credenciais_nome=comando["configuracoes"]+" "+GLOBAL_CMD+" "+sub_comandos_config["nome_usuario"]+\
                                    " "+self.nome_contribuidor
            comando_credenciais_email = comando["configuracoes"] + " " + GLOBAL_CMD + " "+sub_comandos_config["email"]+\
                                        " "+ self.email_contribuidor
            comando_final=juntar_comandos([comando_credenciais_nome,comando_credenciais_email])

        else:
            comando_abrir_diretorio=self.get_comando_abrir_diretorio()

            comando_credenciais_nome = comando["configuracoes"] + " " + sub_comandos_config[
                "nome_usuario"] +" "+ self.nome_contribuidor
            comando_credenciais_email = comando["configuracoes"] +" " + sub_comandos_config[
                "email"] +" " + self.email_contribuidor
            comando_final = juntar_comandos([comando_abrir_diretorio, comando_credenciais_nome, comando_credenciais_email])

        codigo_resultado, texto_resultado = run_command(comando_final)

        return codigo_resultado, texto_resultado


