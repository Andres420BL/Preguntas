matriz1 = [[' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ '],
           [' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ '],
           [' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ '],
           [' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ '],
           [' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ ', ' ◻︎ ']]

correcto = '☑'
incorrecto = '✖︎'
ls_preguntas = [
    '¿Qué es la programación?\n\n1. Proceso de escribir código\n2. Proceso de ejecutar código\n3. Proceso de depurar código\n4. Proceso de diseñar código',
    '¿Qué es un lenguaje de programación?\n\n1. Un conjunto de reglas gramaticales\n2. Un sistema de comunicación entre humanos\n3. Un conjunto de instrucciones para la computadora\n4. Un tipo de alfabeto',
    '¿Qué es un algoritmo?\n\n1. Un conjunto de instrucciones precisas\n2. Una idea vaga\n3. Una ecuación matemática\n4. Un lenguaje de programación',
    '¿Qué es un bucle?\n\n1. Una condición lógica\n2. Un error en el código\n3. Una repetición de instrucciones\n4. Una operación matemática',
    '¿Qué es una condición?\n\n1. Una instrucción para la computadora\n2. Una circunstancia bajo la cual se ejecuta una parte de código\n3. Una variable booleana\n4. Una ecuación matemática',
    '¿Qué es una variable?\n\n1. Un valor constante\n2. Una función matemática\n3. Un contenedor de datos\n4. Una condición lógica',
    '¿Qué es un tipo de datos?\n\n1. Una categoría de valores\n2. Un lenguaje de programación\n3. Una variable global\n4. Una función matemática',
    '¿Qué es una función?\n\n1. Un conjunto de instrucciones para realizar una tarea específica\n2. Una variable de tipo función\n3. Una clase en programación orientada a objetos\n4. Una operación matemática',
    '¿Qué es una clase?\n\n1. Un tipo de función\n2. Un conjunto de datos\n3. Un contenedor de variables\n4. Un bloque de código',
    '¿Qué es un objeto?\n\n1. Una instancia de una clase\n2. Un tipo de dato primitivo\n3. Una función en programación orientada a objetos\n4. Un tipo de lenguaje de programación',
    '¿Qué es una estructura de datos?\n\n1. Una organización de datos para ser procesados de manera eficiente\n2. Una lista de instrucciones\n3. Una variable global\n4. Una función matemática',
    '¿Qué es una biblioteca?\n\n1. Un conjunto de funciones y rutinas que realizan tareas específicas\n2. Una colección de libros\n3. Una estructura de datos\n4. Un tipo de lenguaje de programación',
    '¿Qué es una API?\n\n1. Una interfaz de programación de aplicaciones\n2. Una función matemática\n3. Una clase en programación orientada a objetos\n4. Un tipo de biblioteca',
    '¿Qué es la recursión?\n\n1. Un proceso en el que una función se llama a sí misma\n2. Un error en el código\n3. Una variable global\n4. Una función matemática',
    '¿Qué es la herencia?\n\n1. Un concepto en programación orientada a objetos donde una clase puede heredar atributos y métodos de otra clase\n2. Una función en programación funcional\n3. Una variable global\n4. Una operación matemática',
    '¿Qué es el polimorfismo?\n\n1. La capacidad de un objeto de tomar muchas formas\n2. Una estructura de datos\n3. Una función matemática\n4. Una clase en programación orientada a objetos',
    '¿Qué es la encapsulación?\n\n1. Ocultar los detalles de implementación de una clase y mostrar solo la funcionalidad\n2. Una función matemática\n3. Una estructura de datos\n4. Una biblioteca',
    '¿Qué es la abstracción?\n\n1. Simplificar la complejidad al ignorar los detalles innecesarios\n2. Una función en programación funcional\n3. Una variable global\n4. Una operación matemática',
    '¿Qué es la programación orientada a objetos?\n\n1. Un paradigma de programación que modela conceptos del mundo real como objetos\n2. Una función en programación funcional\n3. Un conjunto de instrucciones para la computadora\n4. Una estructura de datos',
    '¿Qué es la programación funcional?\n\n1. Un paradigma de programación que trata las computaciones como evaluaciones de funciones matemáticas\n2. Una biblioteca\n3. Un tipo de lenguaje de programación\n4. Un conjunto de datos',
    '¿Qué es la programación imperativa?\n\n1. Un paradigma de programación que se basa en el concepto de cambiar el estado del programa mediante la ejecución de comandos\n2. Una API\n3. Una clase en programación orientada a objetos\n4. Una función matemática',
    '¿Qué es la programación declarativa?\n\n1. Un paradigma de programación que se centra en qué debe hacer el programa, en lugar de cómo hacerlo\n2. Una estructura de datos\n3. Una variable global\n4. Una operación matemática',
    '¿Qué es la programación dinámica?\n\n1. Un método de resolver problemas computacionales dividiéndolos en subproblemas más pequeños\n2. Una API\n3. Una función en programación orientada a objetos\n4. Una variable global',
    '¿Qué es la programación concurrente?\n\n1. Un paradigma de programación que se ocupa de múltiples tareas que se ejecutan simultáneamente\n2. Una estructura de datos\n3. Una función matemática\n4. Una biblioteca',
    '¿Qué es la programación paralela?\n\n1. Un paradigma de programación que utiliza múltiples procesadores o núcleos para resolver un problema de manera simultánea\n2. Una API\n3. Una variable global\n4. Una clase en programación orientada a objetos']
   

ls_respuestas = ["1", "3", "1", "3", "2", "3", "1", "1", "1", "1",
                 "1", "1", "1", "1", "1", "1", "1", "1", "1", "1",
                 "1", "1", "1", "1", "1", "1"]

def fnt_pintarmatriz():
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            print(matriz1[i][j],end='   ')
        print('\n\n')

contador = 0

for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        import os
        os.system('cls')  
        fnt_pintarmatriz()
        print()
        print(ls_preguntas[contador])
        print()
        r = input('->')
        if r.lower() == ls_respuestas[contador]:
            matriz1[i][j] = correcto
        else:
            matriz1[i][j] = incorrecto
        contador += 1
