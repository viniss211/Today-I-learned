//function to identify if the user enters ith an action or a value
function calcular(tipo, valor) {
    if (tipo === 'acao') {
        if (valor === 'c') {
            //limpar o visor
            document.getElementById('resultado').value = ''
        }
        if (valor === '+' || valor === '-' || valor === '*' || valor === '/' || valor === '.') {
            document.getElementById('resultado').value += valor
        }
        //struct to resolve 
        if (valor === '=') {
            if (document.getElementById('resultado').value[0] == '√') {
                let text = document.getElementById('resultado').value
                let result = text.replace("√", " ")
                document.getElementById('resultado').value = Math.sqrt(result)

                /*var teste = Math.sqrt(document.getElementById('resultado').value[1])
                document.getElementById('resultado').value = teste*/
            }
            var valor_campo = eval(document.getElementById('resultado').value)
            document.getElementById('resultado').value = valor_campo
        }
        //struct to square root
        if (valor === "√") {

            document.getElementById('resultado').value = '√' + document.getElementById('resultado').value

        }
        //struct to pow of
        if (valor === "pow") {

            document.getElementById('resultado').value += '**'

        }
        //struct to add more values
    } else if (tipo === 'valor') {

        document.getElementById('resultado').value += valor
    }
}