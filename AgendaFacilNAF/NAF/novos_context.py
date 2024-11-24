def faz_parte_professor(request):
    professor = False
    if request.user.is_authenticated:
        if request.user.groups.filter(name="professor").exists():
            professor = True   
    return {"professor": professor}

def faz_parte_aluno(request):
    aluno = False
    if request.user.is_authenticated:
        if request.user.groups.filter(name="aluno").exists():
            aluno = True   
    return {"aluno": aluno}

def faz_parte_adm(request):
    adm = False
    if request.user.is_authenticated:
        if request.user.groups.filter(name="administrador").exists():
            adm = True   
    return {"administrador": adm}
