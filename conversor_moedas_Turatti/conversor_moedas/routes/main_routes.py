from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

# Importa a lógica de conversão do novo serviço
from services.conversion import convert_currency

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("login.html")

@main_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    resultado = None
    if request.method == 'POST':
        de = request.form['de']
        para = request.form['para']
        valor = float(request.form['valor'])

        resultado = convert_currency(valor, de, para)
    
    return render_template('dashboard.html', resultado=resultado)


# ROTA ADICIONADA: Corrige o erro e torna a página de perfil funcional
@main_bp.route("/perfil")
@login_required
def perfil():
    # Passa os dados do perfil do usuário logado para o template
    return render_template("perfil.html", perfil=current_user.perfil)